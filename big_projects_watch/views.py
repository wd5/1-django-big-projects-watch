# coding=UTF-8
import os, re

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _
from big_projects_watch.forms import *
from big_projects_watch.models import *


def check_config_prerequisits():
    missing_cps = []
    
    if SiteConfig.objects.count() != 1:
        missing_cps.append(_("Creation of (exactly) one SiteConfig object in the Django admin \
with the general config params and non-dynamical contents."))
    
    if Project.objects.count() != 1:
        missing_cps.append(_("Creation of (exactly) one Project object in the Django admin \
with general information about the project."))
    if ProjectGoalGroup.objects.count() == 0 or ProjectGoal.objects.count() == 0:
        missing_cps.append(_("Creation of at least one ProjectGoalGroup object in the Django admin \
containing at least one ProjectGoal."))
        
    context = {
      'missing_cps': missing_cps,  
    }
    cp_met = len(missing_cps) == 0
    return cp_met, render_to_response('config_prerequisits.html', context)


def get_project():
    return Project.objects.all()[0]


def get_site_config(request):
    site_config = SiteConfig.objects.all()[0]
    site_config.with_public_docs = getattr(settings, 'WITH_PUBLIC_DOCS', False)
    
    site_config.use_pdfjs_viewer = False
    site_config.browser = 'Unknown'
    if 'Mozilla'.lower() in request.META['HTTP_USER_AGENT'].lower():
        site_config.use_pdfjs_viewer = True
        site_config.browser = 'Mozilla'
    if 'Safari'.lower() in request.META['HTTP_USER_AGENT'].lower():
        site_config.use_pdfjs_viewer = True
        site_config.browser = 'Safari'
    if 'Chrome'.lower() in request.META['HTTP_USER_AGENT'].lower():
        site_config.use_pdfjs_viewer = True
        site_config.browser = 'Chrome'
    if 'Opera'.lower() in request.META['HTTP_USER_AGENT'].lower():
        site_config.use_pdfjs_viewer = True
        site_config.browser = 'Opera'
    if 'MSIE'.lower() in request.META['HTTP_USER_AGENT'].lower():
        site_config.browser = 'MSIE'
        
    return site_config


def get_document_relation_form(request, document):
    form = DocumentRelationForm(initial={'document_id': document.id})
    form_valid = False
    
    if request.method == 'POST' and 'document_relation_form' in request.POST:
        tmp_form = DocumentRelationForm(request.POST)
        if tmp_form.is_valid():
            dr = DocumentRelation()
            dr.document = Document.objects.get(pk=tmp_form.cleaned_data['document_id'])
            dr.content_type = ContentType.objects.get(app_label="big_projects_watch", model=tmp_form.cleaned_data['related_to_type'])
            dr.object_id = tmp_form.cleaned_data['related_to_id'].id
            dr.description = tmp_form.cleaned_data['description']
            dr.page = tmp_form.cleaned_data['page_number']
            dr.comments = tmp_form.cleaned_data['comments']
            dr.activation_hash = os.urandom(16).encode('hex')
            dr.save()
            
            email_users = User.objects.filter(userprofile__receive_new_document_relation_emails=True)
            
            try:
                for user in email_users:
                    sep = "-----------------------------------------------------------\n"
                    subject = _("NEW_DOCUMENT_RELATION_EMAIL_SUBJECT") + '"' + unicode(dr.document) + '"'
                    message  = _("NEW_DOCUMENT_RELATION_EMAIL_MESSAGE") + "\n\n" + sep
                    message += unicode(dr.content_type) + ": " + unicode(dr.content_object) + "\n" + sep
                    message += _("Description of the relation (displayed on page)") + ":\n"
                    message += dr.description + "\n" + sep
                    message += _("Page") + " " + unicode(dr.page) + ", "
                    message += 'http://%s%s?page=%s' % (Site.objects.get_current().domain, dr.document.get_absolute_url(), str(dr.page)) + "\n" + sep
                    message += _("Additional comment (not publicly displayed)") + ":\n"
                    message += dr.comments + "\n" + sep + "\n"
                    
                    if user.has_perm('big_projects_watch.change_documentrelation') and user.email:
                        message += _("NEW_DOCUMENT_RELATION_EMAIL_MESSAGE_ACTIVATION") + "\n"
                        message += 'http://%s/%s?activation_hash=%s' \
                            % (Site.objects.get_current().domain, _("activate_document_relation_url"), dr.activation_hash) + "\n"
                    
                    send_mail(subject, message, settings.EMAIL_FROM, [user.email], fail_silently=False)
            except AttributeError:
                pass
            
            form_valid = True
        else:
            form = tmp_form
            
    return form, form_valid


def get_comment_form(request, content_type, object_id):
    form = CommentForm(initial={
        'content_type': content_type,
        'object_id': object_id,
    })
    form_valid = False
    
    if request.method == 'POST' and 'comment_form' in request.POST:
        tmp_form = CommentForm(request.POST)
        if tmp_form.is_valid():
            c = Comment()
            c.content_type = ContentType.objects.get(app_label="big_projects_watch", model=tmp_form.cleaned_data['content_type'])
            c.object_id = tmp_form.cleaned_data['object_id']
            c.username = tmp_form.cleaned_data['username']
            c.comment = tmp_form.cleaned_data['comment']
            c.page = tmp_form.cleaned_data['page_number']
            c.activation_hash = os.urandom(16).encode('hex')
            c.save()
            
            email_users = User.objects.filter(userprofile__receive_new_comment_emails=True)
            
            try:
                for user in email_users:
                    sep = "-----------------------------------------------------------\n"
                    subject = _("NEW_COMMENT_EMAIL_SUBJECT") + '"' + unicode(c.content_object) + '"'
                    message  = _("NEW_COMMENT_EMAIL_MESSAGE") + "\n\n" + sep
                    message += _("Name") + ": " + unicode(c.username) + "\n"
                    message += _("Comment") + ":\n"
                    message += c.comment + "\n" + sep
                    message += 'http://%s%s' % (Site.objects.get_current().domain, c.content_object.get_absolute_url()) + "\n" + sep + "\n"
                    
                    if user.has_perm('big_projects_watch.change_comment') and user.email:
                        message += _("NEW_COMMENT_EMAIL_MESSAGE_ACTIVATION") + "\n"
                        message += 'http://%s/%s?activation_hash=%s' \
                            % (Site.objects.get_current().domain, _("activate_comment_url"), c.activation_hash) + "\n"
                    
                    send_mail(subject, message, settings.EMAIL_FROM, [user.email], fail_silently=False)
            except AttributeError:
                pass
            
            form_valid = True
        else:
            form = tmp_form
            
    return form, form_valid


def index(request):
    cp, response = check_config_prerequisits()
    if not cp:
        return response
    
    context = {
        'site_config': get_site_config(request),
        'project': get_project(),
        'current_project_goal_group': ProjectGoalGroup.objects.get_current(),
        'project_part_list': ProjectPart.objects.all(),
        'latest_event_list': Event.objects.all()[0:8],
        'latest_document_list': Document.objects.all()[0:8],
        'latest_document_relation_list': DocumentRelation.objects.filter(published=True).order_by('-date_added')[0:3],
        'comment_list': Comment.objects.filter(published=True)[0:3],
    }
    return render_to_response('index.html', context)


def project(request):
    cp, response = check_config_prerequisits()
    if not cp:
        return response
    
    project_part_list = ProjectPart.objects.all()
    context = {
        'site_config': get_site_config(request),
        'project': get_project(),
        'project_goal_group_list': ProjectGoalGroup.objects.all().order_by('event'),
        'project_part_list': project_part_list,
        'comment_list': Comment.objects.filter(published=True, content_type__model="projectpart")[0:8],
    }
    return render_to_response('project.html', context)


def project_part(request, project_part_id):
    cp, response = check_config_prerequisits()
    if not cp:
        return response
    
    project_part = get_object_or_404(ProjectPart, pk=project_part_id)
    
    comment_form, comment_form_valid = get_comment_form(request, 'projectpart', project_part.id)
    
    context = RequestContext(request, {
        'site_config': get_site_config(request),
        'project': get_project(),
        'project_part': project_part,
        'document_relation_list': project_part.document_relations.filter(published=True),
        'comment_form': comment_form,
        'comment_form_valid': comment_form_valid,
        'comment_list': project_part.user_comments.filter(published=True),
    })
    return render_to_response('project_part.html', context)


def process(request):
    cp, response = check_config_prerequisits()
    if not cp:
        return response
    
    event_list = Event.objects.all()
    context = {
        'site_config': get_site_config(request),
        'project': get_project(),
        'project_goal_group_list': ProjectGoalGroup.objects.all().order_by('event'),
        'event_list': event_list,
        'comment_list': Comment.objects.filter(published=True, content_type__model="event")[0:8],
    }
    return render_to_response('process.html', context)


def event(request, event_id):
    cp, response = check_config_prerequisits()
    if not cp:
        return response
    
    event = get_object_or_404(Event, pk=event_id)
    
    comment_form, comment_form_valid = get_comment_form(request, 'event', event.id)
    
    context = RequestContext(request, {
        'site_config': get_site_config(request),
        'project': get_project(),
        'event': event,
        'document_relation_list': event.document_relations.filter(published=True),
        'comment_form': comment_form,
        'comment_form_valid': comment_form_valid,
        'comment_list': event.user_comments.filter(published=True),
    })
    return render_to_response('event.html', context)


def participants(request):
    cp, response = check_config_prerequisits()
    if not cp:
        return response
    
    context = {
        'site_config': get_site_config(request),
        'project': get_project(),
        'ad_participant_list': Participant.objects.filter(participant_type='AD'),
        'po_participant_list': Participant.objects.filter(participant_type='PO'),
        'ci_participant_list': Participant.objects.filter(participant_type='CI'),
        'co_participant_list': Participant.objects.filter(participant_type='CO'),
        'se_participant_list': Participant.objects.filter(participant_type='SE'),
        'comment_list': Comment.objects.filter(published=True, content_type__model="participant")[0:8],
    }
    return render_to_response('participants.html', context)


def participant(request, participant_id):
    cp, response = check_config_prerequisits()
    if not cp:
        return response
    
    participant = get_object_or_404(Participant, pk=participant_id)
    
    comment_form, comment_form_valid = get_comment_form(request, 'participant', participant.id)
    
    context = RequestContext(request, {
        'site_config': get_site_config(request),
        'project': get_project(),
        'participant': participant,
        'document_relation_list': participant.document_relations.filter(published=True),
        'comment_form': comment_form,
        'comment_form_valid': comment_form_valid,
        'comment_list': participant.user_comments.filter(published=True),
    })
    return render_to_response('participant.html', context)


def documents(request):
    cp, response = check_config_prerequisits()
    if not cp:
        return response
    
    document_list = Document.objects.all().order_by('title')
    context = {
        'site_config': get_site_config(request),
        'project': get_project(),
        'document_list': document_list,
        'latest_document_relation_list': DocumentRelation.objects.filter(published=True).order_by('-date_added')[0:6],
        'comment_list': Comment.objects.filter(published=True, content_type__model="document")[0:6],
    }
    return render_to_response('documents.html', context)


def document(request, document_id):
    
    cp, response = check_config_prerequisits()
    if not cp:
        return response
    
    document = get_object_or_404(Document, pk=document_id)
    document_relation_form, document_relation_form_valid = get_document_relation_form(request, document)
    comment_form, comment_form_valid = get_comment_form(request, 'document', document.id)

    context = RequestContext(request, {
        'site_config': get_site_config(request),
        'project': get_project(),
        'document': document,
        'document_relation_form': document_relation_form,
        'document_relation_form_valid': document_relation_form_valid,
        'document_relation_list': DocumentRelation.objects.filter(document=document).filter(published=True).order_by("page"),
        'comment_form': comment_form,
        'comment_form_valid': comment_form_valid,
        'comment_list': document.user_comments.filter(published=True),
        
    })
    return render_to_response('document.html', context)


#PublicDocs
def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:
        
        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
    
    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 


#PublicDocs
def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.
    
    '''
    query = None # Query to search for every search term        
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query 


def search(request):
    
    if ('q' in request.GET) and request.GET['q'].strip():
        
        query_string = request.GET['q']
        
        entry_query = get_query(query_string, ['name', 'description',])
        project_part_list = ProjectPart.objects.select_related().filter(entry_query)
        
        entry_query = get_query(query_string, ['name', 'description',])
        participant_list = Participant.objects.select_related().filter(entry_query)
        
        entry_query = get_query(query_string, ['title', 'description',])
        event_list = Event.objects.select_related().filter(entry_query)
        
        entry_query = get_query(query_string, ['document__title', 'content',])
        found_pages = Page.objects.select_related().filter(entry_query).order_by('document','number')
        
        document_list = []
        for page in found_pages:
            page.document.found_page = page.number
            document_list.append(page.document)
        
        context = RequestContext(request, {
            'site_config': get_site_config(request),
            'project': get_project(),
            'query': query_string,
            'project_part_list': project_part_list,
            'participant_list': participant_list,
            'event_list': event_list,
            'document_list': document_list,
        })
        
        return render_to_response('search.html', context)
    else:
        return HttpResponse("An Error occured!")


def contact(request):
    cp, response = check_config_prerequisits()
    if not cp:
        return response
    
    image_list = Image.objects.all()
    
    context = {
        'site_config': get_site_config(request),
        'project': get_project(),
        'image_list': image_list,
    }
    return render_to_response('contact.html', context)


def activate_document_relation(request):
    dr = get_object_or_404(DocumentRelation, activation_hash=request.GET['activation_hash'])
    
    res  = '<!DOCTYPE html><html><head><meta charset="utf-8"></head><body>'
    res += '<div style="margin:20px;padding:20px;border:1px solid #999;float:left;color:#333;font-size:14px;'
    res += 'font-family:arial, helvetica, sans-serif;">'
    
    if not dr.published:
        dr.published = True
        dr.save()
        res += _("The following document relation was activated for publication on website:") + '<br><br>'
        res += unicode(dr)
    else:
        res += _("Document relation already activated.")
    
    res += '</div></body></html>'
    
    return HttpResponse(res)


def activate_comment(request):
    c = get_object_or_404(Comment, activation_hash=request.GET['activation_hash'])
    
    res  = '<!DOCTYPE html><html><head><meta charset="utf-8"></head><body>'
    res += '<div style="margin:20px;padding:20px;border:1px solid #999;float:left;color:#333;font-size:14px;'
    res += 'font-family:arial, helvetica, sans-serif;">'
    
    if not c.published:
        c.published = True
        c.save()
        res += _("The following comment was activated for publication on website:") + '<br><br>'
        res += unicode(c)
    else:
        res += _("Comment already activated.")
    
    res += '</div></body></html>'
    
    return HttpResponse(res)
    
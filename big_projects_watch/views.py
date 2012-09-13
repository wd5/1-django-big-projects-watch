# coding=UTF-8
import re

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _
from big_projects_watch.forms import *
from big_projects_watch.models import *

try:
    from documents.models  import Document as PublicdocsDoc, Page as PublicdocsPage
    WITH_PUBLIC_DOCS = True
except ImportError, e:
    WITH_PUBLIC_DOCS = False


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


def get_site_config():
    site_config = SiteConfig.objects.all()[0]
    site_config.with_public_docs = WITH_PUBLIC_DOCS
    return site_config


def get_document_relation_form(request, document):
    form = DocumentRelationForm(initial={'document_id': document.id})
    form_valid = False
    
    if request.method == 'POST' and 'document_relation_form' in request.POST:
        tmp_form = DocumentRelationForm(request.POST)
        if tmp_form.is_valid():
            dr = DocumentRelation()
            dr.document = Document.objects.get(pk=tmp_form.cleaned_data['document_id'])
            dr.related_to_type = ContentType.objects.get(app_label="big_projects_watch", model=tmp_form.cleaned_data['related_to_type'])
            dr.related_to_id = tmp_form.cleaned_data['related_to_id'].id
            dr.description = tmp_form.cleaned_data['description']
            dr.page = tmp_form.cleaned_data['page_number']
            dr.save()
            form_valid = True
        else:
            form = tmp_form
            
    return form, form_valid


def get_comment_form(request, commented_object_type, commented_object_id):
    form = CommentForm(initial={
        'commented_object_type': commented_object_type,
        'commented_object_id': commented_object_id,
    })
    form_valid = False
    
    if request.method == 'POST' and 'comment_form' in request.POST:
        tmp_form = CommentForm(request.POST)
        if tmp_form.is_valid():
            c = Comment()
            c.commented_object_type = ContentType.objects.get(app_label="big_projects_watch", model=tmp_form.cleaned_data['commented_object_type'])
            c.commented_object_id = tmp_form.cleaned_data['commented_object_id']
            c.username = tmp_form.cleaned_data['username']
            c.comment = tmp_form.cleaned_data['comment']
            c.page = tmp_form.cleaned_data['page_number']
            c.save()
            form_valid = True
        else:
            form = tmp_form
            
    return form, form_valid


def index(request):
    cp, response = check_config_prerequisits()
    if not cp:
        return response
    
    context = {
        'site_config': get_site_config(),
        'project': get_project(),
        'current_project_goal_group': ProjectGoalGroup.objects.get_current(),
        'project_part_list': ProjectPart.objects.all(),
        'latest_event_list': Event.objects.all()[0:8],
        'latest_document_list': Document.objects.all()[0:8],
        'latest_document_relation_list': DocumentRelation.objects.filter(published=True).order_by('-date_added')[0:4],
        'comment_list': Comment.objects.filter(published=True)[0:4],
    }
    return render_to_response('index.html', context)


def project(request):
    cp, response = check_config_prerequisits()
    if not cp:
        return response
    
    project_part_list = ProjectPart.objects.all()
    context = {
        'site_config': get_site_config(),
        'project': get_project(),
        'project_goal_group_list': ProjectGoalGroup.objects.all().order_by('event'),
        'project_part_list': project_part_list,
        'comment_list': Comment.objects.filter(published=True, commented_object_type__name="project part")[0:8],
    }
    return render_to_response('project.html', context)


def project_part(request, project_part_id):
    cp, response = check_config_prerequisits()
    if not cp:
        return response
    
    project_part = get_object_or_404(ProjectPart, pk=project_part_id)
    
    comment_form, comment_form_valid = get_comment_form(request, 'projectpart', project_part.id)
    
    context = RequestContext(request, {
        'site_config': get_site_config(),
        'project': get_project(),
        'project_part': project_part,
        'document_relation_list': DocumentRelation.objects.filter(published=True, related_to_type__name="project part", related_to_id=project_part_id),
        'comment_form': comment_form,
        'comment_form_valid': comment_form_valid,
        'comment_list': Comment.objects.filter(published=True, commented_object_type__name="project part", commented_object_id=project_part_id),
    })
    return render_to_response('project_part.html', context)


def process(request):
    cp, response = check_config_prerequisits()
    if not cp:
        return response
    
    event_list = Event.objects.all()
    context = {
        'site_config': get_site_config(),
        'project': get_project(),
        'project_goal_group_list': ProjectGoalGroup.objects.all().order_by('event'),
        'event_list': event_list,
        'comment_list': Comment.objects.filter(published=True, commented_object_type__name="event")[0:8],
    }
    return render_to_response('process.html', context)


def event(request, event_id):
    cp, response = check_config_prerequisits()
    if not cp:
        return response
    
    event = get_object_or_404(Event, pk=event_id)
    
    comment_form, comment_form_valid = get_comment_form(request, 'event', event.id)
    
    context = RequestContext(request, {
        'site_config': get_site_config(),
        'project': get_project(),
        'event': event,
        'document_relation_list': DocumentRelation.objects.filter(published=True, related_to_type__name="event", related_to_id=event_id),
        'comment_form': comment_form,
        'comment_form_valid': comment_form_valid,
        'comment_list': Comment.objects.filter(published=True, commented_object_type__name="event", commented_object_id=event_id),
    })
    return render_to_response('event.html', context)


def participants(request):
    cp, response = check_config_prerequisits()
    if not cp:
        return response
    
    context = {
        'site_config': get_site_config(),
        'project': get_project(),
        'ad_participant_list': Participant.objects.filter(participant_type='AD'),
        'po_participant_list': Participant.objects.filter(participant_type='PO'),
        'ci_participant_list': Participant.objects.filter(participant_type='CI'),
        'co_participant_list': Participant.objects.filter(participant_type='CO'),
        'se_participant_list': Participant.objects.filter(participant_type='SE'),
        'comment_list': Comment.objects.filter(published=True, commented_object_type__name="participant")[0:8],
    }
    return render_to_response('participants.html', context)


def participant(request, participant_id):
    cp, response = check_config_prerequisits()
    if not cp:
        return response
    
    participant = get_object_or_404(Participant, pk=participant_id)
    
    comment_form, comment_form_valid = get_comment_form(request, 'participant', participant.id)
    
    context = RequestContext(request, {
        'site_config': get_site_config(),
        'project': get_project(),
        'participant': participant,
        'document_relation_list': DocumentRelation.objects.filter(published=True, related_to_type__name="participant", related_to_id=participant_id),
        'comment_form': comment_form,
        'comment_form_valid': comment_form_valid,
        'comment_list': Comment.objects.filter(published=True, commented_object_type__name="participant", commented_object_id=participant_id),
    })
    return render_to_response('participant.html', context)


def documents(request):
    cp, response = check_config_prerequisits()
    if not cp:
        return response
    
    document_list = Document.objects.all().order_by('title')
    context = {
        'site_config': get_site_config(),
        'project': get_project(),
        'document_list': document_list,
        'latest_document_relation_list': DocumentRelation.objects.filter(published=True).order_by('-date_added')[0:8],
        'comment_list': Comment.objects.filter(published=True, commented_object_type__name="document")[0:8],
    }
    return render_to_response('documents.html', context)


def document(request, document_id):
    
    cp, response = check_config_prerequisits()
    if not cp:
        return response
    
    document = get_object_or_404(Document, pk=document_id)
    
    publicdocs_doc = None
    if WITH_PUBLIC_DOCS:
        publicdocs_docs = PublicdocsDoc.objects.filter(title=document.title)
        if len(publicdocs_docs) == 1:
            publicdocs_doc = publicdocs_docs[0]
    
    document_relation_form, document_relation_form_valid = get_document_relation_form(request, document)
    comment_form, comment_form_valid = get_comment_form(request, 'document', document.id)
    
    '''
    dd_relations = DocumentDocumentRelation.objects.filter(document=document).filter(published=True)| DocumentDocumentRelation.objects.filter(related_to=document).filter(published=True)
    
    for rel in dd_relations:
        if rel.related_to==document:
            tmp_doc = rel.document
            rel.document = rel.related_to
            rel.related_to = tmp_doc
    '''
    context = RequestContext(request, {
        'site_config': get_site_config(),
        'project': get_project(),
        'document': document,
        'publicdocs_doc': publicdocs_doc,
        'document_relation_form': document_relation_form,
        'document_relation_form_valid': document_relation_form_valid,
        'document_relation_list': DocumentRelation.objects.filter(document=document).filter(published=True),
        'comment_form': comment_form,
        'comment_form_valid': comment_form_valid,
        'comment_list': Comment.objects.filter(published=True, commented_object_type__name="document", commented_object_id=document_id),
        
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


#PublicDocs
def document_search(request):
    ''' The search view for handling the search using Django's "Q"-class (see normlize_query and get_query)'''
    query_string = ''
    found_pages = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        
        entry_query = get_query(query_string, ['document__title', 'content',])
        found_pages = PublicdocsPage.objects.select_related().filter(entry_query).order_by('document','number')
        
        document_list = []
        for page in found_pages:
            for pd_doc in page.document.all():
                docs = Document.objects.filter(title=pd_doc.title)
                if len(docs) > 0:
                    docs[0].found_page = page.number
                    document_list.append(docs[0])
                    print docs[0]
        
        context = RequestContext(request, {
            'site_config': get_site_config(),
            'project': get_project(),
            'query': query_string,
            'document_list': document_list,
        })
        
        return render_to_response('documents_search.html', context)
    else:
        return HttpResponse("An Error occured!")


def contact(request):
    cp, response = check_config_prerequisits()
    if not cp:
        return response
    
    image_list = Image.objects.all()
    
    context = {
        'site_config': get_site_config(),
        'project': get_project(),
        'image_list': image_list,
    }
    return render_to_response('contact.html', context)
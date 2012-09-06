# coding=UTF-8

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _
from big_projects_watch.forms import *
from big_projects_watch.models import *

try:
    from documents.models  import Document as PublicdocsDoc
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
    return SiteConfig.objects.all()[0]

def index(request):
    cp, response = check_config_prerequisits()
    if not cp:
        return response
    
    latest_event_list = Event.objects.all()[0:8]
    latest_web_source_list = WebSource.objects.all()[0:8]
    latest_document_list = Document.objects.all()[0:8]
    context = {
        'site_config': get_site_config(),
        'project': get_project(),
        'current_project_goal_group': ProjectGoalGroup.objects.get_current(),
        'project_part_list': ProjectPart.objects.all(),
        'latest_event_list': latest_event_list,
        'latest_web_source_list': latest_web_source_list,
        'latest_document_list': latest_document_list,
        'latest_document_project_part_relation_list': DocumentProjectPartRelation.objects.filter(published=True).order_by('-date_added')[0:2],
        'latest_document_participant_relation_list': DocumentParticipantRelation.objects.filter(published=True).order_by('-date_added')[0:2],
        'latest_document_event_relation_list': DocumentEventRelation.objects.filter(published=True).order_by('-date_added')[0:2],
        'latest_document_document_relation_list': DocumentDocumentRelation.objects.filter(published=True).order_by('-date_added')[0:2],
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
    }
    return render_to_response('project.html', context)


def project_part(request, project_part_id):
    cp, response = check_config_prerequisits()
    if not cp:
        return response
    
    project_part = get_object_or_404(ProjectPart, pk=project_part_id)

    context = {
        'site_config': get_site_config(),
        'project': get_project(),
        'project_part': project_part,
        'relation_list': DocumentProjectPartRelation.objects.filter(related_to=project_part).filter(published=True),
    }
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
    }
    return render_to_response('process.html', context)


def event(request, event_id):
    cp, response = check_config_prerequisits()
    if not cp:
        return response
    
    event = get_object_or_404(Event, pk=event_id)
    context = {
        'site_config': get_site_config(),
        'project': get_project(),
        'event': event,
        'relation_list': DocumentEventRelation.objects.filter(related_to=event).filter(published=True),
    }
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
    }
    return render_to_response('participants.html', context)


def participant(request, participant_id):
    cp, response = check_config_prerequisits()
    if not cp:
        return response
    
    participant = get_object_or_404(Participant, pk=participant_id)
    
    context = {
        'site_config': get_site_config(),
        'project': get_project(),
        'participant': participant,
        'relation_list': DocumentParticipantRelation.objects.filter(related_to=participant).filter(published=True),
    }
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
        'latest_document_project_part_relation_list': DocumentProjectPartRelation.objects.filter(published=True).order_by('-date_added')[0:4],
        'latest_document_participant_relation_list': DocumentParticipantRelation.objects.filter(published=True).order_by('-date_added')[0:4],
        'latest_document_event_relation_list': DocumentEventRelation.objects.filter(published=True).order_by('-date_added')[0:4],
        'latest_document_document_relation_list': DocumentDocumentRelation.objects.filter(published=True).order_by('-date_added')[0:4],
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
    
    document_project_part_relation_form = DocumentProjectPartRelationForm()
    document_participant_relation_form = DocumentParticipantRelationForm()
    document_event_relation_form = DocumentEventRelationForm()
    document_document_relation_form = DocumentDocumentRelationForm()
    
    dd_relations = DocumentDocumentRelation.objects.filter(document=document).filter(published=True)| DocumentDocumentRelation.objects.filter(related_to=document).filter(published=True)
    
    for rel in dd_relations:
        if rel.related_to==document:
            tmp_doc = rel.document
            rel.document = rel.related_to
            rel.related_to = tmp_doc
    
    context = RequestContext(request, {
        'site_config': get_site_config(),
        'project': get_project(),
        'document': document,
        'publicdocs_doc': publicdocs_doc,
        'document_project_part_relation_form': document_project_part_relation_form,
        'document_project_part_relation_list': DocumentProjectPartRelation.objects.filter(document=document).filter(published=True),
        'document_participant_relation_form': document_participant_relation_form,
        'document_participant_relation_list': DocumentParticipantRelation.objects.filter(document=document).filter(published=True),
        'document_event_relation_form': document_event_relation_form,
        'document_event_relation_list': DocumentEventRelation.objects.filter(document=document).filter(published=True),
        'document_document_relation_form': document_document_relation_form,
        'document_document_relation_list': dd_relations,
    })
    return render_to_response('document.html', context)


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
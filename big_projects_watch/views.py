# coding=UTF-8

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.utils.translation import ugettext as _
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


def get_site_config():
    return SiteConfig.objects.all()[0]

def index(request):
    cp, response = check_config_prerequisits()
    if not cp:
        return response
    
    latest_event_list = Event.objects.all()[0:5]
    latest_web_source_list = WebSource.objects.all()[0:5]
    latest_document_list = Document.objects.all()[0:5]
    context = {
        'site_config': get_site_config(),
        'project': get_project(),
        'current_project_goal_group': ProjectGoalGroup.objects.get_current(),
        'project_part_list': ProjectPart.objects.all(),
        'latest_event_list': latest_event_list,
        'latest_web_source_list': latest_web_source_list,
        'latest_document_list': latest_document_list,
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
    web_source_list = WebSource.objects.filter(event__project_parts__id=project_part_id)
    document_list = Document.objects.filter(event__project_parts__id=project_part_id)
    context = {
        'site_config': get_site_config(),
        'project': get_project(),
        'project_part': project_part,
        'web_source_list': web_source_list,
        'document_list': document_list,
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
    web_source_list = WebSource.objects.filter(event__participants__id=participant_id)
    document_list = Document.objects.filter(event__participants__id=participant_id)
    context = {
        'site_config': get_site_config(),
        'project': get_project(),
        'participant': participant,
        'web_source_list': web_source_list,
        'document_list': document_list,
    }
    return render_to_response('participant.html', context)


def information_sources(request):
    cp, response = check_config_prerequisits()
    if not cp:
        return response
    
    web_source_list = WebSource.objects.all().order_by('title')
    document_list = Document.objects.all().order_by('title')
    context = {
        'site_config': get_site_config(),
        'project': get_project(),
        'web_source_list': web_source_list,
        'document_list': document_list,
    }
    return render_to_response('information_sources.html', context)


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
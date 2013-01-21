from django.conf.urls.defaults import patterns, url
from django.utils.translation import ugettext as _


handler404 = 'big_projects_watch.views.custom_404_view'

urlpatterns = patterns('',
    url(r'^$', 'big_projects_watch.views.index'),
    url(r'^404test/$', 'big_projects_watch.views.custom_404_view'),
    url(r'^%s$' % _('project_url'), 'big_projects_watch.views.project'),
    url(r'^%s(?P<project_part_id>\d+)/$' % _('project_parts_url'), 'big_projects_watch.views.project_part'),
    url(r'^%s$' % _('questions_url'), 'big_projects_watch.views.questions'),
    url(r'^%s$' % _('process_url'), 'big_projects_watch.views.process'),
    url(r'^%s(?P<event_id>\d+)/$' % _('events_url'), 'big_projects_watch.views.event'),
    url(r'^%s$' % _('participants_url'), 'big_projects_watch.views.participants'),
    url(r'^%s(?P<participant_id>\d+)/$' % _('participants_url'), 'big_projects_watch.views.participant'),
    url(r'^%s$' % _('documents_url'), 'big_projects_watch.views.documents'),
    url(r'^%s(?P<document_id>\d+)/$' % _('documents_url'), 'big_projects_watch.views.document'),
    url(r'^%s$' %  _('search_url'), 'big_projects_watch.views.search'),
    url(r'^%s$' % _('contact_url'), 'big_projects_watch.views.contact'),
    url(r'^%s$' % _('activate_document_relation_url'), 'big_projects_watch.views.activate_document_relation'),
    url(r'^%s$' % _('activate_comment_url'), 'big_projects_watch.views.activate_comment'),
)
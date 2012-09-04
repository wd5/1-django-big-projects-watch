from django.conf.urls.defaults import patterns, include, url
from django.utils.translation import ugettext as _

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'big_projects_watch.views.index'),
    url(r'^%s/$' % _('project'), 'big_projects_watch.views.project'),
    url(r'^%s(?P<project_part_id>\d+)/$' % _('project_parts_url'), 'big_projects_watch.views.project_part'),
    url(r'^%s$' % _('process_url'), 'big_projects_watch.views.process'),
    url(r'^%s(?P<event_id>\d+)/$' % _('events_url'), 'big_projects_watch.views.event'),
    url(r'^%s$' % _('participants_url'), 'big_projects_watch.views.participants'),
    url(r'^%s(?P<participant_id>\d+)/$' % _('participants_url'), 'big_projects_watch.views.participant'),
    url(r'^%s$' % _('documents_url'), 'big_projects_watch.views.documents'),
    url(r'^%s(?P<document_id>\d+)/$' % _('documents_url'), 'big_projects_watch.views.document'),
    url(r'^%spublicdocs/(?P<slug>[-\w]+)/$' % _('documents_url'), 'big_projects_watch.views.publicdocs_doc'),
    url(r'^%s$' % _('contact_url'), 'big_projects_watch.views.contact'),
    url(r'^admin/', include(admin.site.urls)),
)
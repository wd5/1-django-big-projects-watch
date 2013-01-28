from big_projects_watch.models import *
from django.contrib import admin, messages
from django.contrib.admin.actions import delete_selected
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext as _


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profile'


class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )


class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image',)


class SiteConfigAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_color', 'sub_title', 'sub_title_color')


class WebSourceInline(generic.GenericTabularInline):
    model = WebSource


class ParticipantAdmin(admin.ModelAdmin):
    actions = ['delete_selected',]
    list_display = ('name', 'participant_type',)
    list_filter = ('participant_type',)
    search_fields = ['name', 'description',]
    inlines = [
        WebSourceInline,
    ]
    
    def delete_warning_msg(self, request, participant):
        msg  = _('The following associations with "%s" will be deleted') % unicode(participant)  + u': '
        msg += u'%i Events, ' % participant.related_events.count()
        msg += u'%i Documents' % participant.related_documents.count()
        messages.warning(request, msg)

    def delete_view(self, request, object_id, extra_context=None):
        self.delete_warning_msg(request, Participant.objects.get(pk=object_id))
        return super(ParticipantAdmin, self).delete_view(request, object_id, extra_context)
    
    def delete_selected(self, request, queryset):
        for object in queryset.all():
            self.delete_warning_msg(request, object)
        return delete_selected(self, request, queryset)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [
        WebSourceInline,
    ]


class ProjectPartAdmin(admin.ModelAdmin):
    actions = ['delete_selected',]
    list_display = ('name', 'order',)
    inlines = [
        WebSourceInline,
    ]

    def delete_warning_msg(self, request, project_part):
        msg  = _('The following associations with "%s" will be deleted') % unicode(project_part)  + u': '
        msg += u'%i Events, ' % project_part.related_events.count()
        msg += u'%i Documents' % project_part.related_documents.count()
        messages.warning(request, msg)

    def delete_view(self, request, object_id, extra_context=None):
        self.delete_warning_msg(request, ProjectPart.objects.get(pk=object_id))
        return super(ProjectPartAdmin, self).delete_view(request, object_id, extra_context)
    
    def delete_selected(self, request, queryset):
        for object in queryset.all():
            self.delete_warning_msg(request, object)
        return delete_selected(self, request, queryset)


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_type', 'important', 'date')
    filter_horizontal = ('project_parts', 'participants',)
    inlines = [
        WebSourceInline,
    ]
    list_filter = ('event_type', 'important',)
    search_fields = ['title', 'description',]


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    filter_horizontal = ('project_parts', 'participants', 'events',)


class ProjectGoalInline(admin.StackedInline):
    model = ProjectGoal


class ProjectGoalGroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'event')
    inlines = [
        ProjectGoalInline,
    ]


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'document', 'date',)
    search_fields = ['title', 'description',]
    filter_horizontal = ('participants', 'project_parts', 'events',)
    exclude = ('pdf_images_generated',)


class PageAdmin(admin.ModelAdmin):
    list_display = ('document', 'number')


class DocumentRelationAdmin(admin.ModelAdmin):
    list_display = ('document', 'content_object', 'content_type', 'relation_type', 'published', 'published_by', 'page', 'date_added')
    list_filter = ('content_type', 'published', 'published_by',)
    search_fields = ['description',]
    exclude = ('activation_hash',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('content_object', 'content_type', 'published', 'published_by', 'username', 'date_added')
    list_filter = ('content_type', 'published','published_by',)
    search_fields = ['username', 'comment',]
    exclude = ('activation_hash',)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(SiteConfig, SiteConfigAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectPart, ProjectPartAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(ProjectGoalGroup, ProjectGoalGroupAdmin)
admin.site.register(Document, DocumentAdmin)
#admin.site.register(Page, PageAdmin)
admin.site.register(DocumentRelation, DocumentRelationAdmin)
admin.site.register(Comment, CommentAdmin)

from big_projects_watch.models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


def shorten_url(url):
    max_length = 35
    return (url[:max_length] + '..') if len(url) > max_length else url


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


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'url_', 'info_url_')
    list_filter = ('participant_type',)
    search_fields = ['name', 'description',]
    
    def url_(self, instance):
        return '<a href="%s" target="_blank">%s</a>' % (instance.url, shorten_url(instance.url))
    url_.allow_tags = True
    
    def info_url_(self, instance):
        return '<a href="%s" target="_blank">%s</a>' % (instance.info_url, shorten_url(instance.info_url))
    info_url_.allow_tags = True


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'url_', 'info_url_')
    
    def url_(self, instance):
        return '<a href="%s" target="_blank">%s</a>' % (instance.url, shorten_url(instance.url))
    url_.allow_tags = True
    
    def info_url_(self, instance):
        return '<a href="%s" target="_blank">%s</a>' % (instance.info_url, shorten_url(instance.info_url))
    info_url_.allow_tags = True


class ProjectPartAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'url_')
    
    def url_(self, instance):
        return '<a href="%s" target="_blank">%s</a>' % (instance.url, shorten_url(instance.url))
    url_.allow_tags = True


class WebSourceInline(admin.TabularInline):
    model = WebSource


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_type', 'important', 'date')
    filter_horizontal = ('participants', 'project_parts',)
    inlines = [
        WebSourceInline,
    ]
    list_filter = ('event_type', 'important',)
    search_fields = ['title', 'description',]


class ProjectGoalInline(admin.StackedInline):
    model = ProjectGoal


class ProjectGoalGroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'event')
    inlines = [
        ProjectGoalInline,
    ]


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'document', 'author', 'date',)
    search_fields = ['title', 'description',]


class PageAdmin(admin.ModelAdmin):
    list_display = ('document', 'number')


class DocumentRelationAdmin(admin.ModelAdmin):
    list_display = ('document', 'related_to', 'related_to_type', 'published', 'page', 'date_added')
    list_filter = ('related_to_type', 'published',)
    search_fields = ['description',]
    exclude = ('activation_hash',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('commented_object', 'commented_object_type', 'published', 'username', 'date_added')
    list_filter = ('commented_object_type', 'published',)
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
admin.site.register(ProjectGoalGroup, ProjectGoalGroupAdmin)
admin.site.register(Document, DocumentAdmin)
#admin.site.register(Page, PageAdmin)
admin.site.register(DocumentRelation, DocumentRelationAdmin)
admin.site.register(Comment, CommentAdmin)

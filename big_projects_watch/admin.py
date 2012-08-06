from big_projects_watch.models import *
from django.contrib import admin


class ImageAdmin(admin.ModelAdmin):
    list_display = ('title',)


class SiteConfigAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_color', 'sub_title', 'sub_title_color')


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'info_url')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'info_url')


class ProjectPartAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')


class WebSourceInline(admin.TabularInline):
    model = WebSource


class DocumentInline(admin.TabularInline):
    model = Document


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_type', 'important', 'date')
    filter_horizontal = ('participants', 'project_parts',)
    inlines = [
        WebSourceInline, DocumentInline,
    ]


class ProjectGoalInline(admin.StackedInline):
    model = ProjectGoal


class ProjectGoalGroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'event')
    inlines = [
        ProjectGoalInline,
    ]


admin.site.register(Image, ImageAdmin)
admin.site.register(SiteConfig, SiteConfigAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectPart, ProjectPartAdmin)
admin.site.register(ProjectGoalGroup, ProjectGoalGroupAdmin)
admin.site.register(Event, EventAdmin)
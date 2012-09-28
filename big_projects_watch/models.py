# coding=UTF-8
import os
import shutil
from datetime import datetime

from django.db.models.signals import post_save, pre_delete
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db import models
from django.utils.encoding import smart_unicode 
from django.utils.translation import ugettext, ugettext_lazy as _
from big_projects_watch.doc_scanner import DocScanner



class UserProfile(models.Model):
    user = models.OneToOneField(User)
    receive_new_document_relation_emails = models.BooleanField(default=True)
    receive_new_comment_emails = models.BooleanField(default=True)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)


class Image(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images')
    help_text = _("Short linked html attribution snippet to the original image source or \
alternatively something like 'Own image'.")
    attribution_html = models.CharField(max_length=250, help_text=help_text)
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ['title',]


class SiteConfig(models.Model):
    help_text = _("Main title, shown in the header navi.")
    default = _("Project Website Title")
    title = models.CharField(max_length=250, help_text=help_text, default=default)
    help_text = _("Color for the page title (Format: '#990000').")
    title_color = models.CharField(max_length=7, help_text=help_text, default='#990000')
    help_text = _("Subtitle of the page.")
    default = _("Project Website Subtitle")
    sub_title = models.CharField(max_length=250, help_text=help_text, default=default)
    help_text = _("Color for the page subtitle (Format: '#990000').")
    sub_title_color = models.CharField(max_length=7, help_text=help_text, default='#444444')
    help_text = _("Short intro text to describe your page, not too long, use about text for detailed information.")
    default = _("This is a project watch website.")
    intro_text = models.TextField(help_text=help_text, default=default)
    help_text = _("Optional header image shown at the end of intro box on first page (Width: 450px \
Height: your choice, something around 175px is a good fit).")
    header_image = models.ForeignKey(Image, help_text=help_text, blank=True, null=True)
    help_text = _("Background color for the header (Format: '#990000').")
    header_bg_color = models.CharField(max_length=7, help_text=help_text, default='#EEEEEE')
    help_text = _("Color of the navi links (Format: '#990000').")
    navi_link_color = models.CharField(max_length=7, help_text=help_text, default='#FFFFFF')
    help_text = _("Background color for the navigation (Format: '#990000').")
    navi_bg_color = models.CharField(max_length=7, help_text=help_text, default='#333333')
    help_text = _("Background color to mark important elements on various parts of the site, \
font color will be white, so use something slightly darker.")
    important_bg_color = models.CharField(max_length=7, help_text=help_text, default='#990000')
    help_text = _("Short intro text about this site, what is the purpose, who is running it.")
    desc_about = models.TextField(help_text=help_text)
    help_text = _("Some html text you want to use in the footer of the page, you can e.g. \
provide a link to your email adress or associated social media sites.")
    footer_html = models.TextField(help_text=help_text, default=_("Footer HTML Default"))
    help_text = _("Html to be displayed on the contact page, provide at least an adress there \
and some contact information.")
    contact_html = models.TextField(help_text=help_text, default=_("Contact HTML Default"))
    comments = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.title


class WebSource(models.Model):
    title = models.CharField(max_length=250)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey("content_type", "object_id")
    order = models.IntegerField(blank=True, null=True)
    url = models.URLField()
    date = models.DateField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ['order', '-date_added']


class Participant(models.Model):
    PARTICIPANT_TYPE_CHOICES = (
        ('AD', _('Administration')),
        ('PO', _('Politics / Party / Parliament')),
        ('CI', _('Citizens')),
        ('CO', _('Company')),
        ('SE', _('Miscellaneous')),
    )
    PARTICIPANT_TYPE_CHOICES_ICONS = {
        'AD': 'icon-group',
        'PO': 'icon-group',
        'CI': 'icon-group',
        'CO': 'icon-group',
        'SE': 'icon-group',
    }
    help_text  = _("Person, group or institution acting in some way in the context of the project or being affected by the process or the result of the project execution.")
    name = models.CharField(max_length=250, help_text=help_text)
    participant_type = models.CharField(max_length=2, choices=PARTICIPANT_TYPE_CHOICES)
    help_text = _("Role/tasks as well as interests/goals of the participant regarding the project.")
    description = models.TextField(help_text=help_text)
    web_sources = generic.GenericRelation(WebSource)
    comments = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return "/" + ugettext("participants_url") + unicode(self.id) + "/"
    
    def get_participant_type_icon(self):
        return self.PARTICIPANT_TYPE_CHOICES_ICONS[self.participant_type]
    
    class Meta:
        ordering = ['name',]


class Project(models.Model):
    help_text = _("Name of the project.")
    name = models.CharField(max_length=250, help_text=help_text)
    responsible_participants = models.ManyToManyField(Participant, related_name="responsible_for_project")
    help_text = _("General description of the project, what is it about, what is being done?")
    desc_project = models.TextField(help_text=help_text)
    help_text = _("What are the important parts of the project?")
    desc_project_parts = models.TextField(help_text=help_text)
    help_text = _("Who has initiated the project, what societal groups are involved?")
    desc_participants = models.TextField(help_text=help_text)
    help_text = _("What goals does the project target, what conditions should be met?")
    desc_goal_groups = models.TextField(help_text=help_text)
    help_text = _("What is the general process of the project development?")
    desc_process = models.TextField(help_text=help_text)
    help_text = _("What project documents are collected/provided?")
    desc_documents = models.TextField(help_text=help_text)
    web_sources = generic.GenericRelation(WebSource)
    comments = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name    


class ProjectPart(models.Model):
    help_text = _("Structural parts of the project being stable over time.")
    name = models.CharField(max_length=250, help_text=help_text)
    help_text = _("Use integer numbers for ordering (e.g. '100', '200', '300').")
    order = models.IntegerField(help_text=help_text, blank=True, null=True)
    help_text = _("Website (if existant).")
    description = models.TextField(help_text=help_text)
    web_sources = generic.GenericRelation(WebSource)
    comments = models.TextField(blank=True)

    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return "/" + ugettext("project_parts_url") + unicode(self.id) + "/"
    
    class Meta:
        ordering = ['name',]


class Event(models.Model):
    EVENT_TYPE_CHOICES = (
        ('ME', _('Meeting / Gathering / Session')),
        ('IN', _('New Information / Decision / Statement')),
        ('MI', _('Project Progress / Execution / Milestone')),
        ('CI', _('Action by Civil Society')),
        ('UE', _('Unplanned Event')),
        ('SE', _('Miscellaneous')),
    )
    EVENT_TYPE_CHOICES_ICONS = {
        'ME': 'icon-calendar',
        'IN': 'icon-info-sign',
        'MI': 'icon-wrench',
        'CI': 'icon-bullhorn',
        'UE': 'icon-bolt',
        'SE': 'icon-asterisk',
    }
    title = models.CharField(max_length=250)
    event_type = models.CharField(max_length=2, choices=EVENT_TYPE_CHOICES)
    help_text = _("Event being of central importance for the project.")
    important = models.BooleanField(help_text=help_text)
    description = models.TextField()
    date = models.DateField()
    participants = models.ManyToManyField(Participant, related_name="related_events", blank=True, null=True)
    project_parts = models.ManyToManyField(ProjectPart, related_name="related_events", blank=True, null=True)
    web_sources = generic.GenericRelation(WebSource)
    comments = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.title + ", " + datetime.strftime(self.date, '%d.%m.%Y') 
    
    def get_absolute_url(self):
        return "/" + ugettext("events_url") + unicode(self.id) + "/"
    
    def get_event_type_icon(self):
        return self.EVENT_TYPE_CHOICES_ICONS[self.event_type]
    
    def as_list(self):
        return [self,]
    
    class Meta:
        ordering = ['-date']


class ProjectGoalGroupManager(models.Manager):
    
    def get_current(self):
        return self.all().order_by('event')[0]
        

class ProjectGoalGroup(models.Model):
    help_text = _("Group of project goals being determined at a certain point in time.")
    title = models.CharField(max_length=250, help_text=help_text)
    event = models.ForeignKey(Event)
    help_text = _("Description of the group of project goals.")
    description = models.TextField(help_text=help_text)
    comments = models.TextField(blank=True)
    objects = ProjectGoalGroupManager()
    
    def __unicode__(self):
        return self.title

    def is_current(self):
        return self == ProjectGoalGroup.objects.get_current()


class ProjectGoal(models.Model):
    help_text = _("Name, e.g. 'Project budget', 'Target date', 'Noise level'")
    name = models.CharField(max_length=250, help_text=help_text)
    project_goal_group = models.ForeignKey(ProjectGoalGroup)
    help_text = _("Single performance figure describing the project goal, e.g. '1.000.000 Euro', 'January 25th 2020', ...")
    performance_figure = models.CharField(max_length=250, help_text=help_text)
    help_text = _("Use integer numbers for ordering (e.g. '100', '200', '300').")
    order = models.IntegerField(help_text=help_text, blank=True, null=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['order',]


class Document(models.Model):
    help_text = _("Unique and descriptive title (if PublicDocs is used: PDF live view is shown, if document title is the same)")
    title = models.CharField(max_length=250, help_text=help_text)
    document = models.FileField(upload_to='documents')
    author = models.ForeignKey(Participant, blank=True, null=True)
    date = models.DateField()
    help_text = _("Short description.")
    description = models.TextField(help_text=help_text)
    comments = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.title + " (" + datetime.strftime(self.date, '%d.%m.%Y') + ")"
    
    def get_absolute_url(self):
        return "/" + ugettext("documents_url") + unicode(self.id) + "/"
    
    def get_document_name(self):
        return os.path.basename(self.document.name)
    
    def get_pages_path(self):
        return os.path.join(settings.MEDIA_ROOT, 'documents/document_' + unicode(self.id) + '/')
    
    class Meta:
        ordering = ['-date_added']
    
    def __init__(self, *args, **kwargs):
        super(Document, self).__init__(*args, **kwargs)
        self.old_document = self.document

    def save(self, force_insert=False, force_update=False):
        super(Document, self).save(force_insert, force_update)

        # Delete old document
        if self.old_document and self.old_document != self.document:
            if os.path.exists(self.old_document.path):
                os.remove(self.old_document.path)

        # Saving pages when WITH_PUBLIC_DOCS=True in settings.py
        if getattr(settings, 'WITH_PUBLIC_DOCS', False) and self.old_document != self.document:
            self.page_set.all().delete()
            ds = DocScanner(self)
            doc_pages = ds.get_doc_pages()
            
            i = 1
            for doc_page in doc_pages:
                page = Page(
                    document=self,
                    number=i,
                    content = smart_unicode(doc_page, encoding='utf-8', strings_only=False, errors='strict'),
                )
                page.save()
                i = i + 1
        
        self.old_document = self.document

def delete_pages_folder(sender, **kwargs):
    instance = kwargs['instance']
    if os.path.exists(instance.get_pages_path()):
        shutil.rmtree(instance.get_pages_path())

def delete_document_file(sender, **kwargs):
    instance = kwargs['instance']
    if instance.document and os.path.exists(instance.document.path):
                os.remove(instance.document.path)

pre_delete.connect(delete_pages_folder, sender=Document)
pre_delete.connect(delete_document_file, sender=Document)


class Page(models.Model):
    document = models.ForeignKey(Document)
    number = models.IntegerField()
    content = models.TextField(blank=True)
    
    def get_filename(self):
        return u'page-' + unicode(self.number) + u'.jpg'
    
    def get_filepath(self):
        return self.document.get_pages_path() + self.get_filename()
    
    def __unicode__(self):
        return unicode(self.document) + ", Page " + unicode(self.number)
    
    class Meta:
        ordering = ['number']


def delete_page_image(sender, **kwargs):
    instance = kwargs['instance']
    if os.path.exists(instance.get_filepath()):
        os.remove(instance.get_filepath())

pre_delete.connect(delete_page_image, sender=Page)


class DocumentRelation(models.Model):
    help_text = _('The document having the relation.')
    document = models.ForeignKey(Document, help_text=help_text, related_name='+')
    help_text = _('Type of the related element (ProjectPart, Participant, Event, Document).')
    limit = models.Q(app_label = 'big_projects_watch', model = 'projectpart') | \
            models.Q(app_label = 'big_projects_watch', model = 'participant') | \
            models.Q(app_label = 'big_projects_watch', model = 'event') | \
            models.Q(app_label = 'big_projects_watch', model = 'document')
    related_to_type = models.ForeignKey(ContentType, help_text=help_text, limit_choices_to=limit)
    help_text = _('The id of the related element (you can find the id of an object in the url \
of the object change form in the admin).')
    related_to_id = models.PositiveIntegerField(help_text=help_text)
    related_to = generic.GenericForeignKey('related_to_type', 'related_to_id')
    help_text = _('Relation is only shown on page if published is true.')
    published = models.BooleanField(default=False, help_text=help_text)
    help_text = _("Short description.")
    description = models.TextField(help_text=help_text)
    help_text = _("Page number in document (only the number, e.g. '5', '126', please take \
the page number from pdf viewer if different from page number inside the document), or empty \
if referring to the whole document.")
    page = models.IntegerField(blank=True, null=True, help_text=help_text)
    comments = models.TextField(blank=True)
    activation_hash = models.CharField(max_length=250, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return unicode(self.document) + " -> " + unicode(self.related_to)
    
    class Meta:
        ordering = ['-date_added']


class Comment(models.Model):
    help_text = _('Type of the commented object (ProjectPart, Participant, Event, Document).')
    limit = models.Q(app_label = 'big_projects_watch', model = 'projectpart') | \
            models.Q(app_label = 'big_projects_watch', model = 'participant') | \
            models.Q(app_label = 'big_projects_watch', model = 'event') | \
            models.Q(app_label = 'big_projects_watch', model = 'document')
    commented_object_type = models.ForeignKey(ContentType, help_text=help_text, limit_choices_to=limit)
    help_text = _('The id of the commented object (you can find the id of an object in the url \
of the object change form in the admin).')
    commented_object_id = models.PositiveIntegerField(help_text=help_text)
    commented_object = generic.GenericForeignKey('commented_object_type', 'commented_object_id')
    help_text = _('Comment is only shown on page if published is true.')
    published = models.BooleanField(default=False, help_text=help_text)
    username = models.CharField(max_length=250, help_text=help_text)
    comment = models.TextField()
    help_text = _("Page number in document (only the number, e.g. '5', '126', please take \
the page number from pdf viewer if different from page number inside the document), or empty \
if referring to the whole document.")
    page = models.IntegerField(blank=True, null=True, help_text=help_text)
    activation_hash = models.CharField(max_length=250, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.username + ", " + unicode(self.commented_object) + " (" + datetime.strftime(self.date_added, '%d.%m.%Y') + ")"
    
    class Meta:
        ordering = ['-date_added']
    


# coding=UTF-8
import os

from django.db import models 
from django.utils.translation import ugettext, ugettext_lazy as _



class Image(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='bpw/images')
    help_text = _("Short linked html attribution snippet to the original image source or \
alternatively something like 'Own image'.")
    attribution_html = models.CharField(max_length=250, help_text = help_text)
    
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


class Participant(models.Model):
    PARTICIPANT_TYPE_CHOICES = (
        ('AD', _('Administration')),
        ('PO', _('Politics/Party/Parliament')),
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
    help_text = _("Website of the participant.")
    url = models.URLField(help_text=help_text)
    help_text = _("Background information about the participant (e.g. Wikipedia).")
    info_url = models.URLField(blank=True, help_text=help_text)
    help_text = _("Role/tasks as well as interests/goals of the participant regarding the project.")
    description = models.TextField(help_text=help_text)
    comments = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return "/" + ugettext("participants_url") + str(self.id) + "/"
    
    def get_participant_type_icon(self):
        return self.PARTICIPANT_TYPE_CHOICES_ICONS[self.participant_type]
    
    class Meta:
        ordering = ['name',]


class Project(models.Model):
    help_text = _("Name of the project.")
    name = models.CharField(max_length=250, help_text=help_text)
    help_text = _("Website of the project.")
    url = models.URLField(help_text=help_text)
    help_text = _("Background information about the project (e.g. Wikipedia).")
    info_url = models.URLField(blank=True, help_text=help_text)
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
    comments = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name    


class ProjectPart(models.Model):
    help_text = _("Structural parts of the project being stable over time.")
    name = models.CharField(max_length=250, help_text=help_text)
    help_text = _("Website (if existant).")
    url = models.URLField(help_text=help_text, blank=True)
    help_text = _("Short description.")
    description = models.TextField(help_text=help_text)
    comments = models.TextField(blank=True)

    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return "/" + ugettext("project_parts_url") + str(self.id) + "/"
    
    class Meta:
        ordering = ['name',]


class Event(models.Model):
    EVENT_TYPE_CHOICES = (
        ('ME', _('Meeting/Gathering/Session')),
        ('IN', _('New Information/Decision/Statement')),
        ('MI', _('Project Progress/Execution/Milestone')),
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
    comments = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/" + ugettext("events_url") + str(self.id) + "/"
    
    def get_event_type_icon(self):
        return self.EVENT_TYPE_CHOICES_ICONS[self.event_type]
    
    def as_list(self):
        return [self,]
    
    class Meta:
        ordering = ['-date']


class WebSource(models.Model):
    title = models.CharField(max_length=250)
    event = models.ForeignKey(Event, blank=True, null=True)
    url = models.URLField()
    date = models.DateField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ['-date_added']



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
    
    def __unicode__(self):
        return self.name


class Document(models.Model):
    help_text = _("Unique and descriptive title (if PublicDocs is used: PDF live view is shown, if document title is the same)")
    title = models.CharField(max_length=250, help_text=help_text)
    document = models.FileField(upload_to='bpw/documents')
    date = models.DateField()
    help_text = _("Short description.")
    description = models.TextField(help_text=help_text)
    comments = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/" + ugettext("documents_url") + str(self.id) + "/"
    
    def get_document_name(self):
        return os.path.basename(self.document.name)
    
    class Meta:
        ordering = ['-date_added']


class DocumentProjectPartRelation(models.Model):
    RELATION_TYPE_CHOICES = (
        ('CD', _('Content description')),
        ('SE', _('Scheduling')),
        ('SP', _('Structural planning')),
        ('LA', _('Legal aspects')),
        ('MI', _('Miscellaneous')),
    )
    help_text = _('The document having the relation.')
    document = models.ForeignKey(Document, help_text=help_text, related_name='+')
    help_text = _('The related element.')
    related_to = models.ForeignKey(ProjectPart, help_text=help_text, related_name='+')
    help_text = _('Relation is only shown on page if published is true.')
    published = models.BooleanField(default=False, help_text=help_text)
    help_text = _('Type to specify the relation.')
    relation_type = models.CharField(max_length=2, choices=RELATION_TYPE_CHOICES, help_text=help_text)
    help_text = _("Short description.")
    description = models.TextField(help_text=help_text)
    help_text = _("Page or passage in the document where the relation was found \
(e.g. 'Page 5', 'Pages 7-12', 'Page 47, Paragraph 2').")
    passage_in_document = models.CharField(max_length=250, help_text=help_text)
    help_text = _("Page number in document where passage about relation starts \
(only the number, e.g. '5', '126') (only used if PublicDocs is used for live pdf view, \
if page number of document and of pdf viewer differ, use pdf viewer page number here).")
    passage_start_page = models.IntegerField(blank=True, null=True, help_text=help_text)
    comments = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


class DocumentParticipantRelation(models.Model):
    RELATION_TYPE_CHOICES = (
        ('PA', _('Publisher/Author')),
        ('RE', _('Recipient')),
        ('ME', _('Mention')),
        ('MI', _('Miscellaneous')),
    )
    help_text = _('The document having the relation.')
    document = models.ForeignKey(Document, help_text=help_text, related_name='+')
    help_text = _('The related element.')
    related_to = models.ForeignKey(Participant, help_text=help_text, related_name='+')
    help_text = _('Relation is only shown on page if published is true.')
    published = models.BooleanField(default=False, help_text=help_text)
    help_text = _('Type to specify the relation.')
    relation_type = models.CharField(max_length=2, choices=RELATION_TYPE_CHOICES, help_text=help_text)
    help_text = _("Short description.")
    description = models.TextField(help_text=help_text)
    help_text = _("Page or passage in the document where the relation was found \
(e.g. 'Page 5', 'Pages 7-12', 'Page 47, Paragraph 2').")
    passage_in_document = models.CharField(max_length=250, help_text=help_text)
    help_text = _("Page number in document where passage about relation starts \
(only the number, e.g. '5', '126') (only used if PublicDocs is used for live pdf view, \
if page number of document and of pdf viewer differ, use pdf viewer page number here).")
    passage_start_page = models.IntegerField(blank=True, null=True, help_text=help_text)
    comments = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


class DocumentEventRelation(models.Model):
    RELATION_TYPE_CHOICES = (
        ('RE', _('Result')),
        ('EP', _('Event planning')),
        ('PR', _('Event description')),
        ('ME', _('Mention')),
        ('MI', _('Miscellaneous')),
    )
    help_text = _('The document having the relation.')
    document = models.ForeignKey(Document, help_text=help_text, related_name='+')
    help_text = _('The related element.')
    related_to = models.ForeignKey(Event, help_text=help_text, related_name='+')
    help_text = _('Relation is only shown on page if published is true.')
    published = models.BooleanField(default=False, help_text=help_text)
    help_text = _('Type to specify the relation.')
    relation_type = models.CharField(max_length=2, choices=RELATION_TYPE_CHOICES, help_text=help_text)
    help_text = _("Short description.")
    description = models.TextField(help_text=help_text)
    help_text = _("Page or passage in the document where the relation was found \
(e.g. 'Page 5', 'Pages 7-12', 'Page 47, Paragraph 2').")
    passage_in_document = models.CharField(max_length=250, help_text=help_text)
    help_text = _("Page number in document where passage about relation starts \
(only the number, e.g. '5', '126') (only used if PublicDocs is used for live pdf view, \
if page number of document and of pdf viewer differ, use pdf viewer page number here).")
    passage_start_page = models.IntegerField(blank=True, null=True, help_text=help_text)
    comments = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


class DocumentDocumentRelation(models.Model):
    RELATION_TYPE_CHOICES = (
        ('SU', _('Supplement')),
        ('CO', _('Contradiction')),
        ('VE', _('Version')),
        ('ME', _('Mention')),
        ('MI', _('Miscellaneous')),
    )
    help_text = _('The document having the relation.')
    document = models.ForeignKey(Document, help_text=help_text, related_name='+')
    help_text = _('The related element.')
    related_to = models.ForeignKey(Document, help_text=help_text, related_name='+')
    help_text = _('Relation is only shown on page if published is true.')
    published = models.BooleanField(default=False, help_text=help_text)
    help_text = _('Type to specify the relation.')
    relation_type = models.CharField(max_length=2, choices=RELATION_TYPE_CHOICES, help_text=help_text)
    help_text = _("Short description.")
    description = models.TextField(help_text=help_text)
    help_text = _("Page or passage in the document where the relation was found \
(e.g. 'Page 5', 'Pages 7-12', 'Page 47, Paragraph 2').")
    passage_in_document = models.CharField(max_length=250, help_text=help_text)
    help_text = _("Page number in document where passage about relation starts \
(only the number, e.g. '5', '126') (only used if PublicDocs is used for live pdf view, \
if page number of document and of pdf viewer differ, use pdf viewer page number here).")
    passage_start_page = models.IntegerField(blank=True, null=True, help_text=help_text)
    comments = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

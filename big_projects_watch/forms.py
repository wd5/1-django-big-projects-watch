from django import forms
from django.utils.translation import ugettext_lazy as _

from big_projects_watch.models import ProjectPart, Participant, Event, Document


class DocumentRelationForm(forms.Form):
    RELATED_TO_TYPE_CHOICES = (
        ('projectpart', 'Projektbereich'),
        ('participant', 'Beteiligter'),
        ('event', 'Ereignis'),
        ('document', 'Dokument'),
    )
    document_id = forms.IntegerField(widget=forms.HiddenInput)
    help_text = _("Relation to object type, object")
    related_to_type = forms.ChoiceField(choices=RELATED_TO_TYPE_CHOICES, help_text=help_text)
    
    related_to_id = forms.ModelChoiceField(queryset=Event.objects.all())
    related_to_id_projectpart = forms.ModelChoiceField(queryset=ProjectPart.objects.all())
    related_to_id_participant = forms.ModelChoiceField(queryset=Participant.objects.all())
    related_to_id_event = forms.ModelChoiceField(queryset=Event.objects.all())
    related_to_id_document = forms.ModelChoiceField(queryset=Document.objects.all())
    
    help_text = _("Description of the relation (displayed on page)")
    description = forms.CharField(widget=forms.Textarea(attrs={'style':'width:500px;height:60px;'}), \
                    max_length=450, help_text=help_text)
    help_text = _("Page number in document (only the number, e.g. '5', '126', please take \
the page number from pdf viewer if different from page number inside the document), or empty \
if referring to the whole document.")
    # Using page_number instead of page here due to a strange form bug (initial display of a number)
    # which couldn't been localized
    page_number = forms.IntegerField(help_text=help_text, required=False)
    help_text = _("Additional comment (not publicly displayed)")
    comments = forms.CharField(widget=forms.Textarea(attrs={'style':'width:500px;height:60px;'}), \
                    max_length=450, required=False, help_text=help_text)


class CommentForm(forms.Form):
    RELATED_TO_TYPE_CHOICES = (
        ('project_part', 'Projektbereich'),
        ('participant', 'Beteiligter'),
        ('event', 'Ereignis'),
        ('document', 'Dokument'),
    )
    commented_object_type = forms.CharField(widget=forms.HiddenInput)
    commented_object_id = forms.IntegerField(widget=forms.HiddenInput)
    
    help_text = _("Name")
    username = forms.CharField(widget=forms.TextInput(attrs={'style':'width:200px;'}), \
                            max_length=50, help_text=help_text)
    help_text = _("Comment")
    comment = forms.CharField(widget=forms.Textarea(attrs={'style':'width:500px;height:120px;'}), \
                    max_length=450, help_text=help_text)
    help_text = _("Page number in document (only the number, e.g. '5', '126', please take \
the page number from pdf viewer if different from page number inside the document), or empty \
if referring to the whole document.")
    # Using page_number instead of page here due to a strange form bug (initial display of a number)
    # which couldn't been localized
    page_number = forms.IntegerField(help_text=help_text, required=False)
    
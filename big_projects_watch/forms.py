from django import forms
from django.utils.translation import ugettext_lazy as _

from big_projects_watch.models import ProjectPart, Participant, Event, Document


class DocumentRelationForm(forms.Form):
    RELATED_TO_TYPE_CHOICES = (
        ('project part', 'Projektbereich'),
        ('participant', 'Beteiligter'),
        ('event', 'Ereignis'),
        ('document', 'Dokument'),
    )
    help_text = _("Relation to object type, object")
    related_to_type = forms.ChoiceField(choices=RELATED_TO_TYPE_CHOICES)
    
    related_to_id = forms.ModelChoiceField(queryset=Event.objects.all())
    related_to_project_part_id = forms.ModelChoiceField(queryset=ProjectPart.objects.all())
    related_to_participant_id = forms.ModelChoiceField(queryset=Participant.objects.all())
    related_to_event_id = forms.ModelChoiceField(queryset=Event.objects.all())
    related_to_document_id = forms.ModelChoiceField(queryset=Document.objects.all())
    
    help_text = _("Description of the relation (displayed on page)")
    description = forms.CharField(widget=forms.Textarea(attrs={'style':'width:500px;height:60px;'}), \
                    max_length=450, help_text=help_text)
    help_text = _("Page or passage in the document (e.g. 'Page 5', 'Pages 7-12', 'Page 47, Paragraph 2').")
    passage_in_document = forms.CharField(widget=forms.TextInput(attrs={'style':'width:200px;'}), \
                            max_length=50, help_text=help_text)
    help_text = _("Additional comment (not publicly displayed)")
    comments = forms.CharField(widget=forms.Textarea(attrs={'style':'width:500px;height:60px;'}), \
                    max_length=450, required=False, help_text=help_text)
    
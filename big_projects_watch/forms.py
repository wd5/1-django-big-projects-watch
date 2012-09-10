from django.forms import ModelForm
from django import forms

from big_projects_watch.models import DocumentRelation


class DocumentRelationForm(ModelForm):
    
    sender = forms.EmailField(label="Dadidada", help_text="You're lost!")
    
    class Meta:
        model = DocumentRelation
        fields = ['sender', 'description', 'comments',]

from django.forms import ModelForm
from django import forms

from big_projects_watch.models import DocumentProjectPartRelation, DocumentParticipantRelation
from big_projects_watch.models import DocumentEventRelation, DocumentDocumentRelation


class DocumentProjectPartRelationForm(ModelForm):
    
    class Meta:
        model = DocumentProjectPartRelation
        fields = ['related_to', 'description', 'comments',]


class DocumentParticipantRelationForm(ModelForm):
    
    class Meta:
        model = DocumentParticipantRelation
        fields = ['related_to', 'description', 'comments',]


class DocumentEventRelationForm(ModelForm):
    
    class Meta:
        model = DocumentEventRelation
        fields = ['related_to', 'description', 'comments',]


class DocumentDocumentRelationForm(ModelForm):
    
    class Meta:
        model = DocumentDocumentRelation
        fields = ['related_to', 'description', 'comments',]
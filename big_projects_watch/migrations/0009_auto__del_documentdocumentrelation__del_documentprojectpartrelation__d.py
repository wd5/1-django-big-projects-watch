# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'DocumentDocumentRelation'
        db.delete_table('big_projects_watch_documentdocumentrelation')

        # Deleting model 'DocumentProjectPartRelation'
        db.delete_table('big_projects_watch_documentprojectpartrelation')

        # Deleting model 'DocumentEventRelation'
        db.delete_table('big_projects_watch_documenteventrelation')

        # Deleting model 'DocumentParticipantRelation'
        db.delete_table('big_projects_watch_documentparticipantrelation')

        # Adding model 'DocumentRelation'
        db.create_table('big_projects_watch_documentrelation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('document', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['big_projects_watch.Document'])),
            ('related_to_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('related_to_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('passage_in_document', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('passage_start_page', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('big_projects_watch', ['DocumentRelation'])


    def backwards(self, orm):
        # Adding model 'DocumentDocumentRelation'
        db.create_table('big_projects_watch_documentdocumentrelation', (
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('passage_start_page', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('related_to', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['big_projects_watch.Document'])),
            ('relation_type', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('passage_in_document', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('document', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['big_projects_watch.Document'])),
        ))
        db.send_create_signal('big_projects_watch', ['DocumentDocumentRelation'])

        # Adding model 'DocumentProjectPartRelation'
        db.create_table('big_projects_watch_documentprojectpartrelation', (
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('passage_start_page', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('related_to', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['big_projects_watch.ProjectPart'])),
            ('relation_type', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('passage_in_document', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('document', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['big_projects_watch.Document'])),
        ))
        db.send_create_signal('big_projects_watch', ['DocumentProjectPartRelation'])

        # Adding model 'DocumentEventRelation'
        db.create_table('big_projects_watch_documenteventrelation', (
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('passage_start_page', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('related_to', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['big_projects_watch.Event'])),
            ('relation_type', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('passage_in_document', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('document', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['big_projects_watch.Document'])),
        ))
        db.send_create_signal('big_projects_watch', ['DocumentEventRelation'])

        # Adding model 'DocumentParticipantRelation'
        db.create_table('big_projects_watch_documentparticipantrelation', (
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('passage_start_page', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('related_to', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['big_projects_watch.Participant'])),
            ('relation_type', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('passage_in_document', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('document', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['big_projects_watch.Document'])),
        ))
        db.send_create_signal('big_projects_watch', ['DocumentParticipantRelation'])

        # Deleting model 'DocumentRelation'
        db.delete_table('big_projects_watch_documentrelation')


    models = {
        'big_projects_watch.document': {
            'Meta': {'ordering': "['-date_added']", 'object_name': 'Document'},
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'document': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'big_projects_watch.documentrelation': {
            'Meta': {'object_name': 'DocumentRelation'},
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'document': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['big_projects_watch.Document']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'passage_in_document': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'passage_start_page': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'related_to_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'related_to_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"})
        },
        'big_projects_watch.event': {
            'Meta': {'ordering': "['-date']", 'object_name': 'Event'},
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'event_type': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'important': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'participants': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'related_events'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['big_projects_watch.Participant']"}),
            'project_parts': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'related_events'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['big_projects_watch.ProjectPart']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'big_projects_watch.image': {
            'Meta': {'ordering': "['title']", 'object_name': 'Image'},
            'attribution_html': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'big_projects_watch.participant': {
            'Meta': {'ordering': "['name']", 'object_name': 'Participant'},
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'participant_type': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'big_projects_watch.project': {
            'Meta': {'object_name': 'Project'},
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'desc_documents': ('django.db.models.fields.TextField', [], {}),
            'desc_goal_groups': ('django.db.models.fields.TextField', [], {}),
            'desc_participants': ('django.db.models.fields.TextField', [], {}),
            'desc_process': ('django.db.models.fields.TextField', [], {}),
            'desc_project': ('django.db.models.fields.TextField', [], {}),
            'desc_project_parts': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'responsible_participants': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'responsible_for_project'", 'symmetrical': 'False', 'to': "orm['big_projects_watch.Participant']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'big_projects_watch.projectgoal': {
            'Meta': {'object_name': 'ProjectGoal'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'performance_figure': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'project_goal_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['big_projects_watch.ProjectGoalGroup']"})
        },
        'big_projects_watch.projectgoalgroup': {
            'Meta': {'object_name': 'ProjectGoalGroup'},
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['big_projects_watch.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'big_projects_watch.projectpart': {
            'Meta': {'ordering': "['name']", 'object_name': 'ProjectPart'},
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'big_projects_watch.siteconfig': {
            'Meta': {'object_name': 'SiteConfig'},
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'contact_html': ('django.db.models.fields.TextField', [], {'default': "u'This text will be shown on the contact page.'"}),
            'desc_about': ('django.db.models.fields.TextField', [], {}),
            'footer_html': ('django.db.models.fields.TextField', [], {'default': "u'This text will be shown in the footer of the site.'"}),
            'header_bg_color': ('django.db.models.fields.CharField', [], {'default': "'#EEEEEE'", 'max_length': '7'}),
            'header_image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['big_projects_watch.Image']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'important_bg_color': ('django.db.models.fields.CharField', [], {'default': "'#990000'", 'max_length': '7'}),
            'intro_text': ('django.db.models.fields.TextField', [], {'default': "u'This is a project watch website.'"}),
            'navi_bg_color': ('django.db.models.fields.CharField', [], {'default': "'#333333'", 'max_length': '7'}),
            'navi_link_color': ('django.db.models.fields.CharField', [], {'default': "'#FFFFFF'", 'max_length': '7'}),
            'sub_title': ('django.db.models.fields.CharField', [], {'default': "u'Project Website Subtitle'", 'max_length': '250'}),
            'sub_title_color': ('django.db.models.fields.CharField', [], {'default': "'#444444'", 'max_length': '7'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u'Project Website Title'", 'max_length': '250'}),
            'title_color': ('django.db.models.fields.CharField', [], {'default': "'#990000'", 'max_length': '7'})
        },
        'big_projects_watch.websource': {
            'Meta': {'ordering': "['-date_added']", 'object_name': 'WebSource'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['big_projects_watch.Event']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['big_projects_watch']
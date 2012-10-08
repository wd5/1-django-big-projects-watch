# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table('big_projects_watch_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('receive_new_document_relation_emails', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('receive_new_comment_emails', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('big_projects_watch', ['UserProfile'])

        # Adding model 'Image'
        db.create_table('big_projects_watch_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('attribution_html', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('big_projects_watch', ['Image'])

        # Adding model 'SiteConfig'
        db.create_table('big_projects_watch_siteconfig', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default=u'Project Website Title', max_length=250)),
            ('title_color', self.gf('django.db.models.fields.CharField')(default='#990000', max_length=7)),
            ('sub_title', self.gf('django.db.models.fields.CharField')(default=u'Project Website Subtitle', max_length=250)),
            ('sub_title_color', self.gf('django.db.models.fields.CharField')(default='#444444', max_length=7)),
            ('intro_text', self.gf('django.db.models.fields.TextField')(default=u'This is a project watch website.')),
            ('header_image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['big_projects_watch.Image'], null=True, blank=True)),
            ('header_bg_color', self.gf('django.db.models.fields.CharField')(default='#EEEEEE', max_length=7)),
            ('navi_link_color', self.gf('django.db.models.fields.CharField')(default='#FFFFFF', max_length=7)),
            ('navi_bg_color', self.gf('django.db.models.fields.CharField')(default='#333333', max_length=7)),
            ('important_bg_color', self.gf('django.db.models.fields.CharField')(default='#990000', max_length=7)),
            ('desc_about', self.gf('django.db.models.fields.TextField')()),
            ('footer_html', self.gf('django.db.models.fields.TextField')(default=u'This text will be shown in the footer of the site.')),
            ('contact_html', self.gf('django.db.models.fields.TextField')(default=u'This text will be shown on the contact page.')),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('big_projects_watch', ['SiteConfig'])

        # Adding model 'WebSource'
        db.create_table('big_projects_watch_websource', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('big_projects_watch', ['WebSource'])

        # Adding model 'Participant'
        db.create_table('big_projects_watch_participant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('participant_type', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('big_projects_watch', ['Participant'])

        # Adding model 'Project'
        db.create_table('big_projects_watch_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('desc_project', self.gf('django.db.models.fields.TextField')()),
            ('desc_project_parts', self.gf('django.db.models.fields.TextField')()),
            ('desc_participants', self.gf('django.db.models.fields.TextField')()),
            ('desc_goal_groups', self.gf('django.db.models.fields.TextField')()),
            ('desc_process', self.gf('django.db.models.fields.TextField')()),
            ('desc_documents', self.gf('django.db.models.fields.TextField')()),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('big_projects_watch', ['Project'])

        # Adding M2M table for field responsible_participants on 'Project'
        db.create_table('big_projects_watch_project_responsible_participants', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['big_projects_watch.project'], null=False)),
            ('participant', models.ForeignKey(orm['big_projects_watch.participant'], null=False))
        ))
        db.create_unique('big_projects_watch_project_responsible_participants', ['project_id', 'participant_id'])

        # Adding model 'ProjectPart'
        db.create_table('big_projects_watch_projectpart', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('big_projects_watch', ['ProjectPart'])

        # Adding model 'Event'
        db.create_table('big_projects_watch_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('event_type', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('important', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('big_projects_watch', ['Event'])

        # Adding M2M table for field participants on 'Event'
        db.create_table('big_projects_watch_event_participants', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm['big_projects_watch.event'], null=False)),
            ('participant', models.ForeignKey(orm['big_projects_watch.participant'], null=False))
        ))
        db.create_unique('big_projects_watch_event_participants', ['event_id', 'participant_id'])

        # Adding M2M table for field project_parts on 'Event'
        db.create_table('big_projects_watch_event_project_parts', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm['big_projects_watch.event'], null=False)),
            ('projectpart', models.ForeignKey(orm['big_projects_watch.projectpart'], null=False))
        ))
        db.create_unique('big_projects_watch_event_project_parts', ['event_id', 'projectpart_id'])

        # Adding model 'ProjectGoalGroup'
        db.create_table('big_projects_watch_projectgoalgroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['big_projects_watch.Event'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('big_projects_watch', ['ProjectGoalGroup'])

        # Adding model 'ProjectGoal'
        db.create_table('big_projects_watch_projectgoal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('project_goal_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['big_projects_watch.ProjectGoalGroup'])),
            ('performance_figure', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('big_projects_watch', ['ProjectGoal'])

        # Adding model 'Document'
        db.create_table('big_projects_watch_document', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('document', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('big_projects_watch', ['Document'])

        # Adding M2M table for field participants on 'Document'
        db.create_table('big_projects_watch_document_participants', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('document', models.ForeignKey(orm['big_projects_watch.document'], null=False)),
            ('participant', models.ForeignKey(orm['big_projects_watch.participant'], null=False))
        ))
        db.create_unique('big_projects_watch_document_participants', ['document_id', 'participant_id'])

        # Adding M2M table for field project_parts on 'Document'
        db.create_table('big_projects_watch_document_project_parts', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('document', models.ForeignKey(orm['big_projects_watch.document'], null=False)),
            ('projectpart', models.ForeignKey(orm['big_projects_watch.projectpart'], null=False))
        ))
        db.create_unique('big_projects_watch_document_project_parts', ['document_id', 'projectpart_id'])

        # Adding M2M table for field events on 'Document'
        db.create_table('big_projects_watch_document_events', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('document', models.ForeignKey(orm['big_projects_watch.document'], null=False)),
            ('event', models.ForeignKey(orm['big_projects_watch.event'], null=False))
        ))
        db.create_unique('big_projects_watch_document_events', ['document_id', 'event_id'])

        # Adding model 'Page'
        db.create_table('big_projects_watch_page', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('document', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['big_projects_watch.Document'])),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('big_projects_watch', ['Page'])

        # Adding model 'DocumentRelation'
        db.create_table('big_projects_watch_documentrelation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('document', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['big_projects_watch.Document'])),
            ('related_to_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('related_to_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('page', self.gf('django.db.models.fields.IntegerField')()),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('activation_hash', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('big_projects_watch', ['DocumentRelation'])

        # Adding model 'Comment'
        db.create_table('big_projects_watch_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('commented_object_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('commented_object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('page', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('activation_hash', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('big_projects_watch', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table('big_projects_watch_userprofile')

        # Deleting model 'Image'
        db.delete_table('big_projects_watch_image')

        # Deleting model 'SiteConfig'
        db.delete_table('big_projects_watch_siteconfig')

        # Deleting model 'WebSource'
        db.delete_table('big_projects_watch_websource')

        # Deleting model 'Participant'
        db.delete_table('big_projects_watch_participant')

        # Deleting model 'Project'
        db.delete_table('big_projects_watch_project')

        # Removing M2M table for field responsible_participants on 'Project'
        db.delete_table('big_projects_watch_project_responsible_participants')

        # Deleting model 'ProjectPart'
        db.delete_table('big_projects_watch_projectpart')

        # Deleting model 'Event'
        db.delete_table('big_projects_watch_event')

        # Removing M2M table for field participants on 'Event'
        db.delete_table('big_projects_watch_event_participants')

        # Removing M2M table for field project_parts on 'Event'
        db.delete_table('big_projects_watch_event_project_parts')

        # Deleting model 'ProjectGoalGroup'
        db.delete_table('big_projects_watch_projectgoalgroup')

        # Deleting model 'ProjectGoal'
        db.delete_table('big_projects_watch_projectgoal')

        # Deleting model 'Document'
        db.delete_table('big_projects_watch_document')

        # Removing M2M table for field participants on 'Document'
        db.delete_table('big_projects_watch_document_participants')

        # Removing M2M table for field project_parts on 'Document'
        db.delete_table('big_projects_watch_document_project_parts')

        # Removing M2M table for field events on 'Document'
        db.delete_table('big_projects_watch_document_events')

        # Deleting model 'Page'
        db.delete_table('big_projects_watch_page')

        # Deleting model 'DocumentRelation'
        db.delete_table('big_projects_watch_documentrelation')

        # Deleting model 'Comment'
        db.delete_table('big_projects_watch_comment')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'big_projects_watch.comment': {
            'Meta': {'ordering': "['-date_added']", 'object_name': 'Comment'},
            'activation_hash': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {}),
            'commented_object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'commented_object_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'big_projects_watch.document': {
            'Meta': {'ordering': "['-date_added']", 'object_name': 'Document'},
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'document': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'events': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'related_documents'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['big_projects_watch.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participants': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'related_documents'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['big_projects_watch.Participant']"}),
            'project_parts': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'related_documents'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['big_projects_watch.ProjectPart']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'big_projects_watch.documentrelation': {
            'Meta': {'ordering': "['-date_added']", 'object_name': 'DocumentRelation'},
            'activation_hash': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'document': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['big_projects_watch.Document']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.IntegerField', [], {}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
        'big_projects_watch.page': {
            'Meta': {'ordering': "['number']", 'object_name': 'Page'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'document': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['big_projects_watch.Document']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {})
        },
        'big_projects_watch.participant': {
            'Meta': {'ordering': "['name']", 'object_name': 'Participant'},
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'participant_type': ('django.db.models.fields.CharField', [], {'max_length': '2'})
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'responsible_participants': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'responsible_for_project'", 'symmetrical': 'False', 'to': "orm['big_projects_watch.Participant']"})
        },
        'big_projects_watch.projectgoal': {
            'Meta': {'ordering': "['order']", 'object_name': 'ProjectGoal'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
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
            'Meta': {'ordering': "['order']", 'object_name': 'ProjectPart'},
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
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
        'big_projects_watch.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'receive_new_comment_emails': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'receive_new_document_relation_emails': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'big_projects_watch.websource': {
            'Meta': {'ordering': "['order']", 'object_name': 'WebSource'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
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
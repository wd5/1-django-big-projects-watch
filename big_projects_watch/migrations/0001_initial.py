# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
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

        # Adding model 'Participant'
        db.create_table('big_projects_watch_participant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('participant_type', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('info_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('big_projects_watch', ['Participant'])

        # Adding model 'Project'
        db.create_table('big_projects_watch_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('info_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('desc_project', self.gf('django.db.models.fields.TextField')()),
            ('desc_project_parts', self.gf('django.db.models.fields.TextField')()),
            ('desc_participants', self.gf('django.db.models.fields.TextField')()),
            ('desc_goal_groups', self.gf('django.db.models.fields.TextField')()),
            ('desc_process', self.gf('django.db.models.fields.TextField')()),
            ('desc_information_sources', self.gf('django.db.models.fields.TextField')()),
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
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
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

        # Adding model 'WebSource'
        db.create_table('big_projects_watch_websource', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['big_projects_watch.Event'], null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('big_projects_watch', ['WebSource'])

        # Adding model 'Document'
        db.create_table('big_projects_watch_document', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['big_projects_watch.Event'], null=True, blank=True)),
            ('document', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('big_projects_watch', ['Document'])

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
        ))
        db.send_create_signal('big_projects_watch', ['ProjectGoal'])


    def backwards(self, orm):
        # Deleting model 'Image'
        db.delete_table('big_projects_watch_image')

        # Deleting model 'SiteConfig'
        db.delete_table('big_projects_watch_siteconfig')

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

        # Deleting model 'WebSource'
        db.delete_table('big_projects_watch_websource')

        # Deleting model 'Document'
        db.delete_table('big_projects_watch_document')

        # Deleting model 'ProjectGoalGroup'
        db.delete_table('big_projects_watch_projectgoalgroup')

        # Deleting model 'ProjectGoal'
        db.delete_table('big_projects_watch_projectgoal')


    models = {
        'big_projects_watch.document': {
            'Meta': {'ordering': "['-date_added']", 'object_name': 'Document'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'document': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['big_projects_watch.Event']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
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
            'desc_goal_groups': ('django.db.models.fields.TextField', [], {}),
            'desc_information_sources': ('django.db.models.fields.TextField', [], {}),
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
            'navi_bg_color': ('django.db.models.fields.CharField', [], {'default': "'#333333'", 'max_length': '7'}),
            'navi_link_color': ('django.db.models.fields.CharField', [], {'default': "'#FFFFFF'", 'max_length': '7'}),
            'sub_title': ('django.db.models.fields.CharField', [], {'default': "u'Project Website Subtitle'", 'max_length': '250'}),
            'sub_title_color': ('django.db.models.fields.CharField', [], {'default': "'#444444'", 'max_length': '7'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u'Project Website Title'", 'max_length': '250'}),
            'title_color': ('django.db.models.fields.CharField', [], {'default': "'#990000'", 'max_length': '7'})
        },
        'big_projects_watch.websource': {
            'Meta': {'ordering': "['-date_added']", 'object_name': 'WebSource'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['big_projects_watch.Event']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['big_projects_watch']
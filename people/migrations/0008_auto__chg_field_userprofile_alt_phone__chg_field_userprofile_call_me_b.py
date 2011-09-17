# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'UserProfile.alt_phone'
        db.alter_column('people_userprofile', 'alt_phone', self.gf('django.db.models.fields.CharField')(max_length=12, null=True))

        # Changing field 'UserProfile.call_me_by'
        db.alter_column('people_userprofile', 'call_me_by', self.gf('django.db.models.fields.CharField')(max_length=256, null=True))

        # Changing field 'UserProfile.end_date'
        db.alter_column('people_userprofile', 'end_date', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'UserProfile.office'
        db.alter_column('people_userprofile', 'office', self.gf('django.db.models.fields.CharField')(max_length=256, null=True))

        # Changing field 'UserProfile.phone'
        db.alter_column('people_userprofile', 'phone', self.gf('django.db.models.fields.CharField')(max_length=12, null=True))

        # Changing field 'UserProfile.about_me'
        db.alter_column('people_userprofile', 'about_me', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'UserProfile.start_date'
        db.alter_column('people_userprofile', 'start_date', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'UserProfile.grad_date'
        db.alter_column('people_userprofile', 'grad_date', self.gf('django.db.models.fields.DateField')(null=True))


    def backwards(self, orm):
        
        # Changing field 'UserProfile.alt_phone'
        db.alter_column('people_userprofile', 'alt_phone', self.gf('django.db.models.fields.CharField')(default='', max_length=12))

        # Changing field 'UserProfile.call_me_by'
        db.alter_column('people_userprofile', 'call_me_by', self.gf('django.db.models.fields.CharField')(default='', max_length=256))

        # Changing field 'UserProfile.end_date'
        db.alter_column('people_userprofile', 'end_date', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'UserProfile.office'
        db.alter_column('people_userprofile', 'office', self.gf('django.db.models.fields.CharField')(max_length=256))

        # Changing field 'UserProfile.phone'
        db.alter_column('people_userprofile', 'phone', self.gf('django.db.models.fields.CharField')(default='', max_length=12))

        # Changing field 'UserProfile.about_me'
        db.alter_column('people_userprofile', 'about_me', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'UserProfile.start_date'
        db.alter_column('people_userprofile', 'start_date', self.gf('django.db.models.fields.DateField')())

        # Changing field 'UserProfile.grad_date'
        db.alter_column('people_userprofile', 'grad_date', self.gf('django.db.models.fields.DateField')(null=True))


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
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'people.employmentstatus': {
            'Meta': {'object_name': 'EmploymentStatus'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'people.paygrade': {
            'Meta': {'object_name': 'PayGrade'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'wage': ('django.db.models.fields.FloatField', [], {})
        },
        'people.timeperiod': {
            'Meta': {'object_name': 'TimePeriod'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'people.title': {
            'Meta': {'object_name': 'Title'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'pay_grade': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.PayGrade']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'workgroup': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.WorkGroup']"})
        },
        'people.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'about_me': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'alt_phone': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'call_me_by': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date(2012, 12, 21)', 'blank': 'True'}),
            'grad_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date(1861, 9, 13)', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'office': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'staff_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.fromtimestamp(0)', 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.EmploymentStatus']", 'blank': 'True'}),
            'supervisor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'supervisor'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'title': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Title']", 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'uwnetid'", 'unique': 'True', 'to': "orm['auth.User']"}),
            'working_periods': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.TimePeriod']", 'blank': 'True'})
        },
        'people.workgroup': {
            'Meta': {'object_name': 'WorkGroup'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['people']
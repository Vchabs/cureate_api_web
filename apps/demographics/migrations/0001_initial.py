# Generated by Django 2.1.2 on 2018-11-15 00:11

import django.contrib.postgres.fields.ranges
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityLevel',
            fields=[
                ('row_create_ts', model_utils.fields.AutoCreatedField(db_column='row_create_ts', default=django.utils.timezone.now, editable=False)),
                ('row_lup_ts', model_utils.fields.AutoLastModifiedField(db_column='row_lup_ts', default=django.utils.timezone.now, editable=False)),
                ('row_end_ts', models.DateTimeField(db_column='row_end_ts', default='9999-12-31 00:00:00.00000-00')),
                ('row_ef', models.BooleanField(db_column='row_ef', default=True)),
                ('row_create_usr_id', models.CharField(db_column='row_create_usr_id', default="'docker'", max_length=20)),
                ('row_lup_usr_id', models.CharField(db_column='row_lup_usr_id', default="'docker'", max_length=20)),
                ('ID', models.AutoField(db_column='activity_level_id', primary_key=True, serialize=False)),
                ('value', models.TextField(db_column='value', unique=True)),
            ],
            options={
                'db_table': 'activity_level',
            },
        ),
        migrations.CreateModel(
            name='AgeLevel',
            fields=[
                ('row_create_ts', model_utils.fields.AutoCreatedField(db_column='row_create_ts', default=django.utils.timezone.now, editable=False)),
                ('row_lup_ts', model_utils.fields.AutoLastModifiedField(db_column='row_lup_ts', default=django.utils.timezone.now, editable=False)),
                ('row_end_ts', models.DateTimeField(db_column='row_end_ts', default='9999-12-31 00:00:00.00000-00')),
                ('row_ef', models.BooleanField(db_column='row_ef', default=True)),
                ('row_create_usr_id', models.CharField(db_column='row_create_usr_id', default="'docker'", max_length=20)),
                ('row_lup_usr_id', models.CharField(db_column='row_lup_usr_id', default="'docker'", max_length=20)),
                ('ID', models.AutoField(db_column='age_level_id', primary_key=True, serialize=False)),
                ('value', django.contrib.postgres.fields.ranges.IntegerRangeField(db_column='value', unique=True)),
            ],
            options={
                'db_table': 'age_level',
            },
        ),
        migrations.CreateModel(
            name='AlcoholStatus',
            fields=[
                ('row_create_ts', model_utils.fields.AutoCreatedField(db_column='row_create_ts', default=django.utils.timezone.now, editable=False)),
                ('row_lup_ts', model_utils.fields.AutoLastModifiedField(db_column='row_lup_ts', default=django.utils.timezone.now, editable=False)),
                ('row_end_ts', models.DateTimeField(db_column='row_end_ts', default='9999-12-31 00:00:00.00000-00')),
                ('row_ef', models.BooleanField(db_column='row_ef', default=True)),
                ('row_create_usr_id', models.CharField(db_column='row_create_usr_id', default="'docker'", max_length=20)),
                ('row_lup_usr_id', models.CharField(db_column='row_lup_usr_id', default="'docker'", max_length=20)),
                ('ID', models.AutoField(db_column='alcohol_status_id', primary_key=True, serialize=False)),
                ('value', models.TextField(db_column='value', unique=True)),
            ],
            options={
                'db_table': 'alcohol_status',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('row_create_ts', model_utils.fields.AutoCreatedField(db_column='row_create_ts', default=django.utils.timezone.now, editable=False)),
                ('row_lup_ts', model_utils.fields.AutoLastModifiedField(db_column='row_lup_ts', default=django.utils.timezone.now, editable=False)),
                ('row_end_ts', models.DateTimeField(db_column='row_end_ts', default='9999-12-31 00:00:00.00000-00')),
                ('row_ef', models.BooleanField(db_column='row_ef', default=True)),
                ('row_create_usr_id', models.CharField(db_column='row_create_usr_id', default="'docker'", max_length=20)),
                ('row_lup_usr_id', models.CharField(db_column='row_lup_usr_id', default="'docker'", max_length=20)),
                ('ID', models.AutoField(db_column='gender_id', primary_key=True, serialize=False)),
                ('value', models.TextField(db_column='value', unique=True)),
            ],
            options={
                'db_table': 'gender',
            },
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('row_create_ts', model_utils.fields.AutoCreatedField(db_column='row_create_ts', default=django.utils.timezone.now, editable=False)),
                ('row_lup_ts', model_utils.fields.AutoLastModifiedField(db_column='row_lup_ts', default=django.utils.timezone.now, editable=False)),
                ('row_end_ts', models.DateTimeField(db_column='row_end_ts', default='9999-12-31 00:00:00.00000-00')),
                ('row_ef', models.BooleanField(db_column='row_ef', default=True)),
                ('row_create_usr_id', models.CharField(db_column='row_create_usr_id', default="'docker'", max_length=20)),
                ('row_lup_usr_id', models.CharField(db_column='row_lup_usr_id', default="'docker'", max_length=20)),
                ('ID', models.AutoField(db_column='race_id', primary_key=True, serialize=False)),
                ('value', models.TextField(db_column='value', unique=True)),
            ],
            options={
                'db_table': 'race',
            },
        ),
        migrations.CreateModel(
            name='ReadingLevel',
            fields=[
                ('row_create_ts', model_utils.fields.AutoCreatedField(db_column='row_create_ts', default=django.utils.timezone.now, editable=False)),
                ('row_lup_ts', model_utils.fields.AutoLastModifiedField(db_column='row_lup_ts', default=django.utils.timezone.now, editable=False)),
                ('row_end_ts', models.DateTimeField(db_column='row_end_ts', default='9999-12-31 00:00:00.00000-00')),
                ('row_ef', models.BooleanField(db_column='row_ef', default=True)),
                ('row_create_usr_id', models.CharField(db_column='row_create_usr_id', default="'docker'", max_length=20)),
                ('row_lup_usr_id', models.CharField(db_column='row_lup_usr_id', default="'docker'", max_length=20)),
                ('ID', models.AutoField(db_column='reading_level_id', primary_key=True, serialize=False)),
                ('value', models.TextField(db_column='value', unique=True)),
            ],
            options={
                'db_table': 'reading_level',
            },
        ),
        migrations.CreateModel(
            name='SmokingStatus',
            fields=[
                ('row_create_ts', model_utils.fields.AutoCreatedField(db_column='row_create_ts', default=django.utils.timezone.now, editable=False)),
                ('row_lup_ts', model_utils.fields.AutoLastModifiedField(db_column='row_lup_ts', default=django.utils.timezone.now, editable=False)),
                ('row_end_ts', models.DateTimeField(db_column='row_end_ts', default='9999-12-31 00:00:00.00000-00')),
                ('row_ef', models.BooleanField(db_column='row_ef', default=True)),
                ('row_create_usr_id', models.CharField(db_column='row_create_usr_id', default="'docker'", max_length=20)),
                ('row_lup_usr_id', models.CharField(db_column='row_lup_usr_id', default="'docker'", max_length=20)),
                ('ID', models.AutoField(db_column='smoking_status_id', primary_key=True, serialize=False)),
                ('value', models.TextField(db_column='value', unique=True)),
            ],
            options={
                'db_table': 'smoking_status',
            },
        ),
    ]

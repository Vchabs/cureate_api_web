# Generated by Django 2.1.2 on 2018-11-26 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diseases', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complication',
            name='row_create_usr_id',
            field=models.CharField(db_column='row_create_usr_id', default='dockerbash', max_length=20),
        ),
        migrations.AlterField(
            model_name='complication',
            name='row_lup_usr_id',
            field=models.CharField(db_column='row_lup_usr_id', default='dockerbash', max_length=20),
        ),
        migrations.AlterField(
            model_name='disease',
            name='row_create_usr_id',
            field=models.CharField(db_column='row_create_usr_id', default='dockerbash', max_length=20),
        ),
        migrations.AlterField(
            model_name='disease',
            name='row_lup_usr_id',
            field=models.CharField(db_column='row_lup_usr_id', default='dockerbash', max_length=20),
        ),
    ]

import uuid
from django.db import models
from lib.model_stamps import RowStatusModel
from django.contrib.auth.models import User
from demographics.models import AgeLevel, Gender,Race, ReadingLevel, SmokingStatus,AlcoholStatus,ActivityLevel
from diseases.models import Disease, Complication


class ContentType(RowStatusModel):

    ID = models.AutoField(primary_key=True,db_column='content_type_id')
    value = models.TextField(db_column='value', unique=True)

    class Meta:
        db_table = 'content_type'

class Content(RowStatusModel):

    #Note this is intentional - Typically your primary key should not be the same as a natural key. Always make it different.
    # UUID Fields are great if you have a ton of data, otherwise an AutoField is preferable (uses less space...indexes can be smaller, but UUID fields are small enough)
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_column = 'content_id')
    # Content based fields
    title = models.TextField(db_column='title')
    description = models.TextField(db_column='description')
    image_url = models.TextField(db_column='image_url')
    content_type = models.ForeignKey(ContentType,  on_delete='PROTECT', db_column ='content_type')

    #Disease based fields
    diseases = models.ManyToManyField(Disease)
    complications = models.ManyToManyField(Complication)
    
    #Fields Corresponding to user characteristics/demographics
    gender = models.ManyToManyField(Gender) #do we want this to be a range like <5, 6-10, 11-16,17-21, 21-40, etc.? Think content may be best suited for that
    race = models.ManyToManyField(Race)
    age_level = models.ManyToManyField(AgeLevel) #do we want this to be a range like <5, 6-10, 11-16,17-21, 21-40, etc.? Think content may be best suited for that
    reading_level = models.ManyToManyField(ReadingLevel)
    smoking_status = models.ManyToManyField(SmokingStatus)
    alcohol_status = models.ManyToManyField(AlcoholStatus)
    activity_level = models.ManyToManyField(ActivityLevel)

    class Meta:
        db_table = 'content'




from django.db import models
from django.contrib.auth.models import AbstractUser
from lib.model_stamps import RowStatusModel

from demographics.models import AgeLevel, Gender,Race, ReadingLevel, SmokingStatus,AlcoholStatus,ActivityLevel
from diseases.models import Disease, Complication

class User(AbstractUser,RowStatusModel):
	age_level = models.ForeignKey(AgeLevel, db_column='age_level_id', on_delete='PROTECT')
	gender =  models.ForeignKey(Gender, db_column='gender_id', on_delete='PROTECT')
	race = models.ForeignKey(Race, db_column='race_id', on_delete='PROTECT')
	reading_level = models.ForeignKey(ReadingLevel, db_column='reading_level_id', on_delete='PROTECT')
	smoking_status = models.ForeignKey(SmokingStatus, db_column='smoking_status_id', on_delete='PROTECT')
	alcohol_status = models.ForeignKey(AlcoholStatus, db_column='alcohol_status_id', on_delete='PROTECT')
	activity_level = models.ForeignKey(ActivityLevel, db_column='activity_level_id', on_delete='PROTECT')
	disease = models.ForeignKey(Disease, db_column ='disease_id', on_delete='PROTECT')
	complication = models.ForeignKey(Complication, db_column ='complication_id', on_delete='PROTECT')
	# This is going to have to be modeled differently because someone can definitely have multiple doctors appointments for each condition
	# This next line is for demo purposes only and REALLY NEEDS TO BE REFACTORED FOR PRODUCTION
	diagnosis_date = models.DateTimeField(db_column='diagnosis_date')


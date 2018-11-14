import uuid
from django.db import models
from lib.model_stamps import RowStatusModel
from django.contrib.postgres.fields import IntegerRangeField


class AgeLevel(RowStatusModel):

    ID = models.AutoField(primary_key=True,db_column='age_level_id')
    value = IntegerRangeField(db_column='value', unique=True)

    class Meta:
        db_table = 'age_level'

class Gender(RowStatusModel):

    ID = models.AutoField(primary_key=True,db_column='gender_id')
    value = models.TextField(db_column='value', unique=True)

    class Meta:
        db_table = 'gender'

class Race(RowStatusModel):

    ID = models.AutoField(primary_key=True,db_column='race_id')
    value = models.TextField(db_column='value', unique=True)

    class Meta:
        db_table = 'race'

class ReadingLevel(RowStatusModel):

    ID = models.AutoField(primary_key=True,db_column='reading_level_id')
    value = models.TextField(db_column='value', unique=True)

    class Meta:
        db_table = 'reading_level'


class SmokingStatus(RowStatusModel):

    ID = models.AutoField(primary_key=True,db_column='smoking_status_id')
    value = models.TextField(db_column='value', unique=True)
   
    class Meta:
        db_table = 'smoking_status'

class AlcoholStatus(RowStatusModel):


    ID = models.AutoField(primary_key=True,db_column='alcohol_status_id')
    value = models.TextField(db_column='value', unique=True)
   
    class Meta:
        db_table = 'alcohol_status'	

class ActivityLevel(RowStatusModel):


    ID = models.AutoField(primary_key=True,db_column='activity_level_id')
    value = models.TextField(db_column='value', unique=True)
   
    class Meta:
        db_table = 'activity_level'	



"""
class State(RowStatusModel):

    ID = models.AutoField(primary_key=True,db_column='state_id')
    value = models.TextField(db_column='value')

    class Meta:
        db_table = 'state'
"""

"""
class HospitalNetwork(RowStatusModel):

    ID = models.AutoField(primary_key=True,db_column='hospital_network_id')
    value = models.TextField(db_column='value')

    class Meta:
        db_table = 'hospital_network'
"""


"""
class Doctor(RowStatusModel):

    ID = models.AutoField(primary_key=True,db_column='doctor_id')
    value = models.TextField(db_column='value')

    class Meta:
        db_table = 'doctor'
"""
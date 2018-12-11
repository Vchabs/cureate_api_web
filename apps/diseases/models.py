import uuid
from django.db import models
from lib.model_stamps import RowStatusModel

class Disease(RowStatusModel):

    #Note this is intentional - Typically your primary key should not be the same as a natural key. Always make it different.
    # UUID Fields are great if you have a ton of data, otherwise an AutoField is preferable (uses less space...indexes can be smaller, but UUID fields are small enough)
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_column = 'disease_id')
    value = models.TextField(db_column='title')
    

    def __unicode__(self):
        return '%s' % self.value

    def __str__(self):
        return '%s' % self.value
        
    class Meta:
        db_table = 'disease'

class Complication(RowStatusModel):

    #Note this is intentional - Typically your primary key should not be the same as a natural key. Always make it different.
    # UUID Fields are great if you have a ton of data, otherwise an AutoField is preferable (uses less space...indexes can be smaller, but UUID fields are small enough)
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_column = 'complication_id')
    value = models.TextField(db_column='value')
    disease = models.ForeignKey(Disease, db_column ='disease_id', on_delete=models.PROTECT)


    def __unicode__(self):
        return '%s' % self.disease

    def __str__(self):
        return '%s' % self.value

    class Meta:
        db_table = 'complication'

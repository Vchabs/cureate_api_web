from django.core.management.base import BaseCommand, CommandError
from psycopg2.extras import NumericRange
from django.contrib.auth.models import User

from demographics.models import ReadingLevel, Race, AgeLevel, Gender, SmokingStatus, AlcoholStatus,ActivityLevel


def sanitize_get_or_create(Model,input):
    if input =='' or input == " ":
       return
    elif '\n' in input:
       input = input.rstrip('\n')
       if input != "" or input!=" ":
           Model.objects.get_or_create(value=input)
    else:
        Model.objects.get_or_create(value=input)

class Command(BaseCommand):
    help = 'Loads data'
    ReadingLevel.objects.all().delete()
    Race.objects.all().delete()
    AgeLevel.objects.all().delete()
    Gender.objects.all().delete()
    SmokingStatus.objects.all().delete()
    AlcoholStatus.objects.all().delete()
    ActivityLevel.objects.all().delete()
    

    def handle(self, *args, **options):
        with open('data/demographic_sample_data.csv') as f:
            #iterate through spreadsheets 
            n = 0
            for line in f:
                if n > 0:
                    line = line.rstrip("\n")
                    v = line.split(',')
                    sanitize_get_or_create(ReadingLevel,v[5])
                    sanitize_get_or_create(Race,v[10])
                    sanitize_get_or_create(Gender,v[6])
                    sanitize_get_or_create(SmokingStatus,v[7])
                    sanitize_get_or_create(AlcoholStatus,v[8])
                    sanitize_get_or_create(ActivityLevel,v[9])
                    # reading = ReadingLevel.objects.get_or_create(value = v[5])
                    # race = Race.objects.get_or_create(value = v[10])
                    # try:
                    if v[2] != '':
                        age_range = NumericRange(int(v[2]),int(v[3]))                      
                        age = AgeLevel.objects.get_or_create(value = age_range)

                    # except:
                    #     pass
                    # gender = Gender.objects.get_or_create(value = v[6])
                    # smoking = SmokingStatus.objects.get_or_create(value = v[7])
                    # alcohol = AlcoholStatus.objects.get_or_create(value = v[8])
                    # activity = ActivityLevel.objects.get_or_create(value = v[9])


                n += 1


from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
import json
from content.models import Content

from django.contrib.auth.models import User

from demographics.models import ReadingLevel, Race, AgeLevel, Gender, SmokingStatus, AlcoholStatus,ActivityLevel


class Command(BaseCommand):
    help = 'Loads data'
    age_ranges = [range(0,19),range(19,26)]
    for i in range(5,20):
        age_ranges.append(range(5*i + 1, 5*i+6))

    def handle(self, *args, **options):

        with open('data/demographic_sample_data.csv') as f:
        	#iterate through spreadsheets 
            n = 0
            for line in f:
                if n > 0:
                    v = line.split(',')
                	age_ranges = 0-18,19-25,26-30#
                	reading = ReadingLevel.objects.get_or_create(value = v[5])
                	reading.save()
                	race = Race.objects.get_or_create(value = v[10])
                	race.save()
                	age = AgeLevel.objects.get_or_create(value = list(filter(lambda x: int(v[3]) in x,age_ranges))[0])
                	age.save()
                	gender = Gender.objects.get_or_create(value = v[6])
                	gender.save()
                	smoking = SmokingStatus.objects.get_or_create(value = v[7])
                	smoking.save()
                	alcohol = AlcoholStatus.objects.get_or_create(value = v[8])
                	alcohol.save()
                	activity = ActivityLevel.objects.get_or_create(value = v[9])
                	activity.save()


                n += 1
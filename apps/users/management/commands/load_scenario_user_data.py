from django.core.management.base import BaseCommand, CommandError

from users.models import User

from demographics.models import AgeLevel, Gender,Race, ReadingLevel, SmokingStatus,AlcoholStatus,ActivityLevel
from diseases.models import Disease, Complication

from psycopg2.extras import NumericRange



class Command(BaseCommand):
    help = 'Loads data'


    def handle(self, *args, **options):
        gender = Gender.objects.get(value = 'Male')
        age = AgeLevel.objects.get(value = NumericRange(41,45))
        race = Race.objects.get(value = 'White')
        reading_level = ReadingLevel.objects.get(value = 'College')
        smoking_status = SmokingStatus.objects.get(value = 'Past Smoker')
        alcohol_status = AlcoholStatus.objects.get(value = '2-3x week (casual)')
        for item in ActivityLevel.objects.all():
            print(item.value)

        activity_level = ActivityLevel.objects.get(value__iregex = 'mi')
        print(activity_level)
        disease = Disease.objects.get(value = 'CVD')
        complication = Complication.objects.get(value = 'Diabetes', disease = disease)



        user = User.objects.create_user(username="Dan",password="dan", smoking_status=smoking_status, age_level=age, gender=gender,race=race, reading_level=reading_level, alcohol_status = alcohol_status,activity_level=activity_level,disease=disease,complication=complication)

   


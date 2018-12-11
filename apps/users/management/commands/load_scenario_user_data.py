from django.core.management.base import BaseCommand, CommandError

from users.models import User

from demographics.models import AgeLevel, Gender,Race, ReadingLevel, SmokingStatus,AlcoholStatus,ActivityLevel
from diseases.models import Disease, Complication

from psycopg2.extras import NumericRange
from datetime import datetime, timezone, timedelta

class Command(BaseCommand):
    help = 'Loads data'


    def handle(self, *args, **options):
        User.objects.all().delete()
        gender = Gender.objects.get(value = 'Male')
        age = AgeLevel.objects.get(value = NumericRange(41,45))
        race = Race.objects.get(value = 'White')
        reading_level = ReadingLevel.objects.get(value = 'College')
        smoking_status = SmokingStatus.objects.get(value = 'Past Smoker')
        alcohol_status = AlcoholStatus.objects.get(value = '2-3x week (casual)')


        activity_level = ActivityLevel.objects.get(value__iregex = 'mi')

        disease = Disease.objects.get(value = 'CVD')
        complication = Complication.objects.get(value = 'Diabetes', disease = disease)
        diagnosis_date = datetime.now(timezone.utc)


        user = User.objects.create_user(username="Dan",
                                    password="dan", 
                                    smoking_status=smoking_status, 
                                    age_level=age, 
                                    gender=gender,
                                    race=race, 
                                    reading_level=reading_level, 
                                    alcohol_status = alcohol_status,
                                    activity_level=activity_level,
                                    disease=disease,
                                    complication=complication, 
                                    diagnosis_date=diagnosis_date)

   
        # Create another Dan 20 days away
        diagnosis_date = datetime.now(timezone.utc) - timedelta(days=20)
        

        user = User.objects.create_user(username="Dan (@ 20 days)",
                                    password="dan",
                                    smoking_status=smoking_status, 
                                    age_level=age,
                                    gender=gender,
                                    race=race, 
                                    reading_level=reading_level, 
                                    alcohol_status = alcohol_status,
                                    activity_level=activity_level,
                                    disease=disease,
                                    complication=complication, 
                                    diagnosis_date=diagnosis_date)

        gender = Gender.objects.get(value = 'Female')
        age = AgeLevel.objects.get(value = NumericRange(41,45))
        race = Race.objects.get(value = 'White')
        reading_level = ReadingLevel.objects.get(value = 'College')
        smoking_status = SmokingStatus.objects.get(value = 'Never Smoked')
        alcohol_status = AlcoholStatus.objects.get(value = '1x week (social)')
        activity_level = ActivityLevel.objects.get(value__iregex = 'he')
        disease = Disease.objects.get(value = 'CVD')
        diagnosis_date = datetime.now(timezone.utc)



        user = User.objects.create_user(username="Paula",
                                    password="paula",
                                    smoking_status=smoking_status, 
                                    age_level=age,
                                    gender=gender,
                                    race=race, 
                                    reading_level=reading_level, 
                                    alcohol_status = alcohol_status,
                                    activity_level=activity_level,
                                    disease=disease,
                                    complication=complication, 
                                    diagnosis_date=diagnosis_date)
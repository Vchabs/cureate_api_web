from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
import json

from content.models import Content,ContentType, SharePeriod
from demographics.models import AgeLevel, Gender,Race, ReadingLevel, SmokingStatus,AlcoholStatus,ActivityLevel
from diseases.models import Disease, Complication

from psycopg2.extras import NumericRange
import datetime
from django.contrib.auth.models import User


def _get_age_ranges(low,high):
    age_ranges = []
    if not(low is None and high is None):       
        i = low
        if low < 19:
            age_ranges.append(NumericRange(0,18))
        if high > 25:
            age_ranges.append(NumericRange(19,25))
            i = 26
        while (i > 25) and (i <= high):
            age_ranges.append(NumericRange(i,i + 4))
            i += 5
    return age_ranges



        




class Command(BaseCommand):
    help = 'Loads data'

    def handle(self, *args, **options):
        Content.objects.all().delete()
        SharePeriod.objects.all().delete()
        ContentType.objects.all().delete()
        with open('data/content_sample_data_updated.csv') as f:
            n = 0
            for line in f:
                if n > 0:
                    v = [x.strip('\n') for x in line.split(',')]
                    description_text = ','.join(v[14:])
                    title_name = v[13]
                    image_url = v[12]
                    v = v[:12]
                    v = [None if (x == '') or (x == ' ') else x for x in v]
                    start_date = datetime.timedelta(days=int(v[10]))
                    end_date = datetime.timedelta(days=int(v[11]))

                    date_range = SharePeriod.objects.get_or_create(start_date_interval=start_date, end_date_interval=end_date)[0]

                    content_type = ContentType.objects.get_or_create(value = 'Article')[0]

                    content = Content.objects.get_or_create(title = title_name,
                                                            description = description_text, 
                                                            content_type = content_type,
                                                            image_url = image_url,
                                                            share_period=date_range)[0]
                    

                    age_ranges = _get_age_ranges(int(v[0]),int(v[1]))
                    #Make better

                    if len(age_ranges) > 0:
                        for ar in age_ranges:
                            age = AgeLevel.objects.get(value = ar)
                            content.age_level.add(age)
                    else:
                        for ar in AgeLevel.objects.all():
                            content.age_level.add(ar)

                    if not(v[2] is None):
                        g = Gender.objects.get(value=v[2])
                        content.gender.add(g)
                    else:
                        for g in Gender.objects.all():
                            content.gender.add(g)

                    if not(v[3] is None):
                        r = Race.objects.get(value=v[3])
                        content.race.add(r)
                    else:
                        for r in Race.objects.all():
                            content.race.add(r)

                    if not(v[4] is None):
                        rl = ReadingLevel.objects.get(value=v[4])
                        content.reading_level.add(r)
                    else:
                        for rl in ReadingLevel.objects.all():
                            content.reading_level.add(rl)

                    if not(v[5] is None):
                        ss = SmokingStatus.objects.get(value=v[5])
                        content.smoking_status.add(ss)
                    else:
                        for ss in SmokingStatus.objects.all():
                            content.smoking_status.add(ss)

                    if not(v[6] is None):
                        alcs = AlcoholStatus.objects.get(value=v[6])
                        content.alcohol_status.add(alcs)
                    else:
                        for alcs in AlcoholStatus.objects.all():
                            content.alcohol_status.add(alcs)

                    if not(v[7] is None):
                        al = ActivityLevel.objects.get(value=v[7])
                        content.activity_level.add(al)
                    else:
                        for al in ActivityLevel.objects.all():
                            content.activity_level.add(al)

                    
                    ds = Disease.objects.get(value=v[8])
                    content.diseases.add(ds)
                    if not(v[9] is None):
                        comp = Complication.objects.get(value=v[8],disease = ds)
                        content.complications.add(comp)


                  

                    
                    

                n += 1
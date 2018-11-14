from django.core.management.base import BaseCommand, CommandError
from psycopg2.extras import NumericRange
from django.contrib.auth.models import User

from diseases.models import Disease,Complication


def sanitize_get_or_create(Model,val,dis):
    if Model is Disease:
        if val =='' or val == " ":
           return
        elif '\n' in val:
           val = val.rstrip('\n')
           if val != "" or val!=" ":
               return Disease.objects.get_or_create(value=val)
        else:
            return Disease.objects.get_or_create(value=val)
    if Model is Complication:
        if (val =='' or val == " "):
           return
        elif ('\n' in val):
           val = val.rstrip('\n')
           if (val != "" or val!=" "):
               Complication.objects.get_or_create(value=val,disease = dis)
        else:
            Complication.objects.get_or_create(value=val, disease = dis)

class Command(BaseCommand):
    help = 'Loads data'


    def handle(self, *args, **options):
        with open('data/disease_sample_data.csv') as f:
            #iterate through spreadsheets 
            n = 0
            for line in f:
                if n > 0:
                    line = line.rstrip("\n")
                    v = line.split(',')
                    d = sanitize_get_or_create(Disease,v[0],v[0])[0]
                    sanitize_get_or_create(Complication,v[1],d)
         


                n += 1


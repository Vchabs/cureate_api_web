# from django.core.management.base import BaseCommand, CommandError
# from django.db import transaction
# import json
# from content.models import Content

# from django.contrib.auth.models import User

# class Command(BaseCommand):
#     help = 'Loads data'

#     def handle(self, *args, **options):

#         with open('data/sample_data.csv') as f:
#             n = 0
#             for line in f:
#                 if n > 0:
#                     key = line.split(',')[0]
#                     title = line.split(',')[1]
#                     content = ','.join(line.split(',')[2:])
#                     print(key)
#                     if "1" in key:
#                         username = "Dan"
#                     elif "2" in key:
#                         username= "Paula"
#                     else:
#                         print("ERROR NEW KEY", key)
#                     if not User.objects.filter(username=username).exists():
#                         if "1" in key:
#                             user = User.objects.create_user(username="Dan",password="dan")
#                         elif "2" in key:
#                             user = User.objects.create_user(username="Paula",password="paula")
#                     else:
#                         user = User.objects.get(username=username)

#                     new_content = Content(title = title,description = content)
#                     new_content.save()
#                     new_content.user_id.add(user)

#                 n += 1
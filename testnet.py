import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'deployment.settings')
import django
django.setup()

from members.models import Member

members = Member.objects.all()
for m in members:
    print(m)



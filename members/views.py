from django.shortcuts import render
from .models import Member

# Create your views here.

def members(request):
    members = Member.objects.all()
    return render(request, 'members/index.html', 
    context={
        "members": members
    })
  
  
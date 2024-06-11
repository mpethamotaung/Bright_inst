# shared_assets/assets/views.py

from django.shortcuts import render

def base(request):
    return render(request, 'base.html')

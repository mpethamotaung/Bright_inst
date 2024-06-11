from django.shortcuts import render

#def function that renders the homepage (home.html)
def home(request):
    return render(request, 'home.html')

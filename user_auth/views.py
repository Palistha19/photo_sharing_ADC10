from django.shortcuts import render

# Create your views here.

def get_login_page(req):
    return render(req,"loign.html")
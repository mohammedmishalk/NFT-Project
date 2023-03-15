from django.shortcuts import render

# Create your views here.

def js(req):
    return render(req, "hello word")
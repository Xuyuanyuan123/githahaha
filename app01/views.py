from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def test(request):
    return redirect("test.html")

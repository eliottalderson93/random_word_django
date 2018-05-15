from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.utils.crypto import get_random_string
  # the index function is called when root is visited
initial_random = get_random_string(length=15)
def index(request):
    context = { #declare variables
            "email" : "grootisgood@mail.com",
            "name" : "Erik Nordland",
            "time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
            "random" :  initial_random,
            "attempt" : 1
    }
    if ('initial' in request.session):
        request.session['initial'] = False
        request.session['attempt'] +=1
        request.session['random'] = get_random_string(length=10)
        print("NEW::",request.session['attempt'])
    else:
        request.session['initial'] = True
        request.session['attempt'] = context['attempt']
        request.session['random'] = context['random']
        print("INIT::",request.session['attempt'])
    return render(request, "django_app\index.html", context)
def new(request):
    response = "Placeholder to display a new form to create a new blog"
    return HttpResponse(response)
def generate(request):
    if request.method == "POST":
        return redirect("/")
    else:
        return redirect("/")
def show(request, number):
    response = "Placeholder to display blog "+str(number)
    return HttpResponse(response)
def edit(request, number):
    response = "placeholder to edit blog "+str(number)
    return HttpResponse(response)
def destroy(request):
    request.session.clear()
    return redirect('/')
# views.py


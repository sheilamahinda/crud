from django.shortcuts import render
from django.http import HttpResponse
from .models import People


# Create your views here.
def home(request):
    return render(request, 'home.html')


def insert(request):
    if request.method == "POST":
        name = request.POST.get('name')
        school = request.POST.get('school')
        email = request.POST.get('email')

        # this is the variable in which it will be saved
        person = People(name=name, school=school, email=email)

        person.save()

        # print(name, school, email)

        # what it will output
    return HttpResponse("Success")


def people(request):
    d = People.objects.all()

    return render(request, 'people.html', {
        "data": d
    })


def delete(request, id):
    dd = People.objects.get(id=id)
    dd.delete()

    return HttpResponse("Delete Successfully")


def update(request, id):
    l = People.objects.get(id=id)

    return render(request, 'edit.html', {
        "l": l
    })

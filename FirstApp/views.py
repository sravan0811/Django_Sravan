from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from .forms import NewUser
# Create your views here.

def home(request):
    #return HttpResponse("Welcome to Django")
    return render(request, 'FirstApp/home.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == "POST":
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Validation Success")


    return render(request, 'FirstApp/forms_page.html',{'form':form})


def user(request):
    form1 = forms.NewUser()

    if request.method == 'POST':
        form1 = NewUser(request.POST)

        if form1.is_valid():
            form1.save(commit=True)
            return home(request)
        else:
            print("Form Invalid")

    return render(request, 'FirstApp/users.html', {'form1': form1 })
from django.http import HttpResponseRedirect
from django.shortcuts import render

from jenga_qr.generator.forms import QRForm


def index(request):
    context = {}
    return render(request, "generator/index.html", context)


def generate(request):
    context = {}
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = QRForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = QRForm()

    return render(request, "generator/generate.html", {"form": form})

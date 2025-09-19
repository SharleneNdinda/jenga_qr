from django.shortcuts import redirect, render
from django.urls import reverse
from .models import QRCode

from jenga_qr.generator.forms import QRForm


def index(request):
    context = {}
    return render(request, "generator/index.html", context)


def results(request):
    obj_id = request.session.get("qr_code_id")
    obj = None
    if obj_id:
        try:
            obj = QRCode.objects.get(guid=obj_id)
        except QRCode.DoesNotExist:
            obj = None
    return render(request, "generator/results.html", {"obj": obj})


def generate(request):
    if request.method == "POST":
        form = QRForm(request.POST)
        if form.is_valid():
            obj = form.save()
            request.session["qr_code_id"] = str(obj.guid)
            return redirect(reverse("generator:results"))
    else:
        form = QRForm()

    return render(request, "generator/generate.html", {"form": form})

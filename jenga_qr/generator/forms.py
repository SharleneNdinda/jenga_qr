from django import forms
from .models import QRCode


class QRForm(forms.ModelForm):
    class Meta:
        model = QRCode
        fields = ["data"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["data"].label = ""
        self.fields["data"].widget.attrs.update({"class": "text-class"})

from django import forms
from .models import QRCode


class QRForm(forms.ModelForm):
    class Meta:
        model = QRCode
        fields = ['data'] 
    # forms.Form):
    # data = forms.CharField(
    #     max_length=250,
    #     widget=forms.TextInput(
    #         attrs={"placeholder": "Please provide the text to generate into a qrcode"}
    #     ),
    # )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["data"].label = ""
        self.fields["data"].widget.attrs.update({'class': 'text-class'})

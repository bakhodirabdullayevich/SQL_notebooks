from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django import forms
from .models import Object, Meter, FlowMeterSertificate


class ObjectForm(forms.ModelForm):

    class Meta:
        model = Object
        fields = '__all__'
        labels = {
            "organization": "Tashkilot nomi",
            "object_type": "Turi",
            "name": "Ob'yekt nomi",
            "region": "Joylashgan viloyati",
            "address": "Obyekt manzili",
            "latitude": "Kenglik (широта)",
            "longitude": "Uzunlik (долгота)",
        }


'''class ObjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'


    class Meta:
        model = Object
        fields = '__all__'
        labels = {
            "organization": "Tashkilot nomi",
            "object_type": "Turi",
            "name": "Ob'yekt nomi",
            "region": "Joylashgan viloyati",
            "address": "Obyekt manzili",
            "latitude": "Kenglik (широта)",
            "longitude": "Uzunlik (долгота)",
        }'''


class MeterForm(forms.ModelForm):

    class Meta:
        model = Meter
        fields = ['meter_id',
                  'organization',
                  'name',
                  'diameter',
                  'flow_meter_type',
                  'flow_meter_serial_number',
                  'flow_meter_year',
                  'owner',
                  'contractor',
                  'comment'
                  ]
        labels = {
            "meter_id": "ID raqami",
            "organization": "Tashkilot nomi",
            "name": "O'lchov tarmog'i nomi",
            "diameter": "Diameter",
            "flow_meter_type": "EGHU turi",
            "flow_meter_serial_number ": "Zavod raqami",
            "flow_meter_year": "Ishlab chiqarilgan yili",
            "owner": "Balans saqlovchi",
            "contractor": "Shartnoma tuzgan tashkilot",
            "comment": "Izoh",
        }


class FlowMeterSertificateForm(forms.ModelForm):
    date_start = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
    )

    date_end = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
    )

    url_sertificate = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'type': 'file', 'onchange': 'loadFile(event)', 'placeholder': 'Sertifikat tanlanmagan'}),
        required=False
    )


    class Meta:
        model = FlowMeterSertificate
        fields = ['number', 'date_start', 'date_end', 'url_sertificate', 'is_active']

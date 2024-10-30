from django import forms
from .models import Volume


class RestoredVolumeForm(forms.ModelForm):

    date_start = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = Volume
        fields = ['month', 'flowmeter_volume', 'ns_0', 'ns_1', 'ns_2', 'ns_3', 'ns_4',  'ns_5',  'ns_6', 'ns_7']


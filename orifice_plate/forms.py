from django import forms
from orifice_plate.models import OrificePlate


class AddOrificePlateForm(forms.ModelForm):
    class Meta:
        model = OrificePlate
        fields = ['number', 'd20', 'outer_diameter', 'e', 'd20_calculated',
                  'p_max', 'pressure', 'p_unit', 'temperature', 'dp_max', 'dp_min', 'dp_unit',
                  'q_max', 'q_min', 'betta', 'installed_date', 'installed', 'note']
        labels = {
            "meter": "Tarmoq nomi",
            "number": "raqami",
            "d20": "EGHU turi",
            "outer_diameter": "Zavod raqami",
            "e": "Yili",
            "d20_calculated": "Kod",
            "p_max": "Sahibi",
            "pressure": "Yo'nalish",
            "p_unit": "Birligi",
            "temperature": "Mijoz",
            "note": "Izoh"
        }
        widgets = {
            'nitka': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'd20': forms.TextInput(attrs={'class': 'form-control'}),
            'outer_diameter': forms.TextInput(attrs={'class': 'form-control'}),
            'e': forms.TextInput(attrs={'class': 'form-control'}),
            'd20_calculated': forms.TextInput(attrs={'class': 'form-control'}),
            'p_max': forms.TextInput(attrs={'class': 'form-control'}),
            'pressure': forms.TextInput(attrs={'class': 'form-control'}),
            'temperature': forms.TextInput(attrs={'class': 'form-control'}),
            'dp_max': forms.TextInput(attrs={'class': 'form-control'}),
            'dp_min': forms.TextInput(attrs={'class': 'form-control'}),
            'dp_unit': forms.TextInput(attrs={'class': 'form-control'}),
            'q_max': forms.TextInput(attrs={'class': 'form-control'}),
            'q_min': forms.TextInput(attrs={'class': 'form-control'}),
            'betta': forms.TextInput(attrs={'class': 'form-control'}),
            'installed_date': forms.TextInput(attrs={'class': 'form-control'}),
            'installed': forms.TextInput(attrs={'class': 'form-control'}),
        }
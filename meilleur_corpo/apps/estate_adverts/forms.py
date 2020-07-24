from django import forms

from meilleur_corpo.models import EstateAdverts

class EstateAdvertsSearchForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(EstateAdvertsSearchForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control' if field_name != 'elevator' else 'custom-control-input'

    dept_code = forms.CharField(required=False)
    zip_code = forms.CharField(required=False)
    city = forms.CharField(required=False)
    heating_mode = forms.ChoiceField(required=False, choices=EstateAdverts.HEATING_MODE_CHOICES)
    elevator = forms.BooleanField(required=False)

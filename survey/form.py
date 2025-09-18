from django import forms
from .models import QuestionnaireResponse

WOMAC_CHOICES = [(i, str(i)) for i in range(5)]  # 0–4 scale

class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = QuestionnaireResponse
        fields = [
            "name", "age", "sex", "phone", 
            "had_tkr", "tkr_date", "radiograph",
             "WOMAC", "VAS", "satisfaction", "ambulation"]   # ✅ ensures demographics + WOMAC + VAS + Satisfaction + Ambulation all show up
        widgets = {
            # Demographics
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'min': 0, 'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-select'}),
            "tkr_date": forms.DateInput(attrs={"type": "date"}),

            # Example WOMAC Pain
            'womac_pain_walking': forms.RadioSelect(choices=WOMAC_CHOICES),
            'womac_pain_stairs': forms.RadioSelect(choices=WOMAC_CHOICES),
            # ... (continue with other WOMAC items as we had before) ...

            # VAS
            'vas_pain': forms.NumberInput(attrs={'min': 0, 'max': 10, 'class': 'form-control'}),

            # Satisfaction
            'satisfaction': forms.RadioSelect(choices=[(i, str(i)) for i in range(1, 6)]),

            # Ambulation
            'ambulation': forms.Select(attrs={'class': 'form-select'}),
        }



from django import forms
from .models import QuestionnaireResponse

WOMAC_CHOICES = [(i, str(i)) for i in range(5)]  # 0–4 scale

class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = QuestionnaireResponse
           fields = [
            "name", "age", "sex", "phone",
            "had_tkr", "tkr_date", "radiograph",
            "vas_pain",
            "womac_pain_walking", "womac_pain_stairs", "womac_pain_nocturnal",
            "womac_pain_rest", "womac_pain_weight_bearing",
            "womac_stiffness_morning", "womac_stiffness_later_day",
            "womac_function_descend_stairs", "womac_function_ascend_stairs",
            "womac_function_rising_sitting", "womac_function_standing",
            "womac_function_bending_floor", "womac_function_walking_flat",
            "womac_function_in_out_car", "womac_function_shopping",
            "womac_function_putting_socks", "womac_function_lying_bed",
            "womac_function_taking_socks_off", "womac_function_rising_bed",
            "womac_function_in_out_bath", "womac_function_sitting",
            "womac_function_on_off_toilet", "womac_function_heavy_domestic",
            "womac_function_light_domestic",
            "satisfaction", "ambulation"
        ]  # ✅ ensures demographics + WOMAC + VAS + Satisfaction + Ambulation all show up
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



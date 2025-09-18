from django.db import models


class QuestionnaireResponse(models.Model):
    SEX_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    ]

    AMBULATION_CHOICES = [
        ("independent", "Independent"),
        ("cane", "Cane"),
        ("walker", "Walker"),
        ("wheelchair", "Wheelchair"),
    ]

    # Demographics
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    phone = models.CharField(max_length=20, blank=True, null=True)  # ✅ New

    # Surgery history
    had_tkr = models.BooleanField(default=False)                   # ✅ New
    tkr_date = models.DateField(blank=True, null=True)             # ✅ New

    # Radiograph upload
    radiograph = models.FileField(upload_to="radiographs/", blank=True, null=True)  # ✅ New

    # VAS Pain
    vas_pain = models.PositiveIntegerField()

    # WOMAC Pain (0–4 each, total 0–20)
    womac_pain_walking = models.IntegerField(default=0)
    womac_pain_stairs = models.IntegerField(default=0)
    womac_pain_nocturnal = models.IntegerField(default=0)
    womac_pain_rest = models.IntegerField(default=0)
    womac_pain_weight_bearing = models.IntegerField(default=0)

    # WOMAC Stiffness (0–4 each, total 0–8)
    womac_stiffness_morning = models.IntegerField(default=0)
    womac_stiffness_later_day = models.IntegerField(default=0)

    # WOMAC Function (0–4 each, total 0–68)
    womac_function_descend_stairs = models.IntegerField(default=0)
    womac_function_ascend_stairs = models.IntegerField(default=0)
    womac_function_rising_sitting = models.IntegerField(default=0)
    womac_function_standing = models.IntegerField(default=0)
    womac_function_bending_floor = models.IntegerField(default=0)
    womac_function_walking_flat = models.IntegerField(default=0)
    womac_function_in_out_car = models.IntegerField(default=0)
    womac_function_shopping = models.IntegerField(default=0)
    womac_function_putting_socks = models.IntegerField(default=0)
    womac_function_lying_bed = models.IntegerField(default=0)
    womac_function_taking_socks_off = models.IntegerField(default=0)
    womac_function_rising_bed = models.IntegerField(default=0)
    womac_function_in_out_bath = models.IntegerField(default=0)
    womac_function_sitting = models.IntegerField(default=0)
    womac_function_on_off_toilet = models.IntegerField(default=0)
    womac_function_heavy_domestic = models.IntegerField(default=0)
    womac_function_light_domestic = models.IntegerField(default=0)

    # Satisfaction (1–5 scale)
    satisfaction = models.IntegerField(default=3)

    # Ambulation status
    ambulation = models.CharField(max_length=20, choices=AMBULATION_CHOICES)

    # Date of entry
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.age} y/o)"


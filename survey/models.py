from django.db import models

class QuestionnaireResponse(models.Model):
    # Demographics
    name = models.CharField(max_length=100, default="Unknown")
    age = models.IntegerField(default=0)
    sex = models.CharField(
        max_length=10,
        choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
        default='male'
    )
    phone = models.CharField(max_length=15, blank=True, null=True)  # 📞 phone number

    # New surgery info
    had_tkr = models.BooleanField(default=False)   # total knee replacement
    tkr_date = models.DateField(blank=True, null=True)

    # Radiograph upload
    radiograph = models.FileField(upload_to="radiographs/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    # WOMAC Pain (5 items)
    womac_pain_walking = models.IntegerField(default=0)
    womac_pain_stairs = models.IntegerField(default=0)
    womac_pain_nocturnal = models.IntegerField(default=0)
    womac_pain_rest = models.IntegerField(default=0)
    womac_pain_weight_bearing = models.IntegerField(default=0)

    # WOMAC Stiffness (2 items)
    womac_stiffness_morning = models.IntegerField(default=0)
    womac_stiffness_later_day = models.IntegerField(default=0)

    # WOMAC Physical Function (17 items)
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

    # Other measures
    vas_pain = models.IntegerField(default=0)
    satisfaction = models.IntegerField(default=0)
    ambulation = models.CharField(
        max_length=20,
        choices=[
            ('independent', 'Independent'),
            ('cane', 'Uses Cane'),
            ('walker', 'Uses Walker'),
            ('wheelchair', 'Wheelchair-bound'),
        ],
        default='independent'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.age} yrs) - {self.created_at.date()}"








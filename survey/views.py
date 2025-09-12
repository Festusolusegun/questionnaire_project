from django.shortcuts import render, redirect
from .form import QuestionnaireForm
from .models import QuestionnaireResponse
from django.contrib.auth.decorators import login_required, user_passes_test



def questionnaire_view(request):
    if request.method == "POST":
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = QuestionnaireForm()
    return render(request, "survey/questionnaire.html", {"form": form})


def thank_you_view(request):
    return render(request, "survey/thank_you.html")


# Allow only superusers to view results
@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_superuser
def results_view(request):
    responses = QuestionnaireResponse.objects.all()

    processed = []
    for r in responses:
        pain_total = (
            (r.womac_pain_walking or 0) +
            (r.womac_pain_stairs or 0) +
            (r.womac_pain_nocturnal or 0) +
            (r.womac_pain_rest or 0) +
            (r.womac_pain_weight_bearing or 0)
        )
        stiffness_total = (
            (r.womac_stiffness_morning or 0) +
            (r.womac_stiffness_later_day or 0)
        )
        function_total = (
            (r.womac_function_descend_stairs or 0) +
            (r.womac_function_ascend_stairs or 0) +
            (r.womac_function_rising_sitting or 0) +
            (r.womac_function_standing or 0) +
            (r.womac_function_bending_floor or 0) +
            (r.womac_function_walking_flat or 0) +
            (r.womac_function_in_out_car or 0) +
            (r.womac_function_shopping or 0) +
            (r.womac_function_putting_socks or 0) +
            (r.womac_function_lying_bed or 0) +
            (r.womac_function_taking_socks_off or 0) +
            (r.womac_function_rising_bed or 0) +
            (r.womac_function_in_out_bath or 0) +
            (r.womac_function_sitting or 0) +
            (r.womac_function_on_off_toilet or 0) +
            (r.womac_function_heavy_domestic or 0) +
            (r.womac_function_light_domestic or 0)
        )
        total_womac = pain_total + stiffness_total + function_total

        processed.append({
            "id": r.id,
            "name": r.name,
            "age": r.age,
            "sex": r.sex,
            "created_at": r.created_at,
            "pain_total": pain_total,
            "stiffness_total": stiffness_total,
            "function_total": function_total,
            "total_womac": total_womac,
            "vas_pain": r.vas_pain,
            "satisfaction": r.satisfaction,
            "ambulation": r.get_ambulation_display(),
        })

    return render(request, "survey/results.html", {"responses": processed})


def export_responses_csv(request):
    responses = QuestionnaireResponse.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="responses.csv"'

    writer = csv.writer(response)
    writer.writerow([
        "ID", "Name", "Age", "Sex", "Date",
        "WOMAC Pain Total", "WOMAC Stiffness Total", "WOMAC Function Total",
        "VAS Pain", "Satisfaction", "Ambulation"
    ])

    for r in responses:
        pain_total = (
            r.womac_pain_walking + r.womac_pain_stairs + r.womac_pain_nocturnal +
            r.womac_pain_rest + r.womac_pain_weight_bearing
        )
        stiffness_total = r.womac_stiffness_morning + r.womac_stiffness_later_day
        function_total = (
            r.womac_function_descend_stairs + r.womac_function_ascend_stairs +
            r.womac_function_rising_sitting + r.womac_function_standing +
            r.womac_function_bending_floor + r.womac_function_walking_flat +
            r.womac_function_in_out_car + r.womac_function_shopping +
            r.womac_function_putting_socks + r.womac_function_lying_bed +
            r.womac_function_taking_socks_off + r.womac_function_rising_bed +
            r.womac_function_in_out_bath + r.womac_function_sitting +
            r.womac_function_on_off_toilet + r.womac_function_heavy_domestic +
            r.womac_function_light_domestic
        )

        writer.writerow([
            r.id, r.name, r.age, r.sex, r.created_at.strftime("%Y-%m-%d %H:%M"),
            pain_total, stiffness_total, function_total,
            r.vas_pain, r.satisfaction, r.get_ambulation_display()
        ])

    return response




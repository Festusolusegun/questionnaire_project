from django.shortcuts import render, redirect
from .form import QuestionnaireForm
from .models import QuestionnaireResponse

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

def results_view(request):
    responses = QuestionnaireResponse.objects.all()
    return render(request, "survey/results.html", {"responses": responses})


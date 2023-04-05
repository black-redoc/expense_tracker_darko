from django.shortcuts import render


def index(request):
    context = {"expenses": [{"id": 1, "concept": "concept_1", "amount": 100_000}]}
    return render(request, "expenses/index.html", context=context)

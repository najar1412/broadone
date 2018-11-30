from django.shortcuts import render


def index(request):
    context = {
        'test': {'test': 'ing'}
    }

    return render(request, "slider/index.html", context)
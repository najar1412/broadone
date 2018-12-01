from django.shortcuts import render


def index(request):
    context = {
        'test': {'test': 'ing'}
    }

    return render(request, "map/index.html", context)
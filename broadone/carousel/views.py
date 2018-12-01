from django.shortcuts import render


def index(request):
    context = {
        'test': {'test': 'ing'}
    }

    return render(request, "carousel/index.html", context)
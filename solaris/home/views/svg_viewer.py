from django.shortcuts import render


def svg_viewer(request):
    context = {}

    return render(
        request,
        "home/svg_viewer.html",
        context,
    )

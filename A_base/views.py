from django.shortcuts import render

def base_view(request):
    context = {}
    template = "A_base/base.html"
    return render(
        request,
        template,
        context
    )

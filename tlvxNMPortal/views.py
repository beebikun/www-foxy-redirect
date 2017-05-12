from django.http import HttpResponse
from django.shortcuts import redirect as httpRedirect
from django.template import RequestContext, loader


def home(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))


def redirect(request, page):
    return httpRedirect('home')

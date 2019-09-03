from django.http.response import HttpResponse
from pprint import pprint

# Create your views here.
from django.urls.base import reverse


def index(request):
    info = get_diagnostic_info(request=request)
    pprint(info)

    return HttpResponse("Diagnostics were printed to your console")


def dummy_url(request):
    return HttpResponse("Dummy url")


def get_diagnostic_info(request):
    return {

        'request.META': request.META,
        'request.get_host()': request.get_host(),
        'request.build_absolute_uri()': request.build_absolute_uri(reverse('dummy_url'))
    }

from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

# HTTP REQUEST #


def my_view(request):
    return HttpResponse('Uma linda string')
    # return HTTP Response #


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sobre/', my_view),
]

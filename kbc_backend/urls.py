from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Simple home view
def home(request):
    return HttpResponse("Welcome to KAMS (KBC Advertising Management System)")

urlpatterns = [
    path('admin/', admin.site.urls),   # Django admin
    path('', home, name='home'),       # Home page
    path('kams/', include('kams.urls')),  # Connect kams app
]



from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# A simple view for the root URL
def home_view(request):
    return HttpResponse("Welcome to the Auth System API!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),  # Your app's authentication endpoints
    path('', home_view, name='home'),         # Root URL
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('doctor_finder.urls')),
    path('api/auth/', include('rest_framework.urls')),
    path('third-party/', include('third_party_apis.urls')),
]

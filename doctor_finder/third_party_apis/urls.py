from django.urls import path
from .views import (
    WeatherAPIView, GeocodingAPIView, GitHubAPIView, 
    TwitterAPIView, RESTCountriesAPIView, SendEmailAPIView, 
    SendSMSAPIView, StripePaymentAPIView
)

urlpatterns = [
    path('weather/<str:city>/', WeatherAPIView.as_view(), name='weather'),
    path('geocode/', GeocodingAPIView.as_view(), name='geocode'),
    path('github/<str:username>/', GitHubAPIView.as_view(), name='github'),
    path('twitter/<str:username>/', TwitterAPIView.as_view(), name='twitter'),
    path('countries/<str:country>/', RESTCountriesAPIView.as_view(), name='countries'),
    path('send-email/', SendEmailAPIView.as_view(), name='send_email'),
    path('send-sms/', SendSMSAPIView.as_view(), name='send_sms'),
    path('payment/', StripePaymentAPIView.as_view(), name='payment'),
]

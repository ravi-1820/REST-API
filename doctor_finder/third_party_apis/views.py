import requests
import stripe
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from twilio.rest import Client
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

class WeatherAPIView(APIView):
    def get(self, request, city):
        # OpenWeatherMap API (Practical 14)
        api_key = "dummy_api_key"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        # response = requests.get(url).json()
        return Response({"city": city, "weather": "sunny", "temp": "25C", "note": "Requires valid API key to fetch actual data."})

class GeocodingAPIView(APIView):
    def get(self, request):
        # Google Maps Geocoding API (Practical 15, 22)
        address = request.query_params.get('address', 'New York')
        return Response({"address": address, "lat": 40.7128, "lng": -74.0060, "note": "Mocked coordinates"})

class GitHubAPIView(APIView):
    def get(self, request, username):
        # GitHub API Integration (Practical 16)
        url = f"https://api.github.com/users/{username}/repos"
        # response = requests.get(url).json()
        return Response({"user": username, "repos": ["repo1", "repo2"], "note": "Mocked GitHub data"})

class TwitterAPIView(APIView):
    def get(self, request, username):
        # Twitter API Integration (Practical 17)
        return Response({"user": username, "tweets": ["Hello World", "Django is great!"], "note": "Mocked Twitter data"})

class RESTCountriesAPIView(APIView):
    def get(self, request, country):
        # REST Countries API (Practical 18)
        url = f"https://restcountries.com/v3.1/name/{country}"
        try:
            response = requests.get(url).json()
            return Response(response)
        except:
            return Response({"error": "Failed to fetch data"})

class SendEmailAPIView(APIView):
    def post(self, request):
        # Email Sending API (SendGrid) (Practical 19)
        return Response({"status": "Email sent securely", "note": "SendGrid API mocked."})

class SendSMSAPIView(APIView):
    def post(self, request):
        # SMS Sending API (Twilio) (Practical 20)
        return Response({"status": "OTP sent securely", "note": "Twilio API mocked."})

class StripePaymentAPIView(APIView):
    def post(self, request):
        # Payment Integration (Stripe) (Practical 21)
        return Response({"status": "Payment processed", "amount": 5000, "note": "Stripe API mocked."})

from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .services import search_movies, get_movie_details
from .models import Booking
from .serializers import BookingSerializer, UserSerializer
import requests
from django.conf import settings

# Create your views here.


# jwt
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Hardcoded popular movies
POPULAR_MOVIES = ["Inception", "Avengers", "Titanic", "Matrix", "Interstellar"]

class PopularMoviesView(APIView):
    permission_classes = [] 

    def get(self, request):
        movies = []
        for title in POPULAR_MOVIES:
            try:
                res = requests.get("https://www.omdbapi.com/", params={
                    "apikey": settings.OMDB_API_KEY,
                    "s": title
                }, timeout=5)
                data = res.json()
                if data.get("Search"):
                    movies.extend(data["Search"])
            except Exception as e:
                continue  
        return Response(movies)


class BookingCreateView(generics.CreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BookingListView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

class MovieSearchView(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        title = request.query_params.get("q")
        if not title:
            return Response({"error": "Movie title required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            data = search_movies(title)
            return Response(data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class MovieDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, imdb_id):
        try:
            data = get_movie_details(imdb_id)
            return Response(data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

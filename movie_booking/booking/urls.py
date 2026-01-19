from django.urls import path
from .views import RegisterView, BookingCreateView, BookingListView, MovieSearchView, MovieDetailView,PopularMoviesView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('register/', RegisterView.as_view(), name='user_register'),
    path('movies/popular/', PopularMoviesView.as_view(), name='popular_movies'),
    path('book/', BookingCreateView.as_view(), name='book_ticket'),
    path('bookings/', BookingListView.as_view(), name='list_bookings'),


    path('movies/search/', MovieSearchView.as_view(), name='movie_search'),
    path('movies/<str:imdb_id>/', MovieDetailView.as_view(), name='movie_detail'),
]

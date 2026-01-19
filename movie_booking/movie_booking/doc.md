Movie Booking API Documentation
Base URL
http://127.0.0.1:8000/

1️⃣ Register User

Endpoint: /register/
Method: POST
Body (JSON):

{
  "username": "testuser",
  "email": "test@test.com",
  "password": "123456"
}


Response:

{
  "id": 1,
  "username": "testuser",
  "email": "test@test.com"
}

2️⃣ JWT Token (Login)

Endpoint: /token/
Method: POST
Body (JSON):

{
  "username": "testuser",
  "password": "123456"
}


Response:

{
  "access": "<JWT_ACCESS_TOKEN>",
  "refresh": "<JWT_REFRESH_TOKEN>"
}


Copy access token for Authorization header.

3️⃣ Get Popular Movies

Endpoint: /movies/popular/
Method: GET
Headers: None (public)
Response Example:

[
  {"Title": "Inception", "Year": "2010", "imdbID": "tt1375666", "Type": "movie"},
  {"Title": "Avengers", "Year": "2012", "imdbID": "tt0848228", "Type": "movie"}
]

4️⃣ Search Movies

Endpoint: /movies/search/?q=<movie_name>
Method: GET
Headers: None (public)
Example: /movies/search/?q=Inception

5️⃣ Movie Details (JWT Protected)

Endpoint: /movies/<imdb_id>/
Method: GET
Headers:

Authorization: Bearer <JWT_ACCESS_TOKEN>


Example Response:

{
  "Title": "Inception",
  "Year": "2010",
  "Genre": "Action, Sci-Fi",
  "Director": "Christopher Nolan",
  "Actors": "Leonardo DiCaprio, Joseph Gordon-Levitt",
  "Plot": "A thief who steals corporate secrets..."
}

6️⃣ Book Tickets (JWT Protected)

Endpoint: /book/
Method: POST
Headers:

Authorization: Bearer <JWT_ACCESS_TOKEN>
Content-Type: application/json


Body (JSON):

{
  "movie_id": "tt1375666",
  "movie_title": "Inception",
  "show_time": "7:00 PM",
  "seats": 3
}


Response (with service fee & GST):

{
  "id": 1,
  "user": 1,
  "movie_id": "tt1375666",
  "movie_title": "Inception",
  "show_time": "7:00 PM",
  "seats": 3,
  "base_price": 450,
  "service_fee": 30,
  "tax": 81.0,
  "total_price": 561.0,
  "booking_date": "2026-01-19T12:34:56.789Z"
}


Service Fee Logic:

Seats ≤ 2 → ₹15

Seats 3–4 → ₹30

Seats > 4 → ₹30 + ₹5 per extra seat

GST: 18% of base price

7️⃣ List User Bookings (JWT Protected)

Endpoint: /bookings/
Method: GET
Headers:

Authorization: Bearer <JWT_ACCESS_TOKEN>


Response Example:

[
  {
    "id": 1,
    "movie_id": "tt1375666",
    "movie_title": "Inception",
    "show_time": "7:00 PM",
    "seats": 3,
    "base_price": 450,
    "service_fee": 30,
    "tax": 81.0,
    "total_price": 561.0,
    "booking_date": "2026-01-19T12:34:56.789Z"
  }
]

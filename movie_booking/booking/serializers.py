from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Booking

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['user', 'booking_date', 'base_price', 'service_fee', 'tax', 'total_price']

    def create(self, validated_data):
        seats = validated_data.get('seats', 1)
        base_price_per_seat = 150 
        base_price = seats * base_price_per_seat


        if seats <= 2:
            service_fee = 15
        elif seats <= 4:
            service_fee = 30
        else:
            service_fee = 30 + (seats - 4) * 5


        tax = base_price * 0.18

        total_price = base_price + service_fee + tax

        validated_data['base_price'] = base_price
        validated_data['service_fee'] = service_fee
        validated_data['tax'] = tax
        validated_data['total_price'] = total_price

        return super().create(validated_data)
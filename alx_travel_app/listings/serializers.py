from rest_framework import serializers
from .models import Listing, Booking

# Serializer for Listing model
class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        # Fields to include in API representation
        fields = ['id', 'title', 'description', 'price_per_night', 'location', 'created_at']


# Serializer for Booking model
class BookingSerializer(serializers.ModelSerializer):
    # Nested serializer to show listing details inside booking
    listing = ListingSerializer(read_only=True)
    
    class Meta:
        model = Booking
        fields = ['id', 'listing', 'user', 'check_in', 'check_out', 'guests', 'created_at']


from . models import Lodge, Price, Special_price, Photos,Availability
from rest_framework import serializers

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = '__all__'

class SpecialPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Special_price
        fields = '__all__'

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'

class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = ['name']

class LodgeSerializer(serializers.ModelSerializer):
    photo_gallery_set =  GallerySerializer(many=True)
    special_price_set =  SpecialPriceSerializer(many=True)
    price_set =  PriceSerializer(many=True)
    availability_set =  AvailabilitySerializer(many=True)
    class Meta:
        model = Lodge
        fields = '__all__'
        depth = 1
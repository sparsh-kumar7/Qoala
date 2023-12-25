from rest_framework import serializers
from .models import *

class OCRResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = OCRResult
        fields = '__all__'
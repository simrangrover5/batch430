from rest_framework import serializers
from .models import Blogadd

class Showapi(serializers.ModelSerializer):


    class Meta:
        model  = Blogadd
        fields = ['blog','title']
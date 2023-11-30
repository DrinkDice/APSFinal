from rest_framework import serializers

from .models import Filmes

class FilmesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filmes
        fields = '__all__' #['nome_filme']


class LoginSerializer(serializers.Serializer):
    user = serializers.CurrentUserDefault()
    password = serializers.CharField()
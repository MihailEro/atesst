
from rest_framework import serializers
from suppliers.models import Participant, Contacts, Product
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ParticipantSerializer(serializers.ModelSerializer):
    contacts = ContactsSerializer(read_only=True)
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Participant
        fields = '__all__'
        read_only_fields = ['debt']


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Добавление пользовательских полей в токен
        token['username'] = user.username
        token['email'] = user.email

        return token

from rest_framework import serializers
from .models import Modality, Address, Contact, Institution


class ModalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Modality
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = '__all__'

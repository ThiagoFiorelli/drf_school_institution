from rest_framework import viewsets
from .serializers import ModalitySerializer, ContactSerializer, AddressSerializer, InstitutionSerializer
from .models import Modality, Address, Contact, Institution


class ModalityViewSet(viewsets.ModelViewSet):
    queryset = Modality.objects.all().order_by('name')
    serializer_class = ModalitySerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all().order_by('address_name')
    serializer_class = AddressSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('email')
    serializer_class = ContactSerializer


class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all().order_by('name')
    serializer_class = InstitutionSerializer

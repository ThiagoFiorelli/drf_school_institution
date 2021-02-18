from django.db import models


class Modality(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f'{self.name}'


class Address(models.Model):
    address_name = models.CharField(max_length=100, null=False, blank=False)
    city = models.CharField(max_length=100, null=False, blank=False)
    state = models.CharField(max_length=100, null=False, blank=False)
    country = models.CharField(max_length=100, null=False, blank=False)
    postal_code = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
     return f'{self.address_name}'


class Contact(models.Model):
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    site = models.CharField(max_length=10)

    def __str__(self):
     return f'{self.email}'


class Institution(models.Model):
    name = models.CharField(max_length=150, unique=True, null=False, blank=False)
    initials = models.CharField(max_length=20)
    description = models.TextField() 
    cnpj = models.CharField(max_length=14, unique=True, null=False, blank=False)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)
    modality = models.ManyToManyField(Modality)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
     return f'{self.name}'
     
from django.contrib import admin

from .models import Modality, Contact, Address, Institution


class ModalityAdmin(admin.ModelAdmin):
    list_display = ('name', )


class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'site')


class AddressAdmin(admin.ModelAdmin):
    list_display = ('address_name', 'city', 'state', 'country', 'postal_code')


class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'initials',
                    'get_modalities',
                    'description',
                    'address',
                    'contact',
                    'cnpj',
                    'created_at',
                    'updated_at')
    
    def get_modalities(self, obj):
        return ", ".join([str(p) for p in obj.modality.all()])


admin.site.register(Modality, ModalityAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Institution, InstitutionAdmin)

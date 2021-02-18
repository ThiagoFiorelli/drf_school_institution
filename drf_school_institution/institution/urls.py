from django.urls import include, path
from rest_framework import routers
from .views import ModalityViewSet, ContactViewSet, AddressViewSet, InstitutionViewSet

router = routers.DefaultRouter()
router.register(r'modalities',ModalityViewSet, basename="modalities")
router.register(r'contacts', ContactViewSet, basename="contacts")
router.register(r'addresses', AddressViewSet, basename="addresses")
router.register(r'institutions', InstitutionViewSet, basename="institutions")

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include(
        'rest_framework.urls', namespace='rest_framework'))
]

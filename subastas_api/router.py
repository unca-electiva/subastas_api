from rest_framework import routers
from apps.anuncio import api

# Initializar el router de DRF solo una vez
router = routers.DefaultRouter()

# Registrar un ViewSet
router.register(prefix='categoria', viewset=api.CategoriaViewSet)

urlpatterns = [
]

urlpatterns += router.urls

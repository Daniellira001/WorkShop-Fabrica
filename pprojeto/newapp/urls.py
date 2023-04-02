from rest_framework import routers
from newapp.views import newprojetoViewSet

router = routers.DefaultRouter()
router.register(r'', newprojetoViewSet)

urlpatterns = router.urls
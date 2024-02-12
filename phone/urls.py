from rest_framework import routers

from .views import PhoneViewSet

router = routers.DefaultRouter()
router.register("", PhoneViewSet)

urlpatterns = router.urls


app_name = "phone"

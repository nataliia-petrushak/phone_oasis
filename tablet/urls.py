from rest_framework import routers

from .views import TabletViewSet

router = routers.DefaultRouter()
router.register("", TabletViewSet)

urlpatterns = router.urls


app_name = "tablet"

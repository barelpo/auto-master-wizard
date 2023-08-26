from rest_framework.routers import DefaultRouter

from auto_master_wizard_app.contents.views import ContentViewSet

router = DefaultRouter()
router.register('', ContentViewSet)

urlpatterns = router.urls


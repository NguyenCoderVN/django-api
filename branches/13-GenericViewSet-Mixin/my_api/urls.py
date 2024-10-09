from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter(trailing_slash=False)
router.register('menu-items', views.MenuItemsView, basename='menu-items')
urlpatterns = router.urls

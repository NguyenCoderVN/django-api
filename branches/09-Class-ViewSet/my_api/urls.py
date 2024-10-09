from rest_framework.routers import SimpleRouter
from . import views
router = SimpleRouter(trailing_slash=False)
router.register('menu-items', views.MenuItemsView, basename='menu-items')
urlpatterns = router.urls
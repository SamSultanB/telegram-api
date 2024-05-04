from rest_framework import routers
from .views import UsersModelViewSet

router = routers.DefaultRouter()

router.register(
    "", viewset=UsersModelViewSet, basename="users"
)

urlpatterns = [

]

urlpatterns += router.urls
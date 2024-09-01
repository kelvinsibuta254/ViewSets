# Routers
## allow url configuration to be detected
## automatically generates urls for the viewset

from .views import MemberViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
"""router returns a list of urlpatterns"""

router.register("members", MemberViewSet, basename="member")

urlpatterns = router.urls


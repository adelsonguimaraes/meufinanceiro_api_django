from email.mime import base
from rest_framework.routers import DefaultRouter
from transaction import viewsets

router = DefaultRouter()
router.register("user", viewsets.UserViewset, basename="user")
router.register("transaction", viewsets.TransactionViewset, basename="transaction")
urlpatterns = router.urls

from rest_framework.routers import DefaultRouter
from transactions import viewsets

router = DefaultRouter()
router.register(r'credit_card', viewsets.CreditCardModelViewSet)
router.register(r'transaction', viewsets.TransactionModelViewSet)
router.register(r'portion', viewsets.TransactionPortionModelViewSet)
urlpatterns = router.urls

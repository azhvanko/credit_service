from rest_framework.routers import SimpleRouter

from .views import (
    ContractView,
    GoodsView,
    LoanApplicationView,
    LoanApplicationGoodsView,
    ManufacturerView,
)


router = SimpleRouter()

router.register(r'contract', ContractView, basename='contract')
router.register(r'goods', GoodsView, basename='goods')
router.register(r'loan_application', LoanApplicationView, basename='loan_application')
router.register(r'loan_application_goods', LoanApplicationGoodsView, basename='loan_application_goods')
router.register(r'manufacturer', ManufacturerView, basename='manufacturer')

urlpatterns = router.urls

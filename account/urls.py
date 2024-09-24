from django.urls import path,include
from .views import RegView,UsersInfo,loginVIew,logOutview

from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('', UsersInfo)


urlpatterns = [
    path("", include(router.urls)),
    path('register/', RegView.as_view(), name="register"),
    path('v1/login/', loginVIew.as_view(), name="login"),
    path('v1/logout/', logOutview.as_view(), name="logout"),
]

from django.urls import path, include
from users_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', views.usersignup,name='signup'),

    ]

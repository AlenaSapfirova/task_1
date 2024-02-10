from django.urls import path
from rest_framework.authtoken import views
from .views import PostAPIView, PostDetailAPIView, RegisterApiView

urlpatterns = [
    path('posts/', PostAPIView.as_view()),
    path('posts/<int:id>/', PostDetailAPIView.as_view()),
    path('users/register/', RegisterApiView.as_view()),
    path('api-token-auth/', views.obtain_auth_token)

]

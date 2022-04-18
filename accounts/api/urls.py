from django.urls import path
from accounts.api.views import ProfileDetailAPIView

urlpatterns = [
    path('profile/', ProfileDetailAPIView.as_view(), name='profile-detail')
]

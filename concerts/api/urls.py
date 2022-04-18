from django.urls import path

from .views import BandRUDAPIView, BandListCreateAPIView, EventRUDAPIView, EventListCreateView, EventJoinAPIView


urlpatterns = [
    path("concerts/", EventListCreateView.as_view(), name='event-list'),
    path("concert/<slug:slug>/", EventRUDAPIView.as_view(), name='event-detail'),
    path("concerts/<slug:slug>/join/", EventJoinAPIView.as_view(), name="event-join"),
    path("bands/", BandListCreateAPIView.as_view(), name="band-list"),
    path("bands/<int:pk>/", BandRUDAPIView.as_view(), name="band-detail")
]

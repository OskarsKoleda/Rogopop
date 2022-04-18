from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import status

from django.db.models import Q

from concerts.models import Event, Band
from concerts.api.permissions import IsAuthorOrAdminOrReadOnly
from concerts.api.serializers import BandSerializer, EventSerializer

import time


def get_bands(bands_string):
    band_list = []
    if bands_string:
        band_list_name = bands_string.split(',')
        for band_name in band_list_name:
            band = Band.objects.get(name=band_name)
            band_list.append(band)
    return band_list


class EventJoinAPIView(APIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, slug):
        event = get_object_or_404(Event, slug=slug)
        event.visitors_participants.add(request.user.profile)
        event.save()
        serializer_context = {"request": request}
        serializer = self.serializer_class(event, context=serializer_context)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, slug):
        event = get_object_or_404(Event, slug=slug)
        event.visitors_participants.remove(request.user.profile)
        event.save()
        serializer_context = {"request": request}
        serializer = self.serializer_class(event, context=serializer_context)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EventRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all().order_by('-created_at')
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrAdminOrReadOnly]
    lookup_field = "slug"

    def perform_update(self, serializer):
        print("perform_update EventRUDAPIView: ")
        string_bands = self.request.data.get('bandsParticipated', None)
        band_list = get_bands(string_bands)
        serializer.save(created_by=self.request.user.profile,
                        bands_participated=band_list)
        return super().perform_update(serializer)

    def update(self, request, *args, **kwargs):
        event = Event.objects.get(slug=kwargs['slug'])
        if request.FILES.get('poster', False):
            if event.poster.name != 'concerts/no_poster.jpg':
                event.poster.delete(save=False)
        return super().update(request, *args, **kwargs)


class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all().order_by("title")
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    # search_fields = ['title', 'city']

    def get_queryset(self):
        queryset_list = Event.objects.all().order_by('title')
        query = self.request.GET.get('search')
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query) | Q(city__icontains=query) |
                Q(bands_participated__name__icontains=query)).distinct()
        return queryset_list

    # def list(self, request, *args, **kwargs):
    #     time.sleep(0.5)
    #     return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        string_bands = self.request.data.get('bandsParticipated', None)
        band_list = get_bands(string_bands)
        serializer.save(created_by=self.request.user.profile,
                        bands_participated=band_list)


class BandRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Band.objects.all().order_by('-created_at')
    serializer_class = BandSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrAdminOrReadOnly]

    def get_object(self, pk):
        band = get_object_or_404(Band, pk=pk)
        return band

    def get(self, request, pk):
        band = self.get_object(pk)
        serializer = BandSerializer(band, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        band = self.get_object(pk)
        serializer = BandSerializer(band, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        band = self.get_object(pk)
        band.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BandListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = BandSerializer
    queryset = Band.objects.all().order_by('-created_at')
    permission_classes = [IsAuthenticated]

    def get(self, request):
        bands = Band.objects.all()
        serializer = BandSerializer(
            bands,
            many=True,
            context={'request': request})
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user.profile)

    # def get_queryset(self):
    #     queryset_list = Event.objects.all()
    #     query = self.request.GET.get('search')
    #     if query:
    #         queryset_list = queryset_list.filter(
    #             Q(title__icontains=query) | Q(city__icontains=query)
    #         )
    #     return queryset_list

    # parser_classes = [MultiPartParser, FormParser]

    # def post(self, request, format=None):
    #     serializer = EventSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     else:
    #         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    # def get_object(self, slug):
    #     event = get_object_or_404(Event, slug=slug)
    #     return event

    # def get(self, request, slug):
    #     print("SLUG: ", slug)
    #     event = self.get_object(slug)
    #     serializer = EventSerializer(event, context={'request': request})
    #     return Response(serializer.data)

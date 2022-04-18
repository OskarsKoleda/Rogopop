from rest_framework import generics
from accounts.api.serializers import ProfileSerializer
from rest_framework.response import Response
import time


class ProfileDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer

    def get(self, request):
        profile = request.user.profile
        serializer = ProfileSerializer(profile)
        # time.sleep(0.5)
        return Response(serializer.data)

from rest_framework.serializers import (SerializerMethodField,
                                        StringRelatedField,
                                        ModelSerializer,
                                        SlugField)
from concerts.models import Band, Event
import os


class BandSerializer(ModelSerializer):
    created_at = SerializerMethodField()
    events_performed = StringRelatedField(many=True)

    class Meta:
        model = Band
        exclude = ["id", "updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")


class EventSerializer(ModelSerializer):
    created_by = StringRelatedField()
    created_at = SerializerMethodField()
    slug = SlugField(read_only=True)
    user_has_participated = SerializerMethodField()
    image_name = SerializerMethodField()

    def create(self, validated_data):
        bands = validated_data.pop('bands_participated')
        event = Event.objects.create(**validated_data)
        event.bands_participated.set(bands)
        return event

    class Meta:
        model = Event
        exclude = ["id", "updated_at",
                   "visitors_participants"]
        depth = 1

    def get_image_name(self, instance):
        if instance.poster:
            return os.path.basename(instance.poster.url)
        else:
            return None

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

    def get_user_has_participated(self, instance):
        request = self.context.get("request")
        return instance.visitors_participants.filter(user=request.user).exists()

from rest_framework.serializers import (SerializerMethodField, StringRelatedField,
                                        ModelSerializer)
from django.db.models import Sum
from accounts.models import Profile


class ProfileSerializer(ModelSerializer):
    user = StringRelatedField()
    events_count = SerializerMethodField(read_only=True)
    money_spent = SerializerMethodField(read_only=True)
    is_staff = SerializerMethodField(read_only=True)

    class Meta:
        model = Profile
        exclude = ['id']

    def get_is_staff(self, instance):
        return instance.user.is_staff

    def get_events_count(self, instance):
        return instance.event_set.all().count()

    def get_money_spent(self, instance):
        return instance.event_set.all().aggregate(Sum('ticket_price'))['ticket_price__sum']

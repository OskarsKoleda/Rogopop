from django.db import models
import uuid as uuid_lib
from accounts.models import Profile
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from core.models import TimeStampModel

def upload_to(instance, filename):
    return 'concerts/{filename}'.format(filename=filename)

    
class Band(TimeStampModel):
    created_by = models.ForeignKey(
                                    Profile, 
                                    on_delete=models.CASCADE, 
                                    related_name='user_bands')

    uuid = models.UUIDField(
                            editable=False, 
                            default=uuid_lib.uuid4)
    name = models.CharField(
                            max_length=255, 
                            db_index=True, 
                            unique=True)

    # participated_in = models.ManyToManyField(Event, blank=True, related_name="bands_participated")

    def __str__(self):
        return self.name


class Event(TimeStampModel):
    created_by                                      = models.ForeignKey(
                                                                        Profile, 
                                                                        on_delete=models.CASCADE, 
                                                                        related_name='user_events')
    title                                           = models.CharField(max_length=200)
    slug                                            = models.SlugField(
                                                                        max_length=215, 
                                                                        unique=True,
                                                                        default='', 
                                                                        blank=True, 
                                                                        db_index=True)
    date                                            = models.DateField(blank=True)
    city                                            = models.CharField(max_length=30)
    visitors_participants                           = models.ManyToManyField(Profile, blank=True)
    bands_participated                              = models.ManyToManyField(Band, related_name="events_performed")
    ticket_price                                    = models.IntegerField(blank=True)
    comment                                         = models.TextField()
    poster                                          = models.ImageField(_("Image"),upload_to=upload_to, blank=True, default='concerts/no_poster.jpg')

    def save(self, *args, **kwargs):
        print("SAVING------------------: ")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


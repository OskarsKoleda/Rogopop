from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from django.utils.crypto import get_random_string
from django.utils.text import slugify
import os
from concerts.models import Event


@receiver(pre_save, sender=Event)
def add_slug_to_event(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.title)
        try:
            event = Event.objects.get(slug=slug)
            random_string = get_random_string(length=8)
            instance.slug = slug + "-" + random_string
        except:
            instance.slug = slug
    elif instance.slug:
        new_slug = slugify(instance)
        if new_slug != instance.slug:
            instance.slug = new_slug


@receiver(pre_delete, sender=Event)
def clean_up_poster(sender, instance, *args, **kwargs):
    event = Event.objects.get(slug=instance.slug)
    if event.poster.name != 'concerts/no_poster.jpg':
        event.poster.delete()

# @receiver(pre_save, sender=Event)
# def delete_old_poster_on_poster_change(sender, instance, *args, **kwargs):
#     # try:
#     event = Event.objects.get(slug=instance.slug)
#     old_poster_name = os.path.basename(event.poster.name)
#     new_poster_name = os.path.basename(instance.poster.name)
#     print(" OLD: ",old_poster_name)
#     print("NEW: ",new_poster_name)
#     print(" SENDER: ", sender)
#     print(" INSTANCE: ", instance)
#     print(" INSTANCE POSTER: ", instance.poster)
#     if old_poster_name != 'no_poster.jpg' and new_poster_name != 'no_poster.jpg':
#         event.poster.delete(save=False)

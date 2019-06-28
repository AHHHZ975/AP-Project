from PIL import Image, ExifTags
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.utils import timezone
from publications.models import Author

from ..models import Person, UpdateTime


@receiver(post_save, sender=Person)
def update_authors(**kwargs):
    """Search for the person in Author objects already available"""
    person = kwargs['instance']
    authors = Author.objects.filter(full_name=person.full_name)
    for author in authors:
        author.person = person
        author.save()


@receiver(post_save, sender=Person)
def resize_image(**kwargs):
    """ Post processing person photo """
    person = kwargs['instance']
    img = Image.open(person.picture.path)

    exif = img._getexif()
    if exif is None:
        return

    exif = dict(exif.items())
    for orientation in ExifTags.TAGS.keys():
        if ExifTags.TAGS[orientation] == 'Orientation': break

    try:
        if exif[orientation] == 3:
            img = img.rotate(180, expand=True)
        elif exif[orientation] == 6:
            img = img.rotate(270, expand=True)
        elif exif[orientation] == 8:
            img = img.rotate(90, expand=True)

        img.thumbnail((354, 472), Image.BICUBIC)
        img.save(person.picture.path, quality=50)
    except KeyError:  # When image is saved exif is not saved, so no exif for second time
        pass


@receiver(post_save, sender=Person)
@receiver(pre_delete, sender=Person)
def update_last_time(**kwargs):
    person = kwargs['instance']
    if person.updated_at is None:  # Post save first time
        person.updated_at = UpdateTime.objects.first()
    person.updated_at.updated_at = timezone.now()
    person.updated_at.save()

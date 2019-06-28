from django.apps import AppConfig
from django.db.models.signals import post_save
class BourseConfig(AppConfig):
    name = 'bourse'

    def ready(self):
        from bourse.Signals import handlers
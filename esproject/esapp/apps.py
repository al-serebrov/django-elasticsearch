from django.apps import AppConfig


class EsappConfig(AppConfig):
    name = 'esapp'

def ready(self):
    import esapp.signals
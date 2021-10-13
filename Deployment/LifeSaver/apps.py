from django.apps import AppConfig
from django.conf import settings
import tensorflow as tf


class LifesaverConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'LifeSaver'

    model = tf.keras.models.load_model(settings.MODEL_ROOT, compile=False)

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from importlib import import_module


class SMSError(Exception):
    pass

def import_backend(backend, **kwargs):

    path = backend

    try:
        mod_name, klass_name = path.rsplit('.', 1)
        mod = import_module(mod_name)
    except ImportError as e:
        raise ImproperlyConfigured(('Error importing SMS backend module %s: "%s"' % (mod_name, e)))

    try:
        klass = getattr(mod, klass_name)
    except AttributeError:
        raise ImproperlyConfigured(('Module "%s" does not define a '
                                    '"%s" class' % (mod_name, klass_name)))

    return klass(**kwargs)


def send_sms(text, from_, to, backend=None, **kwargs):
    """
    Send an SMS using the specified backend

    """
    return import_backend(backend or settings.SMS_BACKEND).send_sms(text, from_, to, **kwargs)

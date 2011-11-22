import sms
from sms import send_sms

from nose.plugins.capture import Capture

def test_locmem_backend():
    """
    test local memory backend

    """
    sms.send_sms('my text message', 'me', 'you', backend='sms.backends.locmem.SMSBackend')
    assert len(sms.outbox) == 1
    assert sms.outbox[0]['text'] == 'my text message'
    assert sms.outbox[0]['from'] == 'me'
    assert sms.outbox[0]['to'] == 'you'

def test_console_backend():
    """
    test local memory backend

    """
    capture = Capture()
    capture.begin()

    sms.send_sms('my text message', 'me', 'you', backend='sms.backends.console.SMSBackend')
    assert capture.buffer ==  'youmemy text message'

    capture.finalize(capture.buffer)

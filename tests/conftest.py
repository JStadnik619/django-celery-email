import pytest


@pytest.fixture(autouse=True)
def celery_email_backend(settings):
    settings.EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'

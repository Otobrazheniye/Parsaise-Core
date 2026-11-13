from .base import *  # noqa: F401,F403


DEBUG = False

ALLOWED_HOSTS = [
    "testserver",
    "localhost",
]

# Unit tests only: no real database connection.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.dummy",
    # Здесь dummy специальный backend, который не выполняет реальные операции с базой.
    }
}

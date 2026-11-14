import os

from .base import *  # noqa: F401,F403


DEBUG = False

ALLOWED_HOSTS = ["testserver", "localhost"]

required = [
    "TEST_POSTGRES_DB",
    "TEST_POSTGRES_USER",
    "TEST_POSTGRES_PASSWORD",
    "TEST_POSTGRES_HOST",
    "TEST_POSTGRES_PORT",]

missing = [name for name in required if not os.getenv(name)]

if missing:
    raise RuntimeError(
        f"Missing integration test settings: {missing}")

if os.environ["TEST_POSTGRES_HOST"] not in (
    "localhost", "127.0.0.1",
    "postgres",):
    raise RuntimeError(
        "Integration tests require a local PostgreSQL host")

if os.environ["TEST_POSTGRES_DB"] != "pc89_ci":
    raise RuntimeError(
        "Integration tests require the pc89_ci database")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["TEST_POSTGRES_DB"],
        "USER": os.environ["TEST_POSTGRES_USER"],
        "PASSWORD": os.environ["TEST_POSTGRES_PASSWORD"],
        "HOST": os.environ["TEST_POSTGRES_HOST"],
        "PORT": os.environ["TEST_POSTGRES_PORT"],
        "TEST": {
            "NAME": "test_pc89_ci",
        },
    }
}

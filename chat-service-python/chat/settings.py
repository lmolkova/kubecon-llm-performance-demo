import os
from pathlib import Path
from openai import OpenAI
from opentelemetry._events import get_event_logger

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "django-insecure-kl^t0c0l42fyt=usm+u(4j2e@v9@6gygw2n%dh%m3x#nr!1*(-"
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "chat.urls"

INSTALLED_APPS = [
    'chat',
]

SETTINGS_PATH = os.path.normpath(os.path.dirname(__file__))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(SETTINGS_PATH, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = "chat.wsgi.application"

OPENAI_CLIENT = OpenAI(
    base_url=os.environ.get('OPENAI_API_BASE_URL'),
)

MODEL = os.environ.get('MODEL')
from meilleur_corpo.core.global_settings import *

ROOT_URLCONF = 'meilleur_corpo.projects.api.urls'

WSGI_APPLICATION = 'meilleur_corpo.projects.api.wsgi.application'

INSTALLED_APPS += (
    'rest_framework',

    'meilleur_corpo.apps.estate_adverts'
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ]
}


SECRET_KEY = 'replacethiswithsomethingsecret'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'pldp',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': 32009,
    }
}

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'countries_plus',
    'languages_plus',
    'pldp.core',
    'pldp.location',
    'pldp.agency',
    'pldp.study',
    'pldp.survey',
)

MIDDLEWARE_CLASSES = ()
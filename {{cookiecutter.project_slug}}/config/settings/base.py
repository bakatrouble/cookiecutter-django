import environ
import os

ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path('{{ cookiecutter.project_slug }}')

env = environ.Env()

env_file = str(ROOT_DIR.path('.env'))
if os.path.exists(env_file):
    print('Loading : {}'.format(env_file))
    env.read_env(env_file)

print('The .env file has been loaded. See base.py for more information')

DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.humanize',

    'django.contrib.admin',
]

THIRD_PARTY_APPS = []

LOCAL_APPS = [
    '{{cookiecutter.project_slug}}.users.apps.UsersConfig',
]

SECRET_KEY = 'qz1y-u^p&p5so4!b371tts!^qwb^lqb7fd@-ejo!z-s_blo=s2'

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# MIGRATION_MODULES = {
#     'sites': '{{ cookiecutter.project_slug }}.contrib.sites.migrations'
# }

DEBUG = env.bool('DJANGO_DEBUG', False)

# FIXTURE_DIRS = (
#     str(APPS_DIR.path('fixtures')),
# )

EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',
                    default='django.core.mail.backends.smtp.EmailBackend')

ADMINS = [
    ('''{{cookiecutter.author_name}}''', '{{cookiecutter.email}}'),
]

MANAGERS = ADMINS

DATABASES = {
    'default': env.db('DATABASE_URL', default='sqlite://db.sqlite3'),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

TIME_ZONE = '{{ cookiecutter.timezone }}'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(APPS_DIR.path('templates'))
        ],
        'OPTIONS': {
            'debug': DEBUG,
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

PUBLIC_ROOT = ROOT_DIR.path('public')
STATIC_URL = '/static/'
STATIC_ROOT = str(PUBLIC_ROOT.path('static'))
MEDIA_URL = '/uploads/'
MEDIA_ROOT = str(PUBLIC_ROOT.path('uploads'))

STATICFILES_DIRS = [
    str(APPS_DIR.path('static'))
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

AUTH_USER_MODEL = 'users.User'

ADMIN_URL = r'^admin/'

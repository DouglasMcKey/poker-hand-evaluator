from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

# ================================================= [STANDARD SECURITY SETTINGS]
ROOT_URLCONF = "main.urls"
WSGI_APPLICATION = "main.wsgi.application"
SECRET_KEY = "django-insecure-q!v#p!lf&lq5)jy$wl9g%wc1r8z4r-70ay74td0g4-$90zp-y="

# ============================================= [INSTALLED APPLICATION SETTINGS]
DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "corsheaders",
]

API_APPS = [
    "api.apps.APIConfig",
]

PROJECT_APPS = [
    "main.apps.MainConfig",
]

INSTALLED_APPS = DJANGO_APPS + API_APPS + PROJECT_APPS

# ======================================================== [MIDDLEWARE SETTINGS]
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ========================================================= [TEMPLATES SETTINGS]
BASE_DIRECTORY = Path(__file__).resolve(strict=True).parent.parent.parent
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIRECTORY / "templates"],
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth"
            ]
        }
    }
]

# ============================================== [INTERNATIONALIZATION SETTINGS]
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ============================================================== [HOST SETTINGS]
ALLOWED_HOSTS = [".localhost", "127.0.0.1"]
CORS_ALLOWED_ORIGINS = ["http://localhost:4200", "http://127.0.0.1:4200"]

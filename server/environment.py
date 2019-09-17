import os

ENVIRONMENT = os.environ.get("ENVIRONMENT", "development")

SETTINGS_DICT = {
    "development": "server.settings.development",
    "production": "server.settings.production",
    "aws_production": "server.settings.aws_production"
}

SETTINGS_MODULE = SETTINGS_DICT.get(ENVIRONMENT, 'development')

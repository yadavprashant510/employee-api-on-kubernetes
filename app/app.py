from app.config import Config


def app_info():

    return {
        "application": Config.APP_NAME,
        "version": Config.APP_VERSION,
        "environment": Config.ENVIRONMENT,
    }

import os


class Config:
    APP_NAME = os.getenv("APP_NAME", "Employee API")
    APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 5000))

    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")

    # Probe Simulation
    SIMULATION_MODE = os.getenv("SIMULATION_MODE", "normal")

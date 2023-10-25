import json
import os

from dotenv import dotenv_values


def load_app_config():
    """
    Need this, allows safer value loading, defaults, safe panicking, keeps code dry, etc.
    """
    env_config = dict()

    if "ENVIRONMENT" not in os.environ:
        os.environ["ENVIRONMENT"] = "development"

    env_config["ENVIRONMENT"] = os.environ.get("ENVIRONMENT")

    if env_config["ENVIRONMENT"] == "development":
        env_config = {
            **os.environ,  # override loaded values with environment variables
            **dotenv_values("../../.env.shared"),  # load shared development variables
            **dotenv_values("../../.env.secret"),  # load sensitive variables
            **dotenv_values("../../.env.development"),  # load shared development variables
        }

    return env_config


def test_load_app_config():
    test_config = load_app_config()

    assert test_config["environment"] == "development"
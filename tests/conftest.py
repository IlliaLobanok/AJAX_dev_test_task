import subprocess
import time

import logging
import pytest
from appium import webdriver

from utils import android_get_desired_capabilities
from logger import TLogger


@pytest.fixture(scope='session')
def setup_logger():
    logging.setLoggerClass(TLogger)

    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler("tests/test_log.txt")
    handler.setLevel(logging.DEBUG)
    log_format = logging.Formatter("%(asctime)s ::: %(levelname)s ::: %(message)s")
    handler.setFormatter(log_format)
    logger.addHandler(handler)

    logger.info(f"Logging service started at {__name__}")

    return logger


@pytest.fixture(scope='class')
def get_driver_ajaxsystems(setup_logger):
    capabilities = dict(
        platformName='Android',
        automationName='uiautomator2',
        deviceName='my_phone',
        appPackage='com.ajaxsystems',
        appActivity='.ui.activity.LauncherActivity',
        noReset=False,
        language='en',
        locale='US'
    )
    appium_server_url = 'http://localhost:4723'

    setup_logger.info("Starting up the driver...")

    return webdriver.Remote(appium_server_url, capabilities)


@pytest.fixture(scope='session')
def run_appium_server():
    subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )
    time.sleep(5)


@pytest.fixture(scope='session')
def driver(run_appium_server):
    driver = webdriver.Remote('http://localhost:4723/wd/hub', android_get_desired_capabilities())
    yield driver

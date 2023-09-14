import subprocess
import time

import logging
import pytest
from appium import webdriver

from utils import android_get_desired_capabilities
from logger import TLogger


@pytest.fixture(scope='session', autouse=True)
def setup_logger():
    logging.setLoggerClass(TLogger)
    logger = logging.getLogger(__name__)

    logger.info(f"Logging service started")

    return logger


@pytest.fixture(scope='class')
def get_driver_ajaxsystems():
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

    logger = logging.getLogger(__name__)
    logger.info("Starting up the driver")

    return webdriver.Remote(appium_server_url, capabilities)


# @pytest.fixture(scope='session')
# def run_appium_server():
#     subprocess.Popen(
#         ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell'],
#         stdout=subprocess.DEVNULL,
#         stderr=subprocess.DEVNULL,
#         stdin=subprocess.DEVNULL,
#         shell=True
#     )
#     time.sleep(5)
#
#
# @pytest.fixture(scope='session')
# def driver(run_appium_server):
#     driver = webdriver.Remote('http://localhost:4723/wd/hub', android_get_desired_capabilities())
#     yield driver

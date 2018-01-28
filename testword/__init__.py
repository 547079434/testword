from os import path
from django.apps import AppConfig

VERBOSE_APP_NAME = "分数记录"


def get_current_app_name(file):
    return path.dirname(file).replace('\\', '/').split('/')[-1]


class TestWordConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = VERBOSE_APP_NAME


default_app_config = get_current_app_name(__file__) + '.__init__.TestWordConfig'
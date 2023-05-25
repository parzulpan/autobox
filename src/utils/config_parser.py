# -*- coding: utf-8 -*-
"""


@author: panpan
@since: 2023/5/25
"""
import configparser

config = configparser.ConfigParser()
config.read('./assets/config.ini')


def get(section: str, option: str):
    """

    :param section:
    :param option:
    :return:
    """
    return config.get(section, option)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/1/8 20:45
# @Author  : nujaijey
# @File    : logger_utils.py
# @Desc    :


import logging
import os
import sys
import time
from logging.handlers import TimedRotatingFileHandler


# from jsonpath import jsonpath


class LoggerUtils:
    workdir = os.path.split(os.path.realpath(__file__))[0]

    # @classmethod
    # def jsonpath(cls, json_object, expr):
    #     return jsonpath(json_object, expr)

    @classmethod
    def getLogger(cls, name, package_name):
        logger = logging.getLogger(name)
        if logger.handlers:
            return logger
        logger.setLevel(logging.DEBUG)
        time_formator = '%Y%m%d'
        now_string = time.strftime(time_formator, time.localtime(time.time()))
        file_name = 'log_{}.log'.format(now_string)
        # os.chdir(workdir)
        root_path = os.path.abspath(
            os.path.join(cls.workdir, ".."))
        _folder_path = os.path.join(root_path, package_name)
        if not os.path.exists(_folder_path):
            os.mkdir(_folder_path)
        filePath = os.path.join(_folder_path, file_name)
        t = int(time.time())
        if TimedRotatingFileHandler(filePath).when.startswith('D') and time.localtime(t).tm_mday == time.localtime(
                TimedRotatingFileHandler(filePath).rolloverAt).tm_mday:
            return 1
        else:
            pass

        # FileHandler
        fh = logging.FileHandler(filePath, mode='a', encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '******%(asctime)s - %(name)s - %(filename)s,line %(lineno)s - %(levelname)s: %(message)s')
        fh.setFormatter(formatter)

        sh = logging.StreamHandler(sys.stdout)
        sh.setFormatter(formatter)
        sh.setLevel(logging.DEBUG)
        logger.addHandler(fh)
        logger.addHandler(sh)
        # logger.addHandler(uh)

        return logger

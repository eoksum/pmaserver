#!/usr/bin/python3

import os
import configparser
import socket
import ssl

_configPath = os.getcwd() + "/config.ini"
_dispExceptions = True

def exception(exception):
    if _dispExceptions:
        print("[!!!] {}".format(exception))

def readConf():
    if not os.path.isfile(_configPath):
        print("Configuration file is absent!")
        exit(0)
    try:
        config = configparser.ConfigParser()
        config.read(_configPath)
    
    

def main():
    
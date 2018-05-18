#!/usr/bin/python

import ConfigParser

class Config:
    __instance = None

    @staticmethod
    def getInstance():
        if Config.__instance == None:
            Config()
        return Config.__instance 

    def __init__(self):
        if Config.__instance != None:
            raise Exception("Config class is a singleton!")
        else:
            Config.__instance = self

    conf = None

    def readConfigFile(self,instance):
        self.conf = ConfigParser.ConfigParser()
        filename = "config_" + instance + ".ini"
        print("reading " + filename)
        self.conf.read(filename)

    def getDatabaseConfig(self):
        return self.conf.get("Database", "Host"), self.conf.get("Database", "Username"), self.conf.get("Database", "Password"), self.conf.get("Database", "Database")

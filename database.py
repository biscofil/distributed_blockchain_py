#!/usr/bin/python

from config import Config
import MySQLdb

class Database:
    __instance = None

    @staticmethod
    def getInstance():
        if Database.__instance == None:
            Database()
        return Database.__instance 

    def __init__(self):
        if Database.__instance != None:
            raise Exception("Database class is a singleton!")
        else:
            Database.__instance = self

    db = None
    cur = None

    def db_connect(self):
        (host,user,psw,db) = Config.getInstance().getDatabaseConfig()
        self.db = MySQLdb.connect(host=host,    # your host, usually localhost
                        user=user,         # your username
                        passwd=psw,  # your password
                        db=db)        # name of the data base

        self.cur = self.db.cursor()

    def db_close(self):
        self.db.close()

    def getHosts(self):
        self.cur.execute("SELECT * FROM hosts")
        for row in self.cur.fetchall():
            print row[0]

    def getBlocks(self):
        self.cur.execute("SELECT payload FROM blocks")
        for row in self.cur.fetchall():
            print row[0]
#!/usr/bin/python

from config import Config
from database import Database
import sys

database = Database()
config = Config()

if len(sys.argv) < 2:
    raise Exception("Instance letter needed")

config.readConfigFile(sys.argv[1])

database.db_connect()

database.getBlocks()

database.db_close()
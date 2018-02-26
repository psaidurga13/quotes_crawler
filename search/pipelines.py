
from scrapy.exceptions import DropItem
import sqlite3

class SearchPipeline(object):
    def process_item(self, item, spider):
        return item



class Db_Pipeline(object):

    def __init__(self):
        self.setupDbCon()
        self.createTables()

    def setupDbCon(self):
        self.conn = sqlite3.connect('quotes.db')
        self.conn.text_factory = str
        self.cur = self.conn.cursor()

    def createTables(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS quotes(sno INTEGER PRIMARY KEY AUTOINCREMENT ,author TEXT,quote TEXT)")

    def process_item(self,item,spider):
        self.storeInDb(item)
        return item

    def storeInDb(self,item):
        self.cur.execute("INSERT INTO quotes( author ,quote) VALUES (?, ?)",(item.get("author"), item.get("quote")))
        self.conn.commit()

    def __def__(self):
        self.closeDb()

    def closeDb(self):
        self.conn.commit()
        self.conn.close()


import sqlite3

tables = {
'source_chats_tn' : "source_chats",
'target_chats_tn' : "source_chats",
'route_chats_tn' : "route_chats"
}


class DataSource:
    _DB_NAME = 'fapi.db'

    def __init__(self):
        self.connection = sqlite3.connect(self._DB_NAME)
        all_tables_q = '''SELECT name FROM sqlite_master WHERE type IN ('table','view') AND name NOT LIKE 'sqlite_%' ORDER BY 1;'''
        cursor = self.connection.cursor()
        cursor.execute(all_tables_q)
        self.connection.commit()
        cursor.close()



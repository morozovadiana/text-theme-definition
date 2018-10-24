import pyorient


class Orient(object):
    def __init__(self):
        self.host = "localhost"
        self.port = 2424
        self.user = "root"
        self.password = "root"
        self.name = "Theme"
        self.connection = self.get_db_connection()
    
    def get_db_connection(self):
        instance = pyorient.OrientDB(self.host, self.port)
        instance.db_open(self.name, self.user, self.password)
        self.connection = instance
        return self.connection

    def __enter__(self):
        return self.connection

    def __exit__(self, *args):
        self.connection.close()
        self.connection = None

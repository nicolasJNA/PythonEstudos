class Connection:
    def __init__(self, host="localhost"):
        self.host = host
        self.password = None
        self.user = None
    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_classmethod(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def soma(msg):
        print("LOG: ",msg)


c1 = Connection()
# c2 = Connection.create_with_classmethod("juca","321")
# print(vars(c2))
c1.set_password('123')
c1.set_user("nicolas")
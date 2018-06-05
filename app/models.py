from app import db

class User(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def __init__(self, username, email):
        self.username = username
        self.email = email

class MyItems(db.Model):

    __tablename__ = 'MyItems'

    Uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Vendor = db.Column(db.String(64), index=True)
    Category = db.Column(db.String(64), index=True)
    Model = db.Column(db.String(64), index=True)
    Price = db.Column(db.Integer, index=True)


    def __repr__(self):
        return '<MyItems {}>'.format(self.Uid)

    def __init__(self, Vendor, Category, Model, Price):
        self.Vendor = Vendor
        self.Category = Category
        self.Model = Model
        self.Price = Price

 
from app import db


class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    d_no = db.Column(db.String(150), nullable=False)
    rate = db.Column(db.String(150), nullable=False)
    final_stones = db.Column(db.String(150), nullable=False)
    img = db.Column(db.String(150), nullable=False)

    # def as_dict(self):
    #     return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    # def __repr__(self):        
    #     return json.dumps({c.name: getattr(self, c.name) for c in self.__table__.columns})
    #     # return f"< Vendor Name : {self.name} >"


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    phone_number = db.Column(db.Integer, nullable=False)
    books = db.relationship('Book', backref='users', lazy=True)

    # def as_dict(self):
    #     return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
    #    return json.dumps({c.name: getattr(self, c.name) for c in self.__table__.columns})
        return f"< Name : {self.name} > ---->>> < Book : {len(self.books)} >"


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    qty = db.Column(db.String(100), nullable=False)
    detail = db.Column(db.String(100), nullable=False)
    rate = db.Column(db.String(100), nullable=False)
    total = db.Column(db.String(100), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # def as_dict(self):
    #     return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
    #    return json.dumps({c.name: getattr(self, c.name) for c in self.__table__.columns})
        return f"<Cutomer_id : {self.customer_id} Book id : {self.id} >"

from . import db

class PropertyPortfolio(db.Model):
    __tablename__ = 'property_portfolio' 

    id= db.Column(db.Integer, primary_key=True, autoincrement=True)
    title= db.Column(db.String(100))
    description= db.Column(db.String(200))
    bedroom= db.Column(db.Integer)
    bathroom= db.Column(db.Integer)
    price= db.Column(db.Integer)
    type= db.Column(db.String(10))
    location= db.Column(db.String(255))
    photo= db.Column(db.String(400))

    def __init__(self, title, description, bedroom, bathroom, price, type, location, photo):
        self.title = title
        self.description = description
        self.bedroom = bedroom
        self.bathroom = bathroom
        self.price = price
        self.type = type
        self.location = location
        self.photo = photo
        
        
        
        
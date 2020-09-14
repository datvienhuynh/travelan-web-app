from app import db

# Model for Destination instance
class Destination(db.Model):
    __tablename__ = 'destinations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    caption = db.Column(db.String(512))
    image_names = db.Column(db.String(512))
    date = db.Column(db.Integer)
    month = db.Column(db.String(64))
    year = db.Column(db.Integer)
    country = db.Column(db.String(64))
    visited = db.Column(db.Boolean)

    # Return string of 'month date, year'
    def get_date(self):
        return self.month + ' ' + str(self.date) + ', ' + str(self.year)

    def __repr__(self):
        return '<Destination %r - %r>' % self.name, self.description
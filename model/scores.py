from __init__ import db
from sqlalchemy.exc import IntegrityError

# Define the Score class to manage actions in the 'scores' table
class Score(db.Model):
    # sets scores as the name of the table
    __tablename__ = 'scores'

    # Define the Score schema with variables
    id = db.Column(db.Integer, primary_key=True)
    _name = db.Column(db.String(255), unique=False, nullable=False)
    _score = db.Column(db.String(255), unique=False, nullable=False)

    # constructor the Score object, initialize the object's attributes with variables
    def __init__(self, name, score):
        self._name = name     
        self._score = score

    @property
    def name(self):
        return self._name
    
    @property
    def score(self):
        return self._score
        
    # check if uid parameter matches user id in object, return boolean
    def is_score(self, score):
        return self._score == score
    
    # CRUD create method to add new user to scores table
    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        # returns None on error
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    def read(self):
        return {
            "id": self.id,
            "name": self.name,
            "score": self.score
        }

    # CRUD delete: remove user
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None
            
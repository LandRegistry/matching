from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.types import Enum

from matching import db

class User(db.Model):

    __tablename__ = 'users'

    lrid = db.Column(UUID(as_uuid=True), nullable=False, primary_key=True)
    name = db.Column(TEXT, nullable=False)
    date_of_birth = db.Column(db.Date(), nullable=False)
    gender = db.Column(Enum('F', 'M', name='gender_types'), nullable=False)
    current_address = db.Column(TEXT, nullable=False)
    previous_address = db.Column(TEXT, nullable=False)


    def __repr__(self):
        return str({
            'lrid': self.lrid,
            'name': self.name,
            'date of birth': self.date_of_birth,
            'gender': self.gender,
            'current address': self.current_address,
            'previous address': self.previous_address
        })


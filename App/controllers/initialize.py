from .user import create_user
from .student import create_student
from App.database import db
from App.models import Review


def initialize():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    bob = create_student('bob', 'bobbington')
    bob.reviews.append(Review('Good Job', 'Has done excellent work in class'))
    db.session.add(bob)
    db.session.commit()

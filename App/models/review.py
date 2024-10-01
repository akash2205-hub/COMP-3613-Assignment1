from App.database import db

class Review(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
  title = db.Column(db.String(50), nullable=False)
  text = db.Column(db.String(255), nullable=False)

  def __init__(self, title, text):
      self.title = title
      self.text = text

  def __repr__(self):
    return f'<Review: {self.id} | {self.student.fName}  {self.student.lName} | {self.title} | {self.text}>'
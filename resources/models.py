from server import db, ma

# User Model
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    # def __init__(self, user, email):
    #     self.user = user
    #     self.email = email


# User Schema
class UserSchema(ma.ModelSchema):
    class Meta:
        # Fields to expose
        model = User

class User (UserMixin,db.Model):
    __tablename__ ='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(20))
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(225))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    pitches = db.relationship('Pitch', backref='user', lazy='dynamic')
    comments = db.relationship('Comment', backref='user', lazy='dynamic')

    def __repr__(self):
        return f'User {self.name}' class Category(db.Model):
class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'

    __tablename__ = 'categories'

    id = db.Column(db.Integer,primary_key = True)
    category_name =db.Column(db.String)
    pitches = db.relationship('Pitch', backref='category', lazy='dynamic')

    def save_category(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_categories(cls,id):
        categories = Category.query.all()
        return categories
class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comments = db.relationship('Comment', backref='pitch', lazy='dynamic')

    

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitch(cls,category_id):
        pitches = Pitch.query.order_by(Pitch.id.desc()).filter_by(category_id=category_id).all()
        return pitches        return pitches
        return pitches

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    pitch_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_comment(self):        
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, pitch_id):       
        comments = Comment.query.order_by(Comment.id.desc()).filter_by(pitch_id=pitch_id).all()

        return comments
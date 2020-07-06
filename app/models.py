from app import db
from datetime import datetime
from app.utils import standard_date_format


class Movies(db.Model):
    __tablename__ = 'Movies'

    movie_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    release_date = db.Column(db.DateTime, nullable=False)
    roles = db.relationship('Roles', backref='Movies', lazy=True)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def details(self):
        release_date = datetime.strftime(
            self.release_date,
            standard_date_format
        )
        return {
            'id': self.movie_id,
            'title': self.title,
            'release_date': release_date,
            'roles': self.roles
        }

    def __repr__(self):
        return f'<Movie: {self.title}>'


class Actors(db.Model):
    __tablename__ = 'Actors'

    actor_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    roles = db.relationship('Roles', backref='Actors', lazy=True)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def details(self):
        return {
            'id': self.actor_id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'roles': self.roles
        }

    def __repr__(self):
        return f'<Actor: {self.name}>'


class Roles(db.Model):
    __tablename__ = 'Roles'

    role_id = db.Column(db.Integer, primary_key=True)
    actor_id = db.Column(db.Integer, db.ForeignKey('Actors.actor_id'),
                         nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('Movies.movie_id'),
                         nullable=False)
    role_desc = db.Column(db.String(120), nullable=True)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'<Role: {self.role_desc}\
        in {self.movie_id} played by {self.actor_id}>'

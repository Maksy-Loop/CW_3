from project.dao.models.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session


    def get_by_username(self, email):
        return self.session.query(User).filter(User.email == email).first()


    def create(self, user_d):
        ent = User(**user_d)
        self.session.add(ent)
        self.session.commit()
        return ent


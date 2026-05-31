from sqlmodel import Session, select

from app.models.user_model import User


class UserRepository:

    def __init__(self, session: Session):

        self.session = session


    def create(self, user: User):

        self.session.add(user)

        self.session.commit()

        self.session.refresh(user)

        return user
    
    def get_by_email(self, email: str):

        stmt = select(User).where(
            User.email == email
        )

        return self.session.exec(stmt).first()
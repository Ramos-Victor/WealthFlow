from sqlmodel import Session

from app.models.categoria_model import Categoria


class CategoriaRepository:

    def __init__(self, session: Session):

        self.session = session

    def create(self, categoria: Categoria):

        self.session.add(categoria)

        self.session.commit()

        self.session.refresh(categoria)

        return categoria
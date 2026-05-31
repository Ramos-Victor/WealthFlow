from sqlmodel import Session, select

from app.models.categoria_model import Categoria


class CategoriaRepository:

    def __init__(self, session: Session):

        self.session = session

    def create(self, categoria: Categoria):

        self.session.add(categoria)

        self.session.commit()

        self.session.refresh(categoria)

        return categoria
    
    def get_by_id(self, categoria_id = int):

        stmt = select(Categoria).where(
            Categoria.id == categoria_id
        )

        return self.session.exec(stmt).first()
    
    def get_all_by_user(self, user_id = int):

        stmt = select(Categoria).where(
            Categoria.user_id == user_id
        )

        return self.session.exec(stmt).all()
    
    
    def update(self, categoria: Categoria):

        self.session.add(categoria)
        self.session.commit()
        self.session.refresh(categoria)

        return categoria

    def delete(
        self,
        categoria: Categoria
    ):
        
        self.session.delete(categoria)

        self.session.commit()
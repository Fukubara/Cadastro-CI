from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str] = mapped_column(String(50))
    senha: Mapped[str] = mapped_column(String(50))
    
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, login={self.login!r}, senha={self.senha!r})"


class Pessoa(Base):
    __tablename__ = "Pessoas"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(50))
    cpf: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))
    telefone: Mapped[str] = mapped_column(String(50))
    logradouro: Mapped[str] = mapped_column(String(50))
    cep: Mapped[str] = mapped_column(String(50))
    cidade: Mapped[str] = mapped_column(String(50))
    numero: Mapped[int] = mapped_column(Integer())
    complemento: Mapped[str] = mapped_column(String(50))
    estado: Mapped[str] = mapped_column(String(50))

    def __repr__(self) -> str:
        return f"""User(
            id={self.id!r},
            nome={self.nome!r},
            cpf={self.cpf!r},
            email={self.email!r},
            telefone={self.telefone!r},
            logradouro={self.logradouro!r},
            cep={self.cep!r},
            cidade={self.cidade!r},
            numero={self.numero!r},
            complemento={self.complemento!r},
            estado={self.estado!r}
            )"""
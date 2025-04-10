from sqlalchemy import text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.dao.database import Base, str_uniq
from app.dao.sql_enums import TypeEnum


class Role(Base):
    name: Mapped[str_uniq]
    users: Mapped[list["User"]] = relationship(back_populates="role")

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name})"


class User(Base):
    phone_number: Mapped[str_uniq]
    first_name: Mapped[str]
    last_name: Mapped[str]
    balance: Mapped[int] = mapped_column(default=1)
    email: Mapped[str_uniq]
    password: Mapped[str]
    role_id: Mapped[int] = mapped_column(ForeignKey('roles.id'), default=3, server_default=text("3"))
    role: Mapped["Role"] = relationship("Role", back_populates="users", lazy="joined")

    invoices: Mapped[list['Invoice']] = relationship(back_populates="user", cascade="all, delete") #"Invoice", 

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id})"


class Invoice(Base):
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), default=11, server_default=text("11"))
    user: Mapped["User"] = relationship("User", back_populates="invoices", lazy="joined")
    title: Mapped[str]
    amount: Mapped[float] = mapped_column(nullable=False)
    type: Mapped[TypeEnum]

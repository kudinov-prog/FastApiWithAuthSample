from app.dao.base import BaseDAO
from app.auth.models import User, Role, Invoice


class UsersDAO(BaseDAO):
    model = User


class RoleDAO(BaseDAO):
    model = Role


class InvoiceDAO(BaseDAO):
    model = Invoice
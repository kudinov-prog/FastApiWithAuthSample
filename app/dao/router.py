from fastapi import APIRouter, Request, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.dependencies.dao_dep import get_session_with_commit, get_session_without_commit
from app.dependencies.auth_dep import get_current_user, get_current_admin_user, check_refresh_token
from app.auth.models import User, Invoice
from app.auth.router import get_all_users
from typing import List
from app.auth.schemas import SInvoiceInfo, SInvoiceCreate
from app.auth.dao import InvoiceDAO

from app.auth.schemas import SInvoiceInfo, SInvoiceCreate


router = APIRouter(prefix='/invoices', tags=['Платежи'])


@router.get('/all')
async def get_all_invoices(session: AsyncSession = Depends(get_session_with_commit),
                           user_data: User = Depends(get_current_admin_user)
                           ) -> List[SInvoiceInfo]:
    return await InvoiceDAO(session).find_all()


@router.post("/create")
async def register_invoice(invoice_data: SInvoiceCreate,
                           user_data: User = Depends(get_current_admin_user),
                           session: AsyncSession = Depends(get_session_with_commit)
                           ) -> dict:
    # Проверка существования платежа
    invoice_dao = InvoiceDAO(session)

    # Подготовка данных для добавления
    invoice_data_dict = invoice_data.model_dump()

    # Добавление пользователя
    await invoice_dao.add(values=SInvoiceCreate(**invoice_data_dict))

    return {'message': 'Invoice успешно добавлен!'}

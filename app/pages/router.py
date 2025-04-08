from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from app.auth.router import get_all_users


router = APIRouter(prefix='/pages', tags=['Фронтенд'])
templates = Jinja2Templates(directory='app/templates')


@router.get('/users')
async def get_users_html(request: Request, users=Depends(get_all_users)):
    return templates.TemplateResponse(
        name='users.html',
        context={'request': request, 'users': users}
        )
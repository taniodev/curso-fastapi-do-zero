from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.orm import Session

from fast_zero.database import get_session
from fast_zero.models import User
from fast_zero.schemas import Token
from fast_zero.security import (
    create_access_token,
    verify_password,
)

router = APIRouter(prefix='/auth', tags=['auth'])
OAuth2Form = Annotated[OAuth2PasswordRequestForm, Depends()]
Session = Annotated[Session, Depends(get_session)]


@router.post('/token', response_model=Token)
def login_for_access_token(form_data: OAuth2Form, session: Session):
    db_user = session.scalar(
        select(User).where(User.email == form_data.username)
    )

    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Incorrect e-mail or password',
        )

    if not verify_password(form_data.password, db_user.password):
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Incorrect e-mail or password',
        )

    access_token = create_access_token(data={'sub': db_user.email})

    return {'access_token': access_token, 'token_type': 'bearer'}

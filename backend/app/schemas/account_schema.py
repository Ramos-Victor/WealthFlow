from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime

class AccountCreate(BaseModel):

    name: str
    balance: Decimal
    user_id: int


class AccountResponse(BaseModel):

    id: int
    name: str
    balance: Decimal
    created_at: datetime
    user_id: int

class AccountUpdate(BaseModel):

    name: str | None = None
    balance: Decimal | None = None

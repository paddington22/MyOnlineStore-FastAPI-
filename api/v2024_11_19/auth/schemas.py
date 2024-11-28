from pydantic import BaseModel, EmailStr

from core.database.users import UserRole


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


class AuthResponse(BaseModel):
    auth: TokenResponse
    role: UserRole


class GetToken(BaseModel):
    mail: EmailStr

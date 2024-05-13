from pydantic import BaseModel
from typing import Optional


# Validatsiyalr berish uchun
class SignUpModel(BaseModel):
    id: Optional[int]  # majmuriy kiritish shart emas
    username: str
    email: str
    password: str
    is_staff: Optional[bool]
    is_active: Optional[bool]

    class Config:
        orm_mode = True
        # orm rejimini yoqib beradi
        # malumotlar to'g'ri kiritilgan bo'lsa pydentic uni sqlalchemyga ogirib beradi malumotlar bazasiga saqlanadi
        schema_extra = {
            'example': {
                'username': "Ismingiz",
                'email': "Emailingiz",
                'password': "password",
                'is_staff': False,
                "is_active": True
            }  # foydalanuvshiga placeholder korinishida shu malumotlarni ko'rsatib turadi
        }


class Settings(BaseModel):
    authjwt_secret_key: str = 'a952f06b061769101daf6ef549d6284510cd958d9e77f26ebe9b3edf790efc73'
    # shu secret key orqali userning tokenini enkod va decod qilib haqiqiligini tekshiramiz


class LoginModel(BaseModel):
    username_or_email: str
    password: str

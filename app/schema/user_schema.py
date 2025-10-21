import pydantic as BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):

    username: str = Field(..., min_length=3, max_length=50)
    email : EmailStr
    full_name : str = Field (min_length=1, max_length=100)


class UserCreate(UserBase):

    password : str = Field(..., min_length=8, max_length=100),

class UserUpdate(BaseModel):

    username: str = Field(None , min_length=3, max_length=50),
    email : Optional[EmailStr] = None,
    full_name : Optional[str] = Field (None, min_length=1, max_length=100),


class userResponse(UserBase):

    id : int 
    is_active : bool
    created_at : datetime
    updated_at : Optional[datetime] = None


    class Config:
        from_attributes = True


class Userlogin(BaseModel):

    username : str
    password : str




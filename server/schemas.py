from pydantic import BaseModel, EmailStr
from datetime import datetime

# User creation schema
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# User response schema
class UserResponse(BaseModel):
    id: int
    email: str
    created_at: datetime
    
    class Config:
        from_attributes = True

# JWT Token response schema
class Token(BaseModel):
    access_token: str
    token_type: str

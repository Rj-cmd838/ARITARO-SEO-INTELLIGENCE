from pydantic import BaseModel, EmailStr


# Data required when a user registers
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


# Data returned by the API
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_active: bool

    model_config = {
        "from_attributes": True
    }
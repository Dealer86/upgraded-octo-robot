from pydantic import BaseModel, Field


class OrmModel(BaseModel):
    class Config:
        orm_model = True


class UserInfo(BaseModel):
    username: str = Field(description="Alphanumeric username between 6 and 20 characters")
    email: str = Field(description="Valid email")

    class Config:
        orm_mode = True


class UserAdd(BaseModel):
    username: str = Field(description="Alphanumeric username between 6 and 20 characters")
    email: str = Field(description="Valid email")


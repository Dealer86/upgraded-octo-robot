from pydantic import BaseModel, Field


class UserAdd(BaseModel):
    name: str = Field(description="Full name")
    email: str = Field(description="A valid email, we'll send confirmation code")


class UserUpdate(BaseModel):
    name: str = Field("Name to update")


class UserInfo(UserAdd):
    films: list[str] = Field(default=[], description="List of films on watchlist")
    shows: list[str] = Field(default=[], description="List of TV shows on watchlist")
    id: int = Field(default=None, description="ID by which to identify a specific user")

    class Config:
        orm_mode = True



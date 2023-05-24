from pydantic import BaseModel, Field


class UserAdd(BaseModel):
    name: str = Field(description="Full name")
    email: str = Field(description="A valid email, we'll send confirmation code")

    class Config:
        orm_mode = True


class UserInfo(UserAdd):
    films: list[str] = Field(default=[], description="List of films on watchlist")
    shows: list[str] = Field(default=[], description="List of the shows on watchlist")

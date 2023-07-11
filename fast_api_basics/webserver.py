

from fastapi import FastAPI, APIRouter
from fastapi.responses import HTMLResponse, FileResponse
from starlette.responses import RedirectResponse
from pydantic import BaseModel


class Book(BaseModel):
    name: str
    author: str
    available: int = 0

hello_router = APIRouter(prefix="/hello")



app = FastAPI()

books = []
user = "random_user"


@hello_router.get("/books")
def get_books():
    return {"books": books, "user": user}


@hello_router.post("/books", response_model=Book)
def add_book(book: Book):
    new_book = {"name": book.name, "author": book.author}
    books.append(new_book)
    return new_book


@hello_router.get("")
def get_link():
    link = "https://youtube.com"
    return RedirectResponse(url=link)


@hello_router.get("/again")
def get_picture():
    picture_path = "cs50.jpg"
    return FileResponse(picture_path, media_type="image/jpg")


app.include_router(hello_router)

if __name__ == "__main__":
    import subprocess
    subprocess.run(["uvicorn", "webserver:app", "--reload"])

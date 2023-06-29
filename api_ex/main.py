from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

from api_ex.api.users import users_router
from api_ex.domain.factory import NotRightLength, NotValidEmail

app = FastAPI(description="Store a user info into persistence", debug=True)

app.include_router(users_router)


@app.exception_handler(NotRightLength)
def return_400(_: Request, e: NotRightLength):
    return JSONResponse(status_code=400, content=str(e))


@app.exception_handler(NotValidEmail)
def return_400(_: Request, e: NotValidEmail):
    return JSONResponse(status_code=400, content=str(e))


if __name__ == "__main__":
    import subprocess
    subprocess.run(['uvicorn', 'main:app', '--reload'])

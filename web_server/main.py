from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from web_server.api.users import users_router
from web_server.domain.user_factory import UsernameNotValid, EmailNotValid

# Create an API which can save your preferred films and tvshows.
# We can add users. A user has a name, email, list of films, list of tvshows.
# The lists are empty for a new user.
# We can get the list of all users.
# We can delete a user.
# We can modify the email of a user.
# We can get the list of all films, all tvshows or both for a user.
# We can add a tvshow or a film for a user. We can also remove it.
# Save the users, films & tvshows in a json in a file.

app = FastAPI(
    title="Personal library",
    description="A place to track your films and shows",
    version="0.1.0" # x.y.z x- major version, y - minor version, z - patch version
)


app.include_router(users_router)


@app.exception_handler(UsernameNotValid)
def return_400(_: Request, exc: UsernameNotValid):
    return JSONResponse(status_code=400, content=str(exc))


@app.exception_handler(EmailNotValid)
def return_400(_: Request, exc: EmailNotValid):
    return JSONResponse(status_code=400, content=str(exc))


if __name__ == "__main__":
    import subprocess
    subprocess.run(["uvicorn", "main:app", "--reload"])

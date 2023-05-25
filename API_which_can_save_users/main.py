from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from email_validator import EmailNotValidError

from API_which_can_save_users.domain.user_factory import UsernameNotValid

# Create an API which can save your preferred films and tvshows.
# We can add users. A user has a name, email, list of films, list of tvshows.
# The lists are empty for a new user.
# We can get the list of all users.
# We can delete a user.
# We can modify the email of a user.
# We can get the list of all films, all tvshows or both for a user.
# We can add a tvshow or a film for a user. We can also remove it.
# Save the users, films & tvshows in a json in a database.

app = FastAPI(
    title="Personal library",
    description="A place to track your films and shows",
    version="0.1.0"  # x.y.z x- major version, y - minor version, z - patch version
)

app.include_router(users_router)


@app.exception_handler(UsernameNotValid)
def return_400(_: Request, exc: UsernameNotValid):
    return JSONResponse(status_code=400, content=str(exc))


@app.exception_handler(EmailNotValidError)
def return_400(_: Request, exc: EmailNotValidError):
    return JSONResponse(status_code=400, content=str(exc))


if __name__ == "__main__":
    import subprocess

    subprocess.run(["uvicorn", "main:app", "--reload"])

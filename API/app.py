import multisocial
from fastapi import FastAPI
from dataclasses import asdict

API = FastAPI()

@API.get("/")
def status() -> str:
    return "MultiSocial API is working"

@API.get("/user")
def instagram_user(username: str) -> dict:

    USER = multisocial.packages.instagram.Instagrammer()
    DATA = USER.user(username = username)

    if DATA is not False:
        return asdict(DATA)
    
    else:
        return {"Error": "Unable to fetch data"}

@API.get("userbyid")
def instagram_user_by_id(id: int) -> dict:

    USER = multisocial.packages.instagram.Instagrammer()
    DATA = USER.user_from_id(id = id)

    if DATA is not False:
        return asdict(DATA)
    
    else:
        return {"Error": "Unable to fetch data"}

@API.get("/post")
def instagram_post(url: str) -> dict:

    USER = multisocial.packages.instagram.Instagram(url = url)
    DATA = USER.post()

    if DATA is not False:
        return asdict(DATA)
    
    else:
        return {"Error": "Unable to fetch data"}

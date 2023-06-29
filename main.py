from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# token no manejado


class LoginItem(BaseModel):
    client_id: str
    client_secret: str
    grant_type: str
    authenticated_userid: str
    scope: str


#
# @app.get("/")
# async def root():
#     return {"message": "Hello World api"}


@app.post("/api/clients/user/login")
async def get_body(item: LoginItem):
    # can access subitems like item.client_id
    return {"token_type": "bearer",
            "access_token": "d*KPsueadLxKSqa#niNL¥z]Viy1KtVixrs_0zCoMaFZ5Ca9P",
            "expires_in": "15/06/2023 20:17:00"}

# @app.post("/dummypath")
# async def get_body(request: Request):
#     return await request.json()

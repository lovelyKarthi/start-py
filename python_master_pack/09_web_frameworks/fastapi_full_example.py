"""FastAPI example with auth stub and dependency injection (template)"""
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
app = FastAPI()

class User(BaseModel):
    username: str

def fake_auth(token: str = None):
    if token != 'secrettoken':
        raise HTTPException(status_code=401, detail='unauth')
    return User(username='demo')

@app.get('/me')
def me(user: User = Depends(fake_auth)):
    return {'user': user.dict()}

if __name__ == '__main__':
    print('Run with uvicorn to test endpoints')

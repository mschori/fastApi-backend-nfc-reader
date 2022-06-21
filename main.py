from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel


class Time(BaseModel):
    scanner_code: int
    scanner_password: str
    tag_id: int


app = FastAPI()


@app.post("/time/", status_code=status.HTTP_201_CREATED)
async def create_item(item: Time):
    if item.scanner_code is not '789456123':
        raise HTTPException(status_code=401, detail='Scanner-Code not found.')
    if item.scanner_password is not 'Sml12345':
        raise HTTPException(status_code=403, detail="Invalid Scanner-Password.")
    if item.tag_id is not '42':
        raise HTTPException(status_code=404, detail='No Tag with this ID found.')
    return item

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from inventory.api import api


app = FastAPI()

app.mount('/api', api)

register_tortoise(app, db_url="sqlite://:memory:", modules={"models": ["inventory.items"]},
                  generate_schemas=True, add_exception_handlers=True)
from fastapi import FastAPI
from inventory import items

api = FastAPI()

api.mount("/item", items.api)
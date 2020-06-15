from fastapi import FastAPI
from tortoise import Model, fields
from tortoise.contrib.pydantic import pydantic_model_creator


class Item(Model):
    name = fields.CharField(max_length=255)
    desc = fields.CharField(max_length=255)

ItemSchema = pydantic_model_creator(Item, name="Item")
ItemPostSchema = pydantic_model_creator(Item, name="ItemPost", exclude_readonly=True)

api = FastAPI()

@api.get('/')
async def list_items():
    return {}

@api.post('/', status_code=201)
async def create_item(item: ItemPostSchema):
    item = await Item.create(**item.dict(exclude_unset=True))
    return await ItemSchema.from_tortoise_orm(item)

__models__ = [Item]
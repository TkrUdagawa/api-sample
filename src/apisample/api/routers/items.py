from typing import List

from fastapi import APIRouter

from ..types import APIResponse, Item


router = APIRouter()


@router.post("/item", tags=["item"], response_model=APIResponse)
async def post_item(item: Item):
    """アイテムを追加します
    """
    print(item.title)
    print(item.body)
    return APIResponse(message="ok", status_code=0)


@router.get("/item", tags=["item"], response_model=List[Item])
async def get_item():
    """アイテムを参照します
    """
    items = [
        Item(id="0", title="test", body="testtest"),
        Item(id="1", title="test2", body="testtest2")
    ]
    return items

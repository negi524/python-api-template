from python_api_template.main import read_root
from python_api_template.main import read_item
from python_api_template.main import update_item
from python_api_template.dto.item import Item


def test_read_root():
    assert read_root() == {"Hello": "World"}


def test_read_item():
    item_id = 1
    assert read_item(item_id=item_id, q="hoge") == {"item_id": item_id, "q": "hoge"}


def test_update_item():
    item = Item(name="hoge", price=100, is_offer=True)
    assert update_item(3, item) == {"item_name": "hoge", "item_id": 3}

from python_api_template.main import read_root
from python_api_template.main import read_item


def test_read_root():
    assert read_root() == {"Hello": "World"}


def test_read_item():
    item_id = 1
    assert read_item(item_id=item_id, q="hoge") == {"item_id": item_id, "q": "hoge"}

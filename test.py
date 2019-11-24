import json
import os

import pytest

from app import Application


@pytest.fixture
def test_data_file() -> None:
    disciplines = [
        "string1",
        "string2",
        "string3",
    ]
    with open("disciplines.json", "w") as file:
        json.dump(disciplines, file)
    yield "disciplines.json"
    os.remove("disciplines.json")


def test_discipline_data_returns_dict_from_json():
    app = Application(".")
    expected = [
        "string1",
        "string2",
        "string3",
    ]
    result = app.parse_disciplines()
    assert expected == result

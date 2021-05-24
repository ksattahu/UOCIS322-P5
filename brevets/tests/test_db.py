import nose
from db import db_find, db_insert


data = {}


def test_db_find():
    assert(db_find()==(False, False))


def test_db_insert():
    assert(db_insert(data)==False)

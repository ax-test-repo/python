import sqlite3
import pytest

from sql.db_user_utils import create_db, create_valid_user, delete_valid_user, get_user_name

def setup_module():
    create_db()

def setup_function():
    create_valid_user()

def teardown_function():
    delete_valid_user()

def test_get_user():
    user_name = get_user_name(1)
    assert user_name == "valid_user"

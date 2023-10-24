
import time
from sqlalchemy import update
from sql.models import User, db_session, valid_user


class TestUsers:
    def test_get_valid_user(self, db_session, valid_user):
        db_session.add(valid_user)
        db_session.commit()
        user = db_session.get(User, 0)
        assert user.username == 'username_test'


    def test_update_valid_user(self, db_session, valid_user):
        db_session.add(valid_user)
        db_session.commit()
        stmt = (
        update(User)
        .where(User.id == 0)
        .values(username="username_new")
        )
        db_session.execute(stmt)
        user = db_session.get(User, 0)
        assert user.username == 'username_new'


    def test_get_with_wait(self, db_session):
        timeout = 10  
        timeout_start = time.time()
        while time.time() < timeout_start + timeout:
            user = db_session.get(User, 0)
            if user:
                break
            time.sleep(10)
        assert user.username == 'username_test'
        db_session.delete(user)
        db_session.commit()
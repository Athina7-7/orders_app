from order_service import create_order
from database import SessionLocal
from models import Order
from user_repository import FakeUserRepository

class DummyLogger:
    def log(self, msg):
        pass

class NullNotifier:
    def send(self, to, message):
        pass

def test_create_order_integration_with_fake():
    db = SessionLocal()
    order = create_order(3, 60, NullNotifier(), DummyLogger(), db, FakeUserRepository())
    assert order.status == 'CREATED'
    assert order.user_email == "user3@fake.local"
    db.query(Order).delete()
    db.commit()
    db.close()

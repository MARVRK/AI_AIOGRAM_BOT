from app.models.users import User
from app.db.data_base import Session_local

db = Session_local()


def create_user(user_id, data_conversation, role):
    statement = db.query(User).filter(User.user_id == user_id).first()
    if statement is None:
        statement = User(user_id=user_id, data_conversation=[], role=role)
        db.add(statement)
        db.commit()
    else:
        statement.data_conversation.extend(data_conversation)
    db.add(statement)
    db.commit()
    db.refresh(statement)
    return statement


def fetch_all(user_id):
    statement = db.query(User).filter(User.user_id == user_id).first()
    return statement


def delete(user_id):
    statement = db.query(User).filter(User.user_id == user_id).first()

    if statement is not None:
        db.delete(statement)
        db.commit()
        return print(f"Deleted records: {statement}")
    return print("User not found")

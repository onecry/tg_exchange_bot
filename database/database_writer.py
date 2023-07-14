from database.storage import User, db

def write_in_db(full_name, id, text) -> None:
    with db:
        User.create(name=full_name, telegram_id=id, search_history=text)
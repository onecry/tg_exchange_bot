from database.storage import db, User

def history(from_user_id: int) -> str:
    history_list = list()
    with db:
        for i_elem in User.select().where(User.telegram_id == from_user_id).order_by(User.id.desc()):
            history_list.append(i_elem.search_history)

    result = '\n'.join(history_list[-len(history_list):10])

    return result
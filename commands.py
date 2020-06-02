import sys
from datetime import date

import models
import updates
from answers import answers
from api_handler import send_message
from database import SessionLocal

session = SessionLocal()


def run(update):
    # chat_id is the same as telegram user id because of private chats
    chat_id = updates.get_update_chat_id(update)
    user = session.query(models.User).filter_by(t_id=chat_id).first()
    update_text = updates.get_update_message(update)['text']

    commands_list = ('/start', '/new_list', '/save_list', '/get_list', '/get_commands')

    if update_text in commands_list:
        getattr(
            sys.modules[__name__],
            'command_'+update_text.replace('/', '')
        )(user=user, chat_id=chat_id, update_text=update_text)
    else:
        add_word(user, chat_id, update_text)

    session.commit()


def get_user_list(user, status=None, by_date=True):
    return next(
        filter(
            lambda l: (l.date == date.today() if by_date else True) and (l.status == status if status else True),
            user.lists
        ),
        None
    )


def command_start(user, chat_id, update_text):
    if not user:
        session.add(models.User(t_id=chat_id))
        send_message(chat_id, answers[update_text]['new_user'])
    else:
        send_message(chat_id, answers[update_text]['old_user'])


def command_new_list(user, chat_id, update_text):
    voc_list: models.List = get_user_list(user)

    if voc_list:
        if voc_list.status == 'created':
            send_message(chat_id, answers[update_text]['existed']['created'])
        if voc_list.status == 'saved':
            send_message(chat_id, answers[update_text]['existed']['saved'])
    else:
        user.lists.append(models.List(date=date.today()))
        send_message(chat_id, answers[update_text]['not_existed'])


def command_save_list(user, chat_id, update_text):
    voc_list: models.List = get_user_list(user, 'created')

    if voc_list:
        voc_list.status = 'saved'
        send_message(chat_id, answers[update_text]['existed'])
    else:
        send_message(chat_id, answers[update_text]['not_existed'])


def command_get_list(user, chat_id, update_text):
    voc_list: models.List = get_user_list(user)

    if voc_list:
        words = '\n'.join(list(map(lambda w: f'[{w.word}]', voc_list.words)))
        send_message(chat_id, 'The today\'s list of the words:\n' + words)


def command_get_commands(**kwargs):
    send_message(kwargs['chat_id'], answers[kwargs['update_text']])


def add_word(user, chat_id, update_text):
    voc_list: models.List = get_user_list(user, 'created')
    if voc_list:
        voc_list.words.append(models.Word(word=update_text))
        send_message(chat_id, f'The new word [{update_text}] added to the list')
    else:
        voc_list: models.List = get_user_list(user, 'saved')

        if voc_list:
            send_message(chat_id, 'You\'ve already saved your today\'s list.')
        else:
            send_message(chat_id, 'There are no lists found for today\'s date. '
                                  '\nYou can create the new one by typing the /new_list command!')

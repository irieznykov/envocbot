from api_handler import api_call


def get_updates(offset=None):
    return api_call('getUpdates', 'get', {'timeout': 100, 'offset': offset})


def get_oldest_update(data):
    if data['ok']:
        if len(data['result']) > 0:
            return data['result'][0]
        else:
            return data['result']
    else:
        return False


def get_update_chat_id(update):
    return get_update_message(update)['chat']['id']


def get_update_id(update):
    return update['update_id']


def get_update_message(update):
    return update.get('message') or update.get('edited_message')

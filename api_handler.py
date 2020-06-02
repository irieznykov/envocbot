import requests
import settings

url = f'https://api.telegram.org/bot{settings.BOT_API_KEY}/'


def api_call(uri, method='get', params=None):
    params = {} if params is None else params
    return getattr(requests, method)(url + uri, params=params).json()


def send_message(chat_id: int, text: str):
    return api_call('sendMessage', 'post', {'chat_id': chat_id, 'text': text})

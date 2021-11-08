import requests

class Bot:
    telegram_api_url = f"https://api.telegram.org/bot"

    def __init__(self, token):
        self.token = token
        self.url = f'{self.telegram_api_url}{self.token}'
        self.last_update_id = None


    def get_updates(self):
        req = requests.get(f'{self.url}/getUpdates')
        json_data = req.json()
        if not json_data['ok']:
            return {"error": json_data['description']}
        return json_data['result']


    def get_last_update(self):
        updates = self.get_updates()
        if 'error' in updates:
            return updates
        last_update = updates[-1] if updates else None
        if last_update and last_update['update_id'] != self.last_update_id:
            self.last_update_id = last_update['update_id']
        else:
            last_update = None
        return last_update

    def get_message(self):
        last_update = self.get_last_update()
        print (type(last_update))
        if last_update is None:
            return None
        if 'error' in last_update:
            raise ValueError('Non valid update')
        print('text1')
        if 'text' in last_update['message']:    
            return {"chat_id": last_update['message']['chat']['id'],
                    "text": last_update['message']['text']}
        else:
             return {"chat_id": last_update['message']['chat']['id'],
                    "text": last_update['message']['sticker']['emoji']}
        

    def send_message(self, chat_id, text):
        parameters = f'?chat_id={chat_id}&text={text}'
        req = requests.get(f'{self.url}/sendMessage{parameters}')
        if not req.json()['ok']:
            return {"error": req['description']}
        return req.json()
        
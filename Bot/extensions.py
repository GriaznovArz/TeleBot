import requests
import json
from config import *

class APIException(Exception):
    pass

class Convertor:
    @staticmethod
    def get_price(base, sym, amount):
        try:
            base_key = exchanges[base.lower()]
        except KeyError:
            raise APIException(f"Валюта {base} не найдена!")

        try:
            sym_key = exchanges[sym]
        except KeyError:
            raise APIException(f"Валюта {sym} не найдена!")

        if base_key == sym_key:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}!')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}!')

        response = requests.get(f"https://api.apilayer.com/fixer/convert?to={base}&from=\
        {sym}&amount={str(amount)}",headers = headers)
        resp = json.loads(response.text)
        new_price = round(resp["result"],2)
        message = f"Цена {amount} {base} в {sym} : {new_price}"
        return message
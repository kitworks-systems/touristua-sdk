from functools import partialmethod

import requests

from touristua.constants import TransactionType, URLS, PARAMS_BULK
from touristua.params import FrozenParams


class Api:
    def __init__(self, api_key, api_endpoint=''):
        self.api_key = api_key
        self.api_endpoint = api_endpoint

    def _query(self, transaction_type: TransactionType, params: dict or list):
        URL = URLS[transaction_type]
        if PARAMS_BULK[transaction_type]:
            ready_params = []
            if isinstance(params, list):
                for params_unit in params:
                    frozen_params = FrozenParams(transaction_type, params_unit)
                    ready_params.append(frozen_params)
            elif isinstance(params, dict):
                ready_params.append(FrozenParams(transaction_type, params))
        else:
            ready_params = {}
            if isinstance(params, dict):
                ready_params = FrozenParams(transaction_type, params)
            elif isinstance(params, list):
                ready_params = FrozenParams(transaction_type, params[0])
        response = requests.post(URL, json=ready_params, headers={
            "Content-Type": "application/json", "Accept": "application/json", "KEY": self.api_key
        })
        return response.json()

    create_sales = partialmethod(_query, TransactionType.CREATE_SALES)
    update_sales = partialmethod(_query, TransactionType.UPDATE_SALES)
    delete_sales = partialmethod(_query, TransactionType.DELETE_SALES)
    info_ticket = partialmethod(_query, TransactionType.INFO_TICKET)
    change_ticket = partialmethod(_query, TransactionType.CHANGE_TICKET)

from touristua.api import Api

__all__ = ['Touristua']


class Touristua:
    def __init__(self, api_key, api_endpoint=''):
        self.api_key = api_key
        self.api_endpoint = api_endpoint
        self.api = Api(self.api_key, self.api_endpoint)


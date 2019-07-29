from unittest import TestCase
from unittest.mock import patch

import requests

from touristua import Api
from touristua.constants import TransactionType
from touristua.params import ParamRequired
from touristua.utils import get_required_fields


class UtilsTestCase(TestCase):
    def test_get_required_params(self):
        required_fields_sets = get_required_fields(TransactionType.CREATE_SALES)
        self.assertEqual(required_fields_sets, [{'idCompany', 'logo', 'photoGallery', 'outerId', 'salesType', 'name',
                                                 'descr', 'totalTickets', 'tickets', 'paymentChannel',
                                                 'addressRefFormat', 'schedule', 'rate'}])


@patch.object(requests, 'post')
class ApiTestCase(TestCase):
    def setUp(self):
        self.api = Api('acc', 'url')
        self.var = {
            "id": "5b056605787e9b4fdb7be2ab",
            "idCompany": "5b056605787e9b4fdb7be2ab",
            "outerId": "fghgfj565ghjghj56",
            "logo": "http://new-image.jpg",
            "photoGallery": [
                "http://new-image1.jpg", "http://new-image2.jpg"
            ],
            "salesType": {
                "id": "3"
            },
            "name": {
                "locales": [
                    {
                        "lang": "ru",
                        "value": "new_name_ru"
                    },
                    {
                        "lang": "ua",
                        "value": "name_ua"
                    }
                ]
            },
            "descr": {
                "locales": [
                    {
                        "lang": "ru",
                        "value": "new_description_ru"
                    },
                    {
                        "lang": "ua",
                        "value": "new_description_ua"
                    }
                ]
            },
            "totalTickets": 1,
            "tickets": [
                {
                    "ticketNameType": {
                        "id": "0"
                    },
                    "price": 1.34,
                    "total": 1
                }
            ],
            "paymentChannel": {
                "id": "5b30bee3ce4015b81593b9c9",
            },
            "refundList": [
                {
                    "period": {
                        "id": "4",
                    },
                    "amount": {
                        "id": "5",
                    }
                }
            ],
            "priceInclude": {
                "locales": [
                    {
                        "lang": "ru",
                        "value": "new_priceInclude_ru"
                    },
                    {
                        "lang": "ua",
                        "value": "new_priceInclude_ua"
                    }
                ]
            },
            "priceNotInclude": {
                "locales": [
                    {
                        "lang": "ru",
                        "value": "new_priceNotInclude_ru"
                    },
                    {
                        "lang": "ua",
                        "value": "new_priceNotInclude_ua"
                    }
                ]
            },
            "address": {
                "region": "Днепропетровская",
                "city": "Днепр",
                "street": "Набережная Победы",
                "number": "30"
            },
            "coordinate": {
                "latitude": 48.496871,
                "longitude": 35.04045
            },
            "schedule": {
                "scheduleType": "DATE",
                "dateStart": "20180710T00:00",
                "dateFinish": "20180731T00:00",
                "date": [
                    "20180726T14:00"
                ]
            },
            "entertainment": {
                "id": "4"
            },
            "rate": {
                "id": "5b3a2fefe393d45dd4eb4928",
            }
        }

    def test_query(self, post_mock):
        self.assertRaises(ParamRequired, self.api._query, TransactionType.CREATE_SALES, self.var)
        post_mock.assert_not_called()

        self.api._query(TransactionType.UPDATE_SALES, self.var)
        post_mock.assert_called_once()

    def test_query_bulk(self, post_mock):
        self.api._query(TransactionType.UPDATE_SALES, [self.var, ])
        post_mock.assert_called_once()

    def test_shortcuts(self, post_mock):
        self.api.update_sales(self.var)
        post_mock.assert_called_once()
        self.assertEqual(post_mock.call_args[1]['json'][0]['idCompany'], "5b056605787e9b4fdb7be2ab")
        self.assertEqual(post_mock.call_args[1]['headers']['KEY'], "acc")


@patch.object(requests, 'post')
class SalesTestCase(TestCase):
    def setUp(self):
        self.api = Api('acc', 'url')
        self.var_first = {
            "id": "5b056605787e9b4fdb7be2ab",
            "paymentChannel": {
                "id": "5b30bee3ce4015b81593b9c9",
            },
            "rate": {
                "id": "5b3a2fefe393d45dd4eb4928",
            }
        }
        self.var_second = {
            "idCompany": "5b056605787e9b4fdb7be2ab",
            "outerId": "fghgfj565ghjghj56",
            "paymentChannel": {
                "id": "5b30bee3ce4015b81593b9c9",
            },
            "rate": {
                "id": "5b3a2fefe393d45dd4eb4928",
            }
        }
        self.var_all = {
            "id": "5b056605787e9b4fdb7be2ab",
            "idCompany": "5b056605787e9b4fdb7be2ab",
            "outerId": "fghgfj565ghjghj56",
            "paymentChannel": {
                "id": "5b30bee3ce4015b81593b9c9",
            },
            "rate": {
                "id": "5b3a2fefe393d45dd4eb4928",
            }
        }

    def test_first(self, post_mock):
        self.api.update_sales(self.var_first)
        post_mock.assert_called_once()

    def test_second(self, post_mock):
        self.api.update_sales(self.var_second)
        post_mock.assert_called_once()

    def test_second_error(self, post_mock):
        var_error = self.var_second.copy()
        del var_error['outerId']
        self.assertRaises(ParamRequired, self.api._query, TransactionType.UPDATE_SALES, var_error)
        post_mock.assert_not_called()
        self.api._query(TransactionType.UPDATE_SALES, self.var_second)
        post_mock.assert_called_once()

    def test_all(self, post_mock):
        self.api.update_sales(self.var_all)
        post_mock.assert_called_once()

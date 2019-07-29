from enum import Enum


class TransactionType(str, Enum):
    CREATE_SALES = 'CREATE_SALES'
    UPDATE_SALES = 'UPDATE_SALES'
    DELETE_SALES = 'DELETE_SALES'
    INFO_TICKET = 'INFO_TICKET'
    CHANGE_TICKET = 'CHANGE_TICKET'


REQUIRED_FIELDS = {
    TransactionType.CREATE_SALES: [
        [
            'idCompany',
            'logo',
            'photoGallery',
            'outerId',
            'salesType',
            'name',
            'descr',
            'totalTickets',
            'tickets',
            'paymentChannel',
            'addressRefFormat',
            'schedule',
            'rate',
        ],
    ],
    TransactionType.UPDATE_SALES: [
        [
            'id',
            'rate',
            'paymentChannel',

        ],
        [
            'outerId',
            'idCompany',
            'rate',
            'paymentChannel',

        ],
    ],
    TransactionType.DELETE_SALES: [
        [
            'id',
            'outerId',
            'idCompany',
        ],
    ],
    TransactionType.INFO_TICKET: [
        [
            'idSales',
            'seance',
        ],
    ],
    TransactionType.CHANGE_TICKET: [
        [
            'idSales',
            'seance',
            'total',
            'tickets',
            'id',
            'total',
        ],
    ],
}


PARAMS_BULK = {
    TransactionType.CREATE_SALES: True,
    TransactionType.UPDATE_SALES: True,
    TransactionType.DELETE_SALES: True,
    TransactionType.INFO_TICKET: False,
    TransactionType.CHANGE_TICKET: False,
}


URLS = {
    TransactionType.CREATE_SALES: '/public/api/sales/create',
    TransactionType.UPDATE_SALES: '/public/api/sales/update',
    TransactionType.DELETE_SALES: '/public/api/sales/delete',
    TransactionType.INFO_TICKET: '/api/sales/seance/ticket/info',
    TransactionType.CHANGE_TICKET: '/api/sales/seance/ticket/change',
}


ALL_FIELDS = {
    TransactionType.CREATE_SALES: [
        'id',
        'idCompany',
        'logo',
        'photoGallery',
        'outerId',
        'salesType',
        'name',
        'descr',
        'totalTickets',
        'tickets',
        'paymentChannel',
        'refundList',
        'priceInclude',
        'priceNotInclude',
        'addressRefFormat',
        'coordinate',
        'schedule',
        'rate',
    ],
    TransactionType.UPDATE_SALES: [
        'id',
        'outerId',
        'idCompany',
        'rate',
        'paymentChannel',
        'logo',
        'photoGallery',
        'salesType',
        'name',
        'descr',
        'totalTickets',
        'tickets',
        'refundList',
        'priceInclude',
        'priceNotInclude',
        'addressRefFormat',
        'coordinate',
        'schedule',

    ],
    TransactionType.DELETE_SALES: [
        'id',
        'outerId',
        'idCompany',
    ],
    TransactionType.INFO_TICKET: [
        'idSales',
        'seance',
    ],
    TransactionType.CHANGE_TICKET: [
        'idSales',
        'seance',
        'total',
        'tickets',
        'id',
        'total',
    ],
}
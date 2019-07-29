from collections import MutableMapping
from itertools import chain

from touristua.constants import TransactionType, REQUIRED_FIELDS
from touristua.utils import get_required_fields


class ParamRequired(Exception):
    pass


class ParamValidationError(Exception):
    pass


class ParamsBase(MutableMapping):
    def __init__(self, *args, **kwargs):
        self._store = {}
        self.update(dict(*args, **kwargs))

    def __getitem__(self, key):
        return self._store[key]

    def __setitem__(self, key, value):
        self._store[key] = value

    def __delitem__(self, key):
        del self._store[key]

    def __iter__(self):
        return iter(self._store)

    def __len__(self):
        return len(self._store)

    def __contains__(self, key):
        return key in self._store

    def __str__(self):
        return str(self._store)

    def __repr__(self):
        return repr(self._store)


def _val_not_empty_validator(val):
    return bool(val)


def _transaction_type_validator(val):
    try:
        TransactionType(val)
        return True
    except ValueError:
        return False


class Params(ParamsBase):
    validators = {
        **{field: _val_not_empty_validator for field in set(chain.from_iterable(chain.from_iterable(REQUIRED_FIELDS.values())))},
        'transaction_type': _transaction_type_validator,
    }

    def prepare(self, transaction_type: str):
        self._validate_field('transaction_type', transaction_type)
        required_fields = get_required_fields(transaction_type)
        self._require_fields(required_fields)

    def _require_fields(self, fields_sets):
        any_set = []
        required_fields_error = []
        for fields in fields_sets:
            if not isinstance(fields, set):
                fields = set(fields)
            if not fields.issubset(self.keys()):
                required_fields_error.append(', '.join(fields - self.keys()))
            else:
                any_set.append(True)
        if required_fields_error and not any(any_set):
            raise ParamRequired("Required param(s) not found: '{}'".format(
                ' or '.join(required_fields_error)
            ))

    def _validate_field(self, field, val):
        validator = self.validators.get(field)
        if callable(validator) and not validator(val):
            raise ParamValidationError(f"Invalid param: '{field}'")

    def __setitem__(self, key, value):
        self._validate_field(key, value)
        super().__setitem__(key, value)


class FrozenParams(ParamsBase):
    def __init__(self, transaction_type: TransactionType, params: dict):
        super().__init__()
        self._store = Params(**params)
        self._store.prepare(transaction_type.value)

    def __setitem__(self, key, value):
        raise NotImplementedError

    def __delitem__(self, key):
        raise NotImplementedError

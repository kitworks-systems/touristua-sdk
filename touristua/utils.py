from touristua.constants import TransactionType, REQUIRED_FIELDS


def get_required_fields(transaction_type: str) -> list:
    key = TransactionType(transaction_type)
    return [set(fields_set) for fields_set in REQUIRED_FIELDS[key]]

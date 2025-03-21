def filter_by_state(bank_transaction: list[dict], state: str = "EXECUTED") -> list:
    """Функция возврата словарей банковских операций по ключу"""
    state_bank_transaction = []
    for item in bank_transaction:
        if item["state"] == state:
            state_bank_transaction.append(item)
    return state_bank_transaction


def sort_by_date(data_logs: list[dict], reverse: bool = True) -> list:
    """Функция сортировке банковских операций по дате"""
    return sorted(data_logs, key=lambda x: x["date"], reverse=reverse)

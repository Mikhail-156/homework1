from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(name_for_mask: str) -> str:
    """Функция маскировки для карт и счетов"""
    list_ = name_for_mask.split()
    if "Счет" == list_[0]:
        return f"{list_[0]} {get_mask_account(list_[1])}"
    elif list_[1].isdigit():
        return f"{list_[0]} {get_mask_card_number(list_[1])}"
    else:
        return f"{list_[0]} {list_[1]} {get_mask_card_number(list_[-1])}"


def get_date(my_date: str) -> str:
    """Функция смены вормата даты и вреня"""
    date_obj = datetime.strptime(my_date[:10], "%Y-%m-%d")
    return f"{date_obj.day:02}:{date_obj.month:02}:{date_obj.year}"

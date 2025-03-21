from datetime import datetime

from typing import Union

card_number = input()
account_number = input()
"""Получение даных пользователя"""


def get_mask_card_number(card_number: Union[int, str]) -> Union[str]:
    """Функция которя скрывает номет катры"""
    return f"{str(card_number)[:4]}, {str(card_number)[4:7]}**, ****, {str(card_number)[-4:]}"


def get_mask_account(account_number: Union[int, str]) -> Union[str]:
    """Функция которя скрывает номет счета"""
    return f"**{str(account_number)[-4:]}"


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

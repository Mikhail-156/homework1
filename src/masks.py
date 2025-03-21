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

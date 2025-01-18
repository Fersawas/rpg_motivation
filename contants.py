USER_LENGTH = 50
NAME_LENGHT = 150
PASSWORD_LENGTH = 100

EQUIP_LENGTH = 100
EQUIP_TYPE_LENGTH = 50

DEF_POINTS_CHAR = 5
DEF_POINTS_EQ = 0

FIELD_OPTION = {
    'null': True,
    'blank': True
}

USER_VALIDATORS = {
    'username': 'Пользователь с таким именем существует',
    'password': 'Пароли не совпадают'
}

CHAR_EQUIP = {
    'hands': 'Неверный тип для рук',
    'chest': 'Неверный тип для груди',
    'legs': 'Неверный тип для ног',
    'weapon': 'Неверный тип для оружия',
}

EQUIPMENT = {
    'type_err': 'Указан неверный тип'
}
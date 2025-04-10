import enum

class TypeEnum(str, enum.Enum):
    PAID = "на оплату"
    FREE = "счёт без оплаты"

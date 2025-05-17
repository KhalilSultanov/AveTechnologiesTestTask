from pydantic import BaseModel, constr


class WriteData(BaseModel):
    """
    Схема для номера и адреса
    """
    phone: constr(pattern=r"^89\d{9}$")
    address: str

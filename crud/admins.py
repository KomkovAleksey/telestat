from crud.base import CRUDBase
from core import Admins


class CRUDAdmins(CRUDBase):
    """Класс CRUD для дополнительных методов Admins."""
    pass


admins_crud = CRUDAdmins(Admins)

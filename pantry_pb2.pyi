from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PantryItemType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_ITEM_TYPE: _ClassVar[PantryItemType]
    PROTEIN: _ClassVar[PantryItemType]
    VEGETABLE: _ClassVar[PantryItemType]
    FRUIT: _ClassVar[PantryItemType]
    DAIRY: _ClassVar[PantryItemType]
    SPICE: _ClassVar[PantryItemType]
    GRAIN: _ClassVar[PantryItemType]
    OIL: _ClassVar[PantryItemType]
UNKNOWN_ITEM_TYPE: PantryItemType
PROTEIN: PantryItemType
VEGETABLE: PantryItemType
FRUIT: PantryItemType
DAIRY: PantryItemType
SPICE: PantryItemType
GRAIN: PantryItemType
OIL: PantryItemType

class PantryItem(_message.Message):
    __slots__ = ("type", "name", "quantity", "date_acquired", "expiration_date")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    DATE_ACQUIRED_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    type: PantryItemType
    name: str
    quantity: int
    date_acquired: int
    expiration_date: int
    def __init__(self, type: _Optional[_Union[PantryItemType, str]] = ..., name: _Optional[str] = ..., quantity: _Optional[int] = ..., date_acquired: _Optional[int] = ..., expiration_date: _Optional[int] = ...) -> None: ...

class Pantry(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[PantryItem]
    def __init__(self, items: _Optional[_Iterable[_Union[PantryItem, _Mapping]]] = ...) -> None: ...

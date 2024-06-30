import user_pb2 as _user_pb2
import pantry_pb2 as _pantry_pb2
import contact_details_pb2 as _contact_details_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddUserRequest(_message.Message):
    __slots__ = ("name", "address", "contact_details", "pronouns")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CONTACT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    PRONOUNS_FIELD_NUMBER: _ClassVar[int]
    name: _user_pb2.Name
    address: _user_pb2.Address
    contact_details: _contact_details_pb2.ContactDetails
    pronouns: str
    def __init__(self, name: _Optional[_Union[_user_pb2.Name, _Mapping]] = ..., address: _Optional[_Union[_user_pb2.Address, _Mapping]] = ..., contact_details: _Optional[_Union[_contact_details_pb2.ContactDetails, _Mapping]] = ..., pronouns: _Optional[str] = ...) -> None: ...

class AddUserResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ...) -> None: ...

class GetUserRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class GetUserResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ...) -> None: ...

class GetUsersWithinRadiusRequest(_message.Message):
    __slots__ = ("latitude", "longitude", "radius")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    radius: float
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., radius: _Optional[float] = ...) -> None: ...

class GetUsersWithinRadiusResponse(_message.Message):
    __slots__ = ("users",)
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[_user_pb2.User]
    def __init__(self, users: _Optional[_Iterable[_Union[_user_pb2.User, _Mapping]]] = ...) -> None: ...

class AddItemToPantryRequest(_message.Message):
    __slots__ = ("item_id", "user_id")
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    item_id: str
    user_id: str
    def __init__(self, item_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class AddItemToPantryResponse(_message.Message):
    __slots__ = ("user_id", "pantry")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PANTRY_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    pantry: _pantry_pb2.Pantry
    def __init__(self, user_id: _Optional[str] = ..., pantry: _Optional[_Union[_pantry_pb2.Pantry, _Mapping]] = ...) -> None: ...

class GetPantryForUserRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class GetPantryForUserResponse(_message.Message):
    __slots__ = ("user_id", "pantry")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PANTRY_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    pantry: _pantry_pb2.Pantry
    def __init__(self, user_id: _Optional[str] = ..., pantry: _Optional[_Union[_pantry_pb2.Pantry, _Mapping]] = ...) -> None: ...

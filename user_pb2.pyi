import pantry_pb2 as _pantry_pb2
import contact_details_pb2 as _contact_details_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Name(_message.Message):
    __slots__ = ("first", "last", "preferred")
    FIRST_FIELD_NUMBER: _ClassVar[int]
    LAST_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_FIELD_NUMBER: _ClassVar[int]
    first: str
    last: str
    preferred: str
    def __init__(self, first: _Optional[str] = ..., last: _Optional[str] = ..., preferred: _Optional[str] = ...) -> None: ...

class Address(_message.Message):
    __slots__ = ("street1", "street2", "city", "state", "zip", "latitude", "longitude")
    STREET1_FIELD_NUMBER: _ClassVar[int]
    STREET2_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ZIP_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    street1: str
    street2: str
    city: str
    state: str
    zip: str
    latitude: float
    longitude: float
    def __init__(self, street1: _Optional[str] = ..., street2: _Optional[str] = ..., city: _Optional[str] = ..., state: _Optional[str] = ..., zip: _Optional[str] = ..., latitude: _Optional[float] = ..., longitude: _Optional[float] = ...) -> None: ...

class UserDetails(_message.Message):
    __slots__ = ("name", "contact_details", "address", "pronouns")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTACT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PRONOUNS_FIELD_NUMBER: _ClassVar[int]
    name: Name
    contact_details: _contact_details_pb2.ContactDetails
    address: Address
    pronouns: str
    def __init__(self, name: _Optional[_Union[Name, _Mapping]] = ..., contact_details: _Optional[_Union[_contact_details_pb2.ContactDetails, _Mapping]] = ..., address: _Optional[_Union[Address, _Mapping]] = ..., pronouns: _Optional[str] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ("uuid", "user_details", "pantry")
    UUID_FIELD_NUMBER: _ClassVar[int]
    USER_DETAILS_FIELD_NUMBER: _ClassVar[int]
    PANTRY_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    user_details: UserDetails
    pantry: _pantry_pb2.Pantry
    def __init__(self, uuid: _Optional[str] = ..., user_details: _Optional[_Union[UserDetails, _Mapping]] = ..., pantry: _Optional[_Union[_pantry_pb2.Pantry, _Mapping]] = ...) -> None: ...

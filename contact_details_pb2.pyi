from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PhoneNumberType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_NUMBER_TYPE: _ClassVar[PhoneNumberType]
    HOME: _ClassVar[PhoneNumberType]
    CELL: _ClassVar[PhoneNumberType]
    WORK: _ClassVar[PhoneNumberType]

class AlternativeContactType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_CONTACT_TYPE: _ClassVar[AlternativeContactType]
    FACEBOOK_MESSENGER: _ClassVar[AlternativeContactType]
    INSTAGRAM: _ClassVar[AlternativeContactType]
    TWITTER: _ClassVar[AlternativeContactType]
    DISCORD: _ClassVar[AlternativeContactType]
UNKNOWN_NUMBER_TYPE: PhoneNumberType
HOME: PhoneNumberType
CELL: PhoneNumberType
WORK: PhoneNumberType
UNKNOWN_CONTACT_TYPE: AlternativeContactType
FACEBOOK_MESSENGER: AlternativeContactType
INSTAGRAM: AlternativeContactType
TWITTER: AlternativeContactType
DISCORD: AlternativeContactType

class PhoneNumber(_message.Message):
    __slots__ = ("type", "number")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    type: PhoneNumberType
    number: str
    def __init__(self, type: _Optional[_Union[PhoneNumberType, str]] = ..., number: _Optional[str] = ...) -> None: ...

class AlternativeContactInfo(_message.Message):
    __slots__ = ("type", "screen_name")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SCREEN_NAME_FIELD_NUMBER: _ClassVar[int]
    type: AlternativeContactType
    screen_name: str
    def __init__(self, type: _Optional[_Union[AlternativeContactType, str]] = ..., screen_name: _Optional[str] = ...) -> None: ...

class ContactDetails(_message.Message):
    __slots__ = ("numbers", "alternative_contact_methods", "emails")
    NUMBERS_FIELD_NUMBER: _ClassVar[int]
    ALTERNATIVE_CONTACT_METHODS_FIELD_NUMBER: _ClassVar[int]
    EMAILS_FIELD_NUMBER: _ClassVar[int]
    numbers: _containers.RepeatedCompositeFieldContainer[PhoneNumber]
    alternative_contact_methods: _containers.RepeatedCompositeFieldContainer[AlternativeContactInfo]
    emails: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, numbers: _Optional[_Iterable[_Union[PhoneNumber, _Mapping]]] = ..., alternative_contact_methods: _Optional[_Iterable[_Union[AlternativeContactInfo, _Mapping]]] = ..., emails: _Optional[_Iterable[str]] = ...) -> None: ...

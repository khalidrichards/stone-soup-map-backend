# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: backend_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import user_pb2 as user__pb2
import pantry_pb2 as pantry__pb2
import contact_details_pb2 as contact__details__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x62\x61\x63kend_service.proto\x1a\nuser.proto\x1a\x0cpantry.proto\x1a\x15\x63ontact_details.proto\"|\n\x0e\x41\x64\x64UserRequest\x12\x13\n\x04name\x18\x01 \x01(\x0b\x32\x05.Name\x12\x19\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x08.Address\x12(\n\x0f\x63ontact_details\x18\x03 \x01(\x0b\x32\x0f.ContactDetails\x12\x10\n\x08pronouns\x18\x04 \x01(\t\"&\n\x0f\x41\x64\x64UserResponse\x12\x13\n\x04user\x18\x01 \x01(\x0b\x32\x05.User\"!\n\x0eGetUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"&\n\x0fGetUserResponse\x12\x13\n\x04user\x18\x01 \x01(\x0b\x32\x05.User\"R\n\x1bGetUsersWithinRadiusRequest\x12\x10\n\x08latitude\x18\x01 \x01(\x01\x12\x11\n\tlongitude\x18\x02 \x01(\x01\x12\x0e\n\x06radius\x18\x03 \x01(\x01\"4\n\x1cGetUsersWithinRadiusResponse\x12\x14\n\x05users\x18\x01 \x03(\x0b\x32\x05.User\":\n\x16\x41\x64\x64ItemToPantryRequest\x12\x0f\n\x07item_id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\"C\n\x17\x41\x64\x64ItemToPantryResponse\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x17\n\x06pantry\x18\x02 \x01(\x0b\x32\x07.Pantry\"*\n\x17GetPantryForUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"D\n\x18GetPantryForUserResponse\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x17\n\x06pantry\x18\x02 \x01(\x0b\x32\x07.Pantry2\xd0\x02\n\x0e\x42\x61\x63kendService\x12,\n\x07\x41\x64\x64User\x12\x0f.AddUserRequest\x1a\x10.AddUserResponse\x12,\n\x07GetUser\x12\x0f.GetUserRequest\x1a\x10.GetUserResponse\x12S\n\x14GetUsersWithinRadius\x12\x1c.GetUsersWithinRadiusRequest\x1a\x1d.GetUsersWithinRadiusResponse\x12\x44\n\x0f\x41\x64\x64ItemToPantry\x12\x17.AddItemToPantryRequest\x1a\x18.AddItemToPantryResponse\x12G\n\x10GetPantryForUser\x12\x18.GetPantryForUserRequest\x1a\x19.GetPantryForUserResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'backend_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ADDUSERREQUEST']._serialized_start=74
  _globals['_ADDUSERREQUEST']._serialized_end=198
  _globals['_ADDUSERRESPONSE']._serialized_start=200
  _globals['_ADDUSERRESPONSE']._serialized_end=238
  _globals['_GETUSERREQUEST']._serialized_start=240
  _globals['_GETUSERREQUEST']._serialized_end=273
  _globals['_GETUSERRESPONSE']._serialized_start=275
  _globals['_GETUSERRESPONSE']._serialized_end=313
  _globals['_GETUSERSWITHINRADIUSREQUEST']._serialized_start=315
  _globals['_GETUSERSWITHINRADIUSREQUEST']._serialized_end=397
  _globals['_GETUSERSWITHINRADIUSRESPONSE']._serialized_start=399
  _globals['_GETUSERSWITHINRADIUSRESPONSE']._serialized_end=451
  _globals['_ADDITEMTOPANTRYREQUEST']._serialized_start=453
  _globals['_ADDITEMTOPANTRYREQUEST']._serialized_end=511
  _globals['_ADDITEMTOPANTRYRESPONSE']._serialized_start=513
  _globals['_ADDITEMTOPANTRYRESPONSE']._serialized_end=580
  _globals['_GETPANTRYFORUSERREQUEST']._serialized_start=582
  _globals['_GETPANTRYFORUSERREQUEST']._serialized_end=624
  _globals['_GETPANTRYFORUSERRESPONSE']._serialized_start=626
  _globals['_GETPANTRYFORUSERRESPONSE']._serialized_end=694
  _globals['_BACKENDSERVICE']._serialized_start=697
  _globals['_BACKENDSERVICE']._serialized_end=1033
# @@protoc_insertion_point(module_scope)

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vtrpc.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='vtrpc.proto',
  package='vtrpc',
  syntax='proto3',
  serialized_pb=_b('\n\x0bvtrpc.proto\x12\x05vtrpc\"F\n\x08\x43\x61llerID\x12\x11\n\tprincipal\x18\x01 \x01(\t\x12\x11\n\tcomponent\x18\x02 \x01(\t\x12\x14\n\x0csubcomponent\x18\x03 \x01(\t\";\n\x08RPCError\x12\x1e\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x10.vtrpc.ErrorCode\x12\x0f\n\x07message\x18\x02 \x01(\t*\x87\x02\n\tErrorCode\x12\x0b\n\x07SUCCESS\x10\x00\x12\r\n\tCANCELLED\x10\x01\x12\x11\n\rUNKNOWN_ERROR\x10\x02\x12\r\n\tBAD_INPUT\x10\x03\x12\x15\n\x11\x44\x45\x41\x44LINE_EXCEEDED\x10\x04\x12\x13\n\x0fINTEGRITY_ERROR\x10\x05\x12\x15\n\x11PERMISSION_DENIED\x10\x06\x12\x16\n\x12RESOURCE_EXHAUSTED\x10\x07\x12\x14\n\x10QUERY_NOT_SERVED\x10\x08\x12\r\n\tNOT_IN_TX\x10\t\x12\x12\n\x0eINTERNAL_ERROR\x10\n\x12\x13\n\x0fTRANSIENT_ERROR\x10\x0b\x12\x13\n\x0fUNAUTHENTICATED\x10\x0c\x42\x1a\n\x18\x63om.youtube.vitess.protob\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_ERRORCODE = _descriptor.EnumDescriptor(
  name='ErrorCode',
  full_name='vtrpc.ErrorCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANCELLED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_ERROR', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAD_INPUT', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEADLINE_EXCEEDED', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTEGRITY_ERROR', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERMISSION_DENIED', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESOURCE_EXHAUSTED', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUERY_NOT_SERVED', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_IN_TX', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_ERROR', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRANSIENT_ERROR', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNAUTHENTICATED', index=12, number=12,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=156,
  serialized_end=419,
)
_sym_db.RegisterEnumDescriptor(_ERRORCODE)

ErrorCode = enum_type_wrapper.EnumTypeWrapper(_ERRORCODE)
SUCCESS = 0
CANCELLED = 1
UNKNOWN_ERROR = 2
BAD_INPUT = 3
DEADLINE_EXCEEDED = 4
INTEGRITY_ERROR = 5
PERMISSION_DENIED = 6
RESOURCE_EXHAUSTED = 7
QUERY_NOT_SERVED = 8
NOT_IN_TX = 9
INTERNAL_ERROR = 10
TRANSIENT_ERROR = 11
UNAUTHENTICATED = 12



_CALLERID = _descriptor.Descriptor(
  name='CallerID',
  full_name='vtrpc.CallerID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='principal', full_name='vtrpc.CallerID.principal', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='component', full_name='vtrpc.CallerID.component', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='subcomponent', full_name='vtrpc.CallerID.subcomponent', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=92,
)


_RPCERROR = _descriptor.Descriptor(
  name='RPCError',
  full_name='vtrpc.RPCError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='vtrpc.RPCError.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='vtrpc.RPCError.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=94,
  serialized_end=153,
)

_RPCERROR.fields_by_name['code'].enum_type = _ERRORCODE
DESCRIPTOR.message_types_by_name['CallerID'] = _CALLERID
DESCRIPTOR.message_types_by_name['RPCError'] = _RPCERROR
DESCRIPTOR.enum_types_by_name['ErrorCode'] = _ERRORCODE

CallerID = _reflection.GeneratedProtocolMessageType('CallerID', (_message.Message,), dict(
  DESCRIPTOR = _CALLERID,
  __module__ = 'vtrpc_pb2'
  # @@protoc_insertion_point(class_scope:vtrpc.CallerID)
  ))
_sym_db.RegisterMessage(CallerID)

RPCError = _reflection.GeneratedProtocolMessageType('RPCError', (_message.Message,), dict(
  DESCRIPTOR = _RPCERROR,
  __module__ = 'vtrpc_pb2'
  # @@protoc_insertion_point(class_scope:vtrpc.RPCError)
  ))
_sym_db.RegisterMessage(RPCError)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\030com.youtube.vitess.proto'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)

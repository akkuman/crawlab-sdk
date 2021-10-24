# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: services/task_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from entity import request_pb2 as entity_dot_request__pb2
from entity import response_pb2 as entity_dot_response__pb2
from entity import stream_message_pb2 as entity_dot_stream__message__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='services/task_service.proto',
  package='grpc',
  syntax='proto3',
  serialized_options=b'Z\006.;grpc',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1bservices/task_service.proto\x12\x04grpc\x1a\x14\x65ntity/request.proto\x1a\x15\x65ntity/response.proto\x1a\x1b\x65ntity/stream_message.proto2u\n\x0bTaskService\x12\x34\n\tSubscribe\x12\x13.grpc.StreamMessage\x1a\x0e.grpc.Response\"\x00(\x01\x12\x30\n\rGetDataSource\x12\r.grpc.Request\x1a\x0e.grpc.Response\"\x00\x42\x08Z\x06.;grpcb\x06proto3'
  ,
  dependencies=[entity_dot_request__pb2.DESCRIPTOR,entity_dot_response__pb2.DESCRIPTOR,entity_dot_stream__message__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_TASKSERVICE = _descriptor.ServiceDescriptor(
  name='TaskService',
  full_name='grpc.TaskService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=111,
  serialized_end=228,
  methods=[
  _descriptor.MethodDescriptor(
    name='Subscribe',
    full_name='grpc.TaskService.Subscribe',
    index=0,
    containing_service=None,
    input_type=entity_dot_stream__message__pb2._STREAMMESSAGE,
    output_type=entity_dot_response__pb2._RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetDataSource',
    full_name='grpc.TaskService.GetDataSource',
    index=1,
    containing_service=None,
    input_type=entity_dot_request__pb2._REQUEST,
    output_type=entity_dot_response__pb2._RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TASKSERVICE)

DESCRIPTOR.services_by_name['TaskService'] = _TASKSERVICE

# @@protoc_insertion_point(module_scope)

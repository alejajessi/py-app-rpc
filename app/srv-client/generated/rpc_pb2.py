# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rpc.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\trpc.proto\".\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08greeting\x18\x02 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"?\n\x0c\x44\x65layedReply\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x1e\n\x07request\x18\x02 \x03(\x0b\x32\r.HelloRequest\"\x0e\n\x0c\x45mptyMessage\"\x1b\n\x0cMessageReply\x12\x0b\n\x03\x61\x63k\x18\x01 \x01(\t2\x80\x02\n\x08RcpTypes\x12.\n\x0eNothingMessage\x12\r.EmptyMessage\x1a\r.MessageReply\x12&\n\x08SayHello\x12\r.HelloRequest\x1a\x0b.HelloReply\x12/\n\x0fParrotSaysHello\x12\r.HelloRequest\x1a\x0b.HelloReply0\x01\x12\x37\n\x15\x43hattyClientSaysHello\x12\r.HelloRequest\x1a\r.DelayedReply(\x01\x12\x32\n\x10InteractingHello\x12\r.HelloRequest\x1a\x0b.HelloReply(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'rpc_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_HELLOREQUEST']._serialized_start=13
  _globals['_HELLOREQUEST']._serialized_end=59
  _globals['_HELLOREPLY']._serialized_start=61
  _globals['_HELLOREPLY']._serialized_end=90
  _globals['_DELAYEDREPLY']._serialized_start=92
  _globals['_DELAYEDREPLY']._serialized_end=155
  _globals['_EMPTYMESSAGE']._serialized_start=157
  _globals['_EMPTYMESSAGE']._serialized_end=171
  _globals['_MESSAGEREPLY']._serialized_start=173
  _globals['_MESSAGEREPLY']._serialized_end=200
  _globals['_RCPTYPES']._serialized_start=203
  _globals['_RCPTYPES']._serialized_end=459
# @@protoc_insertion_point(module_scope)

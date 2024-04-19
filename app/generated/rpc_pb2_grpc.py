# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import rpc_pb2 as rpc__pb2


class RcpTypesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.NothingMessage = channel.unary_unary(
                '/RcpTypes/NothingMessage',
                request_serializer=rpc__pb2.EmptyMessage.SerializeToString,
                response_deserializer=rpc__pb2.MessageReply.FromString,
                )
        self.SayHello = channel.unary_unary(
                '/RcpTypes/SayHello',
                request_serializer=rpc__pb2.HelloRequest.SerializeToString,
                response_deserializer=rpc__pb2.HelloReply.FromString,
                )
        self.ParrotSaysHello = channel.unary_stream(
                '/RcpTypes/ParrotSaysHello',
                request_serializer=rpc__pb2.HelloRequest.SerializeToString,
                response_deserializer=rpc__pb2.HelloReply.FromString,
                )
        self.ChattyClientSaysHello = channel.stream_unary(
                '/RcpTypes/ChattyClientSaysHello',
                request_serializer=rpc__pb2.HelloRequest.SerializeToString,
                response_deserializer=rpc__pb2.DelayedReply.FromString,
                )
        self.InteractingHello = channel.stream_stream(
                '/RcpTypes/InteractingHello',
                request_serializer=rpc__pb2.HelloRequest.SerializeToString,
                response_deserializer=rpc__pb2.HelloReply.FromString,
                )


class RcpTypesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def NothingMessage(self, request, context):
        """Basic
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SayHello(self, request, context):
        """Unary
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ParrotSaysHello(self, request, context):
        """Server Streaming
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChattyClientSaysHello(self, request_iterator, context):
        """Client Streaming
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InteractingHello(self, request_iterator, context):
        """Both Streaming
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RcpTypesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'NothingMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.NothingMessage,
                    request_deserializer=rpc__pb2.EmptyMessage.FromString,
                    response_serializer=rpc__pb2.MessageReply.SerializeToString,
            ),
            'SayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello,
                    request_deserializer=rpc__pb2.HelloRequest.FromString,
                    response_serializer=rpc__pb2.HelloReply.SerializeToString,
            ),
            'ParrotSaysHello': grpc.unary_stream_rpc_method_handler(
                    servicer.ParrotSaysHello,
                    request_deserializer=rpc__pb2.HelloRequest.FromString,
                    response_serializer=rpc__pb2.HelloReply.SerializeToString,
            ),
            'ChattyClientSaysHello': grpc.stream_unary_rpc_method_handler(
                    servicer.ChattyClientSaysHello,
                    request_deserializer=rpc__pb2.HelloRequest.FromString,
                    response_serializer=rpc__pb2.DelayedReply.SerializeToString,
            ),
            'InteractingHello': grpc.stream_stream_rpc_method_handler(
                    servicer.InteractingHello,
                    request_deserializer=rpc__pb2.HelloRequest.FromString,
                    response_serializer=rpc__pb2.HelloReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'RcpTypes', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RcpTypes(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def NothingMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RcpTypes/NothingMessage',
            rpc__pb2.EmptyMessage.SerializeToString,
            rpc__pb2.MessageReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RcpTypes/SayHello',
            rpc__pb2.HelloRequest.SerializeToString,
            rpc__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ParrotSaysHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/RcpTypes/ParrotSaysHello',
            rpc__pb2.HelloRequest.SerializeToString,
            rpc__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChattyClientSaysHello(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/RcpTypes/ChattyClientSaysHello',
            rpc__pb2.HelloRequest.SerializeToString,
            rpc__pb2.DelayedReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InteractingHello(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/RcpTypes/InteractingHello',
            rpc__pb2.HelloRequest.SerializeToString,
            rpc__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
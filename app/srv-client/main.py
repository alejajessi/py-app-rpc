from generated import rpc_pb2
from generated import rpc_pb2_grpc
import grpc
import time
import enum
import argparse

def get_reader_stream_requests():
    while True:
        name = input("Please enter a  name:")
        if name == "":
            break

        hello_request = rpc_pb2.HelloRequest(greeting = "Hello", name = name)
        yield hello_request
        time.sleep(1)

class RpcType(enum.Enum):
    BASIC = 0
    UNARY = 1
    SERVER_STREAMING = 2
    CLIENT_STREAMING = 3
    BIDIRECTIONAL_STREAMING = 4

def parse_arguments():
    parser = argparse.ArgumentParser(description='Run different types of gRPC calls.')
    parser.add_argument('--type', type=int, choices=[rpc.value for rpc in RpcType], required=True, help='Specify the type of RPC call to make.')
    return parser.parse_args()

def create_stub():
    channel = grpc.insecure_channel('localhost:50051')
    stub = rpc_pb2_grpc.RcpTypesStub(channel)
    return channel, stub

def perform_nothing_message(stub):
    print ("Nothing Message")
    empty_request = rpc_pb2.EmptyMessage()
    empty_reply = stub.NothingMessage(empty_request)
    print(empty_reply)

def perform_unary_call(stub):
    print ("Unary Message")
    hello_request = rpc_pb2.HelloRequest(greeting = "Hello", name = "User")
    hello_reply = stub.SayHello(hello_request)
    print (hello_reply)

def perform_server_streaming_call(stub):
    print ("Server Streaming Message")
    hello_request = rpc_pb2.HelloRequest(greeting = "Hello", name = "User")
    hello_replies = stub.ParrotSaysHello(hello_request)
    for hello_reply in hello_replies:
        print("The result of server streaming rpc implementation is :")
        print(hello_reply)

def perform_client_streaming_call(stub):
    print ("Client Streaming Message")
    delayed_reply = stub.ChattyClientSaysHello(get_reader_stream_requests())
    print (delayed_reply)

def perform_bidirectional_streaming_call(stub):
    print ("Bidirectional Streaming Message")
    replies =stub.InteractingHello(get_reader_stream_requests())
    for hello_reply in replies:
        print("The result of bidirectional streaming rpc implementation is :")
        print(hello_reply)

def main():
    args = parse_arguments()
    rpc_type = RpcType(args.type)
    channel, stub = create_stub()
    operation_mapping = {
        RpcType.BASIC: perform_nothing_message(stub),
        RpcType.UNARY: perform_unary_call(stub),
        RpcType.SERVER_STREAMING: perform_server_streaming_call(stub),
        RpcType.CLIENT_STREAMING: perform_client_streaming_call(stub),
        RpcType.BIDIRECTIONAL_STREAMING: perform_bidirectional_streaming_call(stub)
    }
    with channel:
        operation = operation_mapping.get(rpc_type)
        if operation:
            operation(stub)
        else:
            print("Invalid RPC type specified.")

if __name__ == "__main__":
    main()

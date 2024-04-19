import rpc_pb2_grpc
import rpc_pb2
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

# Define other RPC functions (perform_nothing_message, perform_unary_call, etc.)

def main():
    args = parse_arguments()
    rpc_type = RpcType(args.type)

    operation_mapping = {
        RpcType.BASIC: perform_nothing_message(),
        RpcType.UNARY: perform_unary_call,
        RpcType.SERVER_STREAMING: perform_server_streaming_call,
        RpcType.CLIENT_STREAMING: perform_client_streaming_call,
        RpcType.BIDIRECTIONAL_STREAMING: perform_bidirectional_streaming_call
    }

    channel, stub = create_stub()
    with channel:
        operation = operation_mapping.get(rpc_type)
        if operation:
            operation(stub)
        else:
            print("Invalid RPC type specified.")

if __name__ == "__main__":
    main()

import rpc_pb2_grpc
import rpc_pb2
import grpc
import time

def get_reader_stream_requests():
    while True:
        name = input("Please enter a  name:")
        if name == "":
            break

        hello_request = rpc_pb2.HelloRequest(greeting = "Hello", name = name)
        yield hello_request
        time.sleep(1)

def main():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = rpc_pb2_grpc.RcpTypesStub(channel)
        print("0. Basics")
        print("1. Unary")
        print("2. Server Side Streaming")
        print("3. Client Side Streaming")
        print("4. Both Streaming")
        rpc_input = input("Which rcp would you like to make?:")

        if rpc_input == "0":
            print("This is a basic rpc implementation with empty message and just an ack")
            empty_request = rpc_pb2.EmptyMessage()
            empty_reply = stub.NothingMessage(empty_request)
            print('The result of basic rpc implementation is :')
            print(empty_reply)

        elif rpc_input == "1":
            print("This is a unary rpc implementation (SayHello)")
            hello_request = rpc_pb2.HelloRequest(greeting = "Hello", name = "User")
            hello_reply = stub.SayHello(hello_request)
            print("The result of unary rpc implementation is :")
            print(hello_reply)

        elif rpc_input == "2":
            print("This is a server streaming rpc implementation (ParrotSayHello)")
            hello_request = rpc_pb2.HelloRequest(greeting = "Hello", name = "User")
            hello_replies = stub. ParrotSaysHello(hello_request)

            for hello_reply in hello_replies:
                print("The result of server streaming rpc implementation is :")
                print(hello_reply)

        elif rpc_input == "3":
            print("This is a client streaming rpc implementation (ChattyClientSaysHello)")
            delayed_reply = stub.ChattyClientSaysHello(get_reader_stream_requests())
            print("The result of client streaming rpc implementation is :")
            print(delayed_reply)

        elif rpc_input == "4":
            print("This is a both streaming rpc implementation (InteractingHello)")
            replies =stub.InteractingHello(get_reader_stream_requests())
            for reply in replies:
                print("The result of client streaming rpc implementation is :")
                print(reply)


if __name__ == "__main__":
    main()

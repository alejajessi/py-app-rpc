import grpc
from generated import rpc_pb2
from generated import rpc_pb2_grpc
import time
from concurrent import futures
## virtual env local para probar local 

class RpcService(rpc_pb2_grpc.RcpTypesServicer): 
    def NothingMessage(self, request, context):
        print("Empty Request:")
        empty_reply = rpc_pb2.MessageReply(ack = '1')
        
        return empty_reply
    
    def SayHello(self, request, context):
        print("SayHello Request:")
        print(request)
        hello_reply = rpc_pb2.HelloReply()
        hello_reply.message = f"{request.greeting} {request.name}"

        return hello_reply
    
    def ParrotSaysHello(self, request, context):
        print("ParrotSaysHello Request:")
        print(request)

        for i in range(3):
            hello_reply = rpc_pb2.HelloReply()
            hello_reply.message = f"{request.greeting} {request.name} {i + 1}"
            yield hello_reply
            time.sleep(3)

    def ChattyClientSaysHello(self, request_iterator, context):
        delayed_reply = rpc_pb2.DelayedReply()
        for request in request_iterator:
            print("ChattyClientSaysHello Request:")
            print(request)
            delayed_reply.request.append(request)

        delayed_reply.message = f"You have sent {len(delayed_reply.request)} messages. Please expect a delayed response."
        return delayed_reply

    def InteractingHello(self, request_iterator, context):
        for request in request_iterator:
            print("InteractingHello Request:")
            print(request)

            hello_reply = rpc_pb2.HelloReply()
            hello_reply.message = f"{request.greeting} {request.name}"

            yield hello_reply


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rpc_pb2_grpc.add_RcpTypesServicer_to_server(RpcService(), server)

    server.add_insecure_port('[::]:50051')
    server.start() ## Iniciamos el server

    print("GRPC server is WORKING!!!") ## Mensaje para ver si el servicio está funcionando
    server.wait_for_termination() ## Para que no se caiga el microservicio, aunque no haya nadie invocandolo

if __name__ == "__main__":
    main()


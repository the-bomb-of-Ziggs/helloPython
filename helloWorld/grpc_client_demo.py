
#python3 -m pip install grpcio-tools
#python3 -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. ./MsgPmCmd.proto
## 教程地址：https://grpc.io/docs/languages/python/quickstart/
import grpc
from helloWorld import hellogrpc_pb2,hellogrpc_pb2_grpc
from helloWorld import MsgPmCmd_pb2,MsgPmCmd_pb2_grpc


_HOST = 'localhost'
_PORT = '8888'
import json

def run():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)  # 监听频道
    # print(conn)
    client = hellogrpc_pb2_grpc.GreeterStub(channel=conn)  # 客户端使用Stub类发送请求,参数为频道,为了绑定链接
    # client = hellogrpc_pb2_grpc.GreeterStub(channel=conn)  # 客户端使用Stub类发送请求,参数为频道,为了绑定链接
    # print(client)
    response = client.SayHello(hellogrpc_pb2.HelloRequest(name='you'))
    # response = client.SayHello(MsgPmCmd_pb2.MsgPmCmdC2S(strData='adduserexp 1000'))
    print("Greeter client received: " + response.message)

## 报错处理：AttributeError: module 'google.protobuf.descriptor' has no attribute '_internal_create_key'，这个是pip安装的protobuf和protoc版本不一致导致的
if __name__ == '__main__':
    run()
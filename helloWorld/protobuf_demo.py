#encoding=utf8
'''
python 安装Protobuffer，到官网下载安装包 protobuf-python-3.5.1.tar.gz，解压后进入python-protobuf-3.5.1/python目录，执行python setup.py install或者pip install protobuf就可以了，
然后windows下下载二进制包，将解压出来的protoc 文件路径加到path变量中，就可以使用protoc 编译文件了 使用命令protoc  --python_out=.  msg.proto会生成一个Python文件，引用这个文件就可以执行下面的操作了。

'''
from helloWorld import msg_pb2
from helloWorld import hellogrpc_pb2

account = msg_pb2.Account()

#序列化输出
account.accountName ='test001'
account.pwd = '222222222'
ser = account.SerializeToString()
print(ser)

#从文件中读取然后反序列化
account.ParseFromString(open('./proto_output.data','rb').read())
print(account)
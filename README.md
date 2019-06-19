# grpc-python3-for-fun-and-profit
Testing grpc with python3 for tech sharing


# Build

python3 -m grpc_tools.protoc -I./protobuf --python_out=messages --grpc_python_out=messages ./protobuf/stdmetadata.proto 

# Source

https://medium.com/@biplav.nep/grpc-using-flask-restful-code-2ed5607ae9a

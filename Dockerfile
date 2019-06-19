FROM python:3.6
COPY . .
ENV PYTHONPATH "${PYTHONPATH}:/messages:/services"
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN python3 -m grpc_tools.protoc -I./protobuf --python_out=messages --grpc_python_out=messages ./protobuf/stdmetadata.proto
EXPOSE 50021
CMD [ "python3", "./server.py" ]
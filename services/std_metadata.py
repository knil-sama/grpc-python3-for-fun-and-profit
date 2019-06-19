import grpc
import messages.stdmetadata_pb2_grpc as stdmetadata_pb2_service
import messages.stdmetadata_pb2 as stdmetadata_pb2_messages
import logging
import time
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp

class StdMetadataService(stdmetadata_pb2_service.StdMetadataServicer):

    def GetStdMetadata(self):
        return stdmetadata_pb2_messages.StdMetadataResponse()
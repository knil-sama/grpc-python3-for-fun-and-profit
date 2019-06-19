from  concurrent import futures
import time
import grpc
import messages.stdmetadata_pb2_grpc as std_service
from services.std_metadata import StdMetadataService
import logging
_ONE_DAY_IN_SECONDS = 60 * 60 * 24
def grpc_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # Register std service
    stdmetadata_serve = StdMetadataService()
    std_service.add_StdMetadataServicer_to_server(stdmetadata_serve, server)
    server.add_insecure_port('[::]:50021')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        logging.debug('GRPC stop')
        server.stop(0)
if __name__ == '__main__':
    grpc_server()
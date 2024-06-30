# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import backend_service_pb2 as backend__service__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in backend_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class BackendServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddUser = channel.unary_unary(
                '/BackendService/AddUser',
                request_serializer=backend__service__pb2.AddUserRequest.SerializeToString,
                response_deserializer=backend__service__pb2.AddUserResponse.FromString,
                _registered_method=True)
        self.GetUser = channel.unary_unary(
                '/BackendService/GetUser',
                request_serializer=backend__service__pb2.GetUserRequest.SerializeToString,
                response_deserializer=backend__service__pb2.GetUserResponse.FromString,
                _registered_method=True)
        self.GetUsersWithinRadius = channel.unary_unary(
                '/BackendService/GetUsersWithinRadius',
                request_serializer=backend__service__pb2.GetUsersWithinRadiusRequest.SerializeToString,
                response_deserializer=backend__service__pb2.GetUsersWithinRadiusResponse.FromString,
                _registered_method=True)
        self.AddItemToPantry = channel.unary_unary(
                '/BackendService/AddItemToPantry',
                request_serializer=backend__service__pb2.AddItemToPantryRequest.SerializeToString,
                response_deserializer=backend__service__pb2.AddItemToPantryResponse.FromString,
                _registered_method=True)
        self.GetPantryForUser = channel.unary_unary(
                '/BackendService/GetPantryForUser',
                request_serializer=backend__service__pb2.GetPantryForUserRequest.SerializeToString,
                response_deserializer=backend__service__pb2.GetPantryForUserResponse.FromString,
                _registered_method=True)


class BackendServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddUser(self, request, context):
        """User rpc calls 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUsersWithinRadius(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddItemToPantry(self, request, context):
        """Pantry rpc calls 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPantryForUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BackendServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddUser': grpc.unary_unary_rpc_method_handler(
                    servicer.AddUser,
                    request_deserializer=backend__service__pb2.AddUserRequest.FromString,
                    response_serializer=backend__service__pb2.AddUserResponse.SerializeToString,
            ),
            'GetUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUser,
                    request_deserializer=backend__service__pb2.GetUserRequest.FromString,
                    response_serializer=backend__service__pb2.GetUserResponse.SerializeToString,
            ),
            'GetUsersWithinRadius': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUsersWithinRadius,
                    request_deserializer=backend__service__pb2.GetUsersWithinRadiusRequest.FromString,
                    response_serializer=backend__service__pb2.GetUsersWithinRadiusResponse.SerializeToString,
            ),
            'AddItemToPantry': grpc.unary_unary_rpc_method_handler(
                    servicer.AddItemToPantry,
                    request_deserializer=backend__service__pb2.AddItemToPantryRequest.FromString,
                    response_serializer=backend__service__pb2.AddItemToPantryResponse.SerializeToString,
            ),
            'GetPantryForUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPantryForUser,
                    request_deserializer=backend__service__pb2.GetPantryForUserRequest.FromString,
                    response_serializer=backend__service__pb2.GetPantryForUserResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'BackendService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('BackendService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class BackendService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/BackendService/AddUser',
            backend__service__pb2.AddUserRequest.SerializeToString,
            backend__service__pb2.AddUserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/BackendService/GetUser',
            backend__service__pb2.GetUserRequest.SerializeToString,
            backend__service__pb2.GetUserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetUsersWithinRadius(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/BackendService/GetUsersWithinRadius',
            backend__service__pb2.GetUsersWithinRadiusRequest.SerializeToString,
            backend__service__pb2.GetUsersWithinRadiusResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def AddItemToPantry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/BackendService/AddItemToPantry',
            backend__service__pb2.AddItemToPantryRequest.SerializeToString,
            backend__service__pb2.AddItemToPantryResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetPantryForUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/BackendService/GetPantryForUser',
            backend__service__pb2.GetPantryForUserRequest.SerializeToString,
            backend__service__pb2.GetPantryForUserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

import backend_service_pb2
import backend_service_pb2_grpc
import user_pb2
import user_pb2_grpc
import contact_details_pb2
import contact_details_pb2_grpc

class BackendServer(backend_service_pb2_grpc.BackendServiceServicer):
    def AddUser(self, request, context):
        return backend_service_pb2.AddUserResponse(
            user=user_pb2.User(
                uuid='user123',
                user_details=user_pb2.UserDetails(
                    name=user_pb2.Name(
                        first='Khal',
                        last='Rich',
                        preferred='K R'
                    ),
                    contact_details=contact_details_pb2.ContactDetails(
                        numbers=[
                            contact_details_pb2.PhoneNumber(
                                type=contact_details_pb2.PhoneNumberType.CELL,
                                number='3104849901'
                            )
                        ],
                        alternative_contact_methods=None,
                        emails= [ 'fake@email.com' ]
                    ),
                    address=user_pb2.Address(
                        street1='123 Fake Street',
                        street2='Apartment 69420',
                        city='Brooklyn',
                        state='NY',
                        zip='11216',
                        latitude=40.678177,
                        longitude=-73.944160
                    ),
                    pronouns='he/him',
                )
            )
        )
    
    def GetUser(self, request, context):
        return None

    def GetUsersWithinRadius(self, request, context):
        return None
    
    def AddItemToPantry(self, request, context):
        return None
    
    def GetPantryForUser(self, request, context):
        return None
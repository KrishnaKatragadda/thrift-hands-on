from gen_py.user_profile import UserProfileService
from gen_py.user_profile.ttypes import User

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class UserProfileHandler:
    def __init__(self):

        self.users = {
    1: User(id=1, name="Alice", email="alice@example.com", phone_number="123-456-7890"),
    2: User(id=2, name="Bob")
}

        # self.users = {
        #     # 1: User(id=1, name="Alice", email="alice@example.com"),
        #     # 2: User(id=2, name="Bob")
            
        # }

    def getUserById(self, id):
        return self.users.get(id, User(id=id, name="Unknown"))

handler = UserProfileHandler()
processor = UserProfileService.Processor(handler)

transport = TSocket.TServerSocket(host='127.0.0.1', port=9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
print("Starting server on port 9090...")
server.serve()

from gen_py.user_profile import UserProfileService

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

# Set up client transport
transport = TSocket.TSocket('127.0.0.1', 9090)
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = UserProfileService.Client(protocol)

transport.open()

user = client.getUserById(1)
print(f"User 1: {user.name}, Email: {user.email}")
print("Phone:", user.phone_number)


user = client.getUserById(99)
print(f"User 99: {user.name}, Email: {user.email}")

transport.close()

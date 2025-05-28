from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.Thrift import TException

from gen_py.user_profile import UserProfileService

def main():
    try:
        # Connect to Java server
        transport = TSocket.TSocket('localhost', 9090)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)

        client = UserProfileService.Client(protocol)
        transport.open()

        user = client.getUserById(1)
        print(f"User ID: {user.id}, Name: {user.name}, Email: {user.email}")

        transport.close()

    except TException as e:
        print(f"Thrift exception: {e}")

if __name__ == '__main__':
    main()
how
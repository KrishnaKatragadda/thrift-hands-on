package user.profile;

import org.apache.thrift.protocol.TBinaryProtocol;
import org.apache.thrift.protocol.TProtocolFactory;
import org.apache.thrift.server.TSimpleServer;
import org.apache.thrift.server.TServer;
import org.apache.thrift.transport.TServerSocket;
import org.apache.thrift.transport.TServerTransport;

public class JavaServer {
    public static void main(String[] args) {
        try {
            UserProfileServiceHandler handler = new UserProfileServiceHandler();
            UserProfileService.Processor processor = new UserProfileService.Processor(handler);

            TServerTransport serverTransport = new TServerSocket(9090);
            TProtocolFactory protocolFactory = new TBinaryProtocol.Factory();

            TServer server = new TSimpleServer(
                new TServer.Args(serverTransport).processor(processor).protocolFactory(protocolFactory)
            );

            System.out.println("Starting the Java Thrift server...");
            server.serve();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

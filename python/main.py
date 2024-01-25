import socket

class TCPServer:
    server_address = ('localhost', 8888)
    def start(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(self.server_address)
        sock.listen(1)
        print(f"server running on {self.server_address[0] } port {self.server_address[1]}")

        while True:
            # Wait for a connection
            print('waiting for a connection')
            connection, client_address = sock.accept()
            try:
                print('connection from', client_address)

                # Receive the data in small chunks and retransmit it
                # while True:
                data = connection.recv(1024)
                print('received {!r}'.format(data))
                if data:
                    print(f"received data length {len(data)}")
                    connection.sendall(data)
                else:
                    print('no data from', client_address)
                    break

            finally:
                # Clean up the connection
                print('close connection')
                connection.close()




if __name__ == '__main__':
    server = TCPServer()
    server.start()

import socket


class EchoClient:
    # Connect the socket to the port where the server is listening
    server_address = ("localhost", 8888)

    def send(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print(f"[CLIENT] Connect to server")

        sock.connect(self.server_address)

        try:
            # Send data
            message = b"This is the message.  It will be repeated."
            print("sending {!r}".format(message))
            sock.sendall(message)

            # Look for the response
            amount_received = 0
            amount_expected = len(message)

            while amount_received < amount_expected:
                data = sock.recv(16)
                amount_received += len(data)
                print("[CLIENT] received {!r}".format(data))

        finally:
            print("[CLIENT] closing socket")
            sock.close()


if __name__ == "__main__":
    client = EchoClient()
    client.send()

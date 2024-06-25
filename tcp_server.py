import socket
import threading

IP = "0.0.0.0"
PORT = 9998


def handle_client(client_socket):
    with client_socket as sock:
        while True:
            request = sock.recv(1024)
            if not request:
                break
            message = request.decode("utf-8").strip()
            print(f"[*] Received: {message}")
            if message.lower() == "hello":
                response = "Hi there!"
            elif message.lower() == "bye":
                response = "Goodbye!"
                sock.send(response.encode())
                break
            else:
                response = "Unknown command."
            sock.send(response.encode())


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f"[*] Listening on {IP}:{PORT}")

    while True:
        client, address = server.accept()
        print(f"[*] Accepted connection from {address[0]}:{address[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()


if __name__ == "__main__":
    main()

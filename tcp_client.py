import socket


def main():
    target_host = "127.0.0.1"
    target_port = 9998

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_host, target_port))

    while True:
        message = input("Enter message: ")
        client.send(message.encode())
        response = client.recv(4096)
        print(f"Server response: {response.decode()}")
        if message.lower() == "bye":
            break

    client.close()


if __name__ == "__main__":
    main()

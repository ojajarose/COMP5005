import ssl
import socket
import json

# Configuration Variables
HOST = 'localhost'
PORT = 443  # Use a secure port for SSL/TLS
CERT_FILE = r'C:\Users\opeye\PycharmProjects\BLAIZE\venv\cert.pem'
KEY_FILE = r'C:\Users\opeye\PycharmProjects\BLAIZE\venv\key.pem'

def server():
    # Specify the fixed SSL/TLS version (TLS 1.2 in this case)
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)
    context.verify_mode = ssl.CERT_NONE  # Disable certificate verification

    with socket.socket() as bindsocket:
        bindsocket.bind((HOST, PORT))
        bindsocket.listen(5)

        while True:
            newsocket, fromaddr = bindsocket.accept()
            with context.wrap_socket(newsocket, server_side=True) as connstream:
                try:
                    data = connstream.recv(1024)
                    print(f"Received health data: {data.decode('utf-8')}")
                    # Process the health data here
                except Exception as e:
                    print(f"Error: {e}")
                finally:
                    connstream.shutdown(socket.SHUT_RDWR)

if __name__ == "__main__":
    server()

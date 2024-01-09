import ssl
import socket
import json

# Configuration Variables
HOST = 'localhost'
PORT = 443  # Use a secure port for SSL/TLS
CLIENT_CERT_FILE = r'C:\Users\opeye\PycharmProjects\BLAIZE\venv\cert.pem'
CLIENT_KEY_FILE = r'C:\Users\opeye\PycharmProjects\BLAIZE\venv\key.pem'

def client():
    # Specify the fixed SSL/TLS version (TLS 1.2 in this case)
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain(certfile=CLIENT_CERT_FILE, keyfile=CLIENT_KEY_FILE)
    context.check_hostname = False  # Disable hostname verification
    context.verify_mode = ssl.CERT_NONE  # Disable certificate verification

    with socket.create_connection((HOST, PORT)) as sock:
        with context.wrap_socket(sock, server_hostname=HOST) as ssl_sock:
            health_data = {
                "temperature": 36.7,
                "heartbeat": 78,
                "blood_pressure": "120/80"
            }
            ssl_sock.sendall(json.dumps(health_data).encode('utf-8'))

if __name__ == "__main__":
    client()

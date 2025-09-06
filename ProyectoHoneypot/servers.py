import socket
import threading
from ProyectoHoneypot.logger import setup_logger

logger=setup_logger()


def fake_http_server(host="0.0.0.0", port=8080):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    logger.info(f"fake http server listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        logger.info(f"connection attempt from {addr}")

        response = b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<h1> Welcome</h1>"
        client_socket.send(response)
        client_socket.close()

def fake_ssh_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    logger.info(f"[SSh] Listening on host {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        logger.info(f"[SSH] Connection from {addr}")
        banner = b"SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.5\r\n"
        client_socket.send(banner)
        client_socket.close()

def fake_fpt_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    logger.info(f"[FTP] Listening on host {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        logger.info(f"[FTP] Connection from {addr}")
        banner = b"220 (vsFTPd 3.0.3)\r\n"
        client_socket.send(banner)
        client_socket.close()
    
def fake_sql_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    logger.info(f"[Sql] Listening on host {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        logger.info(f"[FTP] Connection from {addr}")
        banner = b"Welcome to MySql\r\n"
        client_socket.send(banner)
        client_socket.close()
import socket
import subprocess

HOST = '127.0.0.1'
PORT = 22345

def run_command(command):
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    except:
        output = b"Command execution failed"
    return output

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Listening on {HOST}:{PORT}...")
    
    conn, addr = server_socket.accept()
    print(f"Connection from {addr[0]}:{addr[1]}")
    
    while True:
        command = conn.recv(1024).decode().strip()
        if command == "exit":
            conn.close()
            break
        output = run_command(command)
        conn.sendall(output)
        conn.sendall(b"\n")

start_server()

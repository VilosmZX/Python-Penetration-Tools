import socket 
import os 

sock = socket.socket()
HOST = input('Enter IP: ').strip()
PORT = 8080
ENCODE = 'utf-8'
sock.connect((HOST, PORT))
print('Berhasil Connect ke dalam server!')

while True:
  command = sock.recv(1024).decode(ENCODE)
  if command == 'view_cwd':
    print(f'Command masuk: {command}')
    files = os.getcwd()
    sock.send(files.encode(ENCODE))
  elif command == 'ls':
    print(f'Command masuk: {command}')
    results = ''
    files = os.listdir(os.getcwd())
    for file in files:
      results += f'{file}\n'
    sock.send(results.encode(ENCODE))
  elif command.startswith('cd'):
    path = command.split(' ')[1]
    try:
      os.chdir(path)
      sock.send('Direktori Terganti!'.encode(ENCODE))
    except:
      sock.send('Path tidak ada'.encode(ENCODE))
  elif command.startswith('rm'):
    path = command.split(' ')[1]
    if(os.path.isfile(path)):
      os.remove(path)
      sock.send('File berhasil di apus!'.encode(ENCODE))
    elif(os.path.isdir(path)):
      os.rmdir(path)
      sock.send('Folder berhasil di hapus!'.encode(ENCODE))
  elif command.startswith('file'):
    file = command.split(' ')[1].strip()
    text = command.split(' ')[2:]
    result = ''
    for t in text:
      result += t.strip() + ' '
    with open(file, 'w') as f:
      f.write(result)
    sock.send(f'File berhasil dibuat dengan isi {result}'.encode(ENCODE))
  else:
    print(f'Unknown command {command}')
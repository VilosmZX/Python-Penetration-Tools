import socket as __socket
from typing import Union as __Union
from IPy import IP  as __IP
import time as __time

__port_list = [21, 22, 23, 25, 80, 106, 110, 143, 443]

def __validate_ip(ip):
  try:
    __IP(ip)
    return ip 
  except ValueError:
    try:
      return __socket.gethostbyname(ip)
    except:
      return None 

def __get_banner(s):
  return s.recv(1024)

def __scan_all(args: list):
  print('')
  start_time = __time.time()
  for ip in args:
    valid_ip = __validate_ip(ip.strip())
    if(valid_ip is None):
      print('IP Tidak Valid!')
    else:
      print(f'Target: {ip.strip()} [{valid_ip}]')
      for port in __port_list:
        try:
          sock = __socket.socket()
          sock.settimeout(0.1)
          sock.connect((valid_ip, port))
          try:
            banner = __get_banner(sock).decode().strip('\n')
            print(f'[✅] Port {port} terbuka : {banner}')
          except:
            print(f'[✅] Port {port} terbuka')
        except:
          pass
    print('')
  end_time = __time.time()
  delta_time = end_time - start_time
  print('Selesai dalam {:.2f} detik.'.format(delta_time))

def __scan(ip: str):
  print('\n')
  start_time = __time.time()
  valid_ip = __validate_ip(ip.strip())
  if(valid_ip is None):
    print('IP Tidak Valid!')
  else:
    print(f'Target: {ip.strip()} [{valid_ip}]')
    for port in __port_list:
      try:
        sock = __socket.socket()
        sock.settimeout(0.5)
        sock.connect((valid_ip, port))
        try:
          banner = __get_banner(sock).decode().strip('\n')
          print(f'[✅] Port {port} terbuka : {banner}')
        except:
          print(f'[✅] Port {port} terbuka')
        
      except:
        pass
  print('')
  end_time = __time.time()
  delta_time = end_time - start_time
  print('Selesai dalam {:.2f} detik.'.format(delta_time))

def port_scan():
  print('Pakai koma untuk scan lebih dari 1, contoh:\ngoogle.com, bing.com, 192.168.0.1')
  ip = input('[+] Target: ')
  if ',' in ip:
    ip = ip.split(',')
    __scan_all(ip)
  else:
    __scan(ip)




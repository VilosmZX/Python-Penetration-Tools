import subprocess
import sys 

try:
  import IPy
  from tools import port_scan
  if __name__ == '__main__':
    port_scan()
except ModuleNotFoundError:
  print('Required Module: IPy')
  install = input('Install ([Y]es | [N]o): ').lower()
  if install == 'y':
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
  else:
    print('Cancelled.')



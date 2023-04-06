import socket

target = input("target: ") #ip for a target
port = input("port range ex(5-200): ") #port range to scan

starting = int(port.split('-')[0])
ending = int(port.split('-')[1])

print(" Scanning Host ", target , " From Port ", starting , " To Port ", ending)


for port in range(starting, ending): #loop from the first port to the ending port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((target, port))
    if (status == 0):
        print("port ", port, "Open")
    else:
        print("Port ", port, "Closed")
    s.close()

from socket import *
import random 
import time 

# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket
serverSocket.bind(('', 12000))

print("Server online.")

packet_drop_chance = 0.1

while True:
    try:
        # Receive the client packet along with the address it is coming from
        message, address = serverSocket.recvfrom(1024)
        print (f"Received message: {message} from {address}")

        if random.random() < packet_drop_chance:
            print('This packet has been dropped.')
            continue 
        
        timestamp = time.strftime("%a %b %d %H %M %S %Y")

        delay = random.randint(10, 20) / 1000 #Convert ms to seconds here 
        print(f"Delay of {delay * 1000:.2f} ms")

        time.sleep(delay) #delay here

        # The server responds
        serverSocket.sendto(message + timestamp.encode(), address)
        print(f'Response to {address} with delay')

    except Exception as e:
        print (f'Error: {e}')
        break 
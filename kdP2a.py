import time 
import socket 
import sys 

#Define server variables 
server_name = 'localhost'
server_port = 12000
server_timeout = 60 #timeout in seconds 
#number_of_pings_to_send = 10
number_of_pings_to_send = 50

#Creating UDP Socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_socket.settimeout(server_timeout)

rtt_list = []
sent_packets_count = 0
received_packet_count = 0

for number_of_pings in range(1, number_of_pings_to_send + 1):
    message = f'Kyle {number_of_pings}'.encode()
    sent_packets_count += 1
    start_time = time.time()

    try:

        client_socket.sendto(message, (server_name, server_port))

        response, serverAddress = client_socket.recvfrom(1024)
        end_time = time.time()

        #Calculate RTT
        rtt = (end_time - start_time) * 1000 #milliseconds
        rtt_list.append(rtt)
        received_packet_count += 1

        #Response 
        response_message = response.decode()
        print(f"Kyle {number_of_pings}: server reply: {response_message}, RTT = {rtt:.2f} ms")

    except socket.timeout:
        print (f"Kyle {number_of_pings}: Request timed out")

#Calculations 

if received_packet_count > 0:
    min_rtt = min(rtt_list)
    max_rtt = max(rtt_list)
    average_rtt = sum(rtt_list) / len(rtt_list)
    packet_loss = ((sent_packets_count - received_packet_count) / sent_packets_count) * 100

    print("\n--- Ping statistics ---")
    print(f"Minimum RTT: {min_rtt:.2f} ms")
    print(f"Maximum RTT: {max_rtt:.2f} ms")
    print(f"Average RTT: {average_rtt:.2f} ms")
    print(f"Packet loss: {packet_loss:.2f}%")
else:
    print("No packets received, no statistics available.")

#close UDP socket
client_socket.close()
"""Raw socket TCP client example (local test)"""
import socket
def echo_client(msg, host='127.0.0.1', port=9999):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host,port))
        s.sendall(msg.encode())
        data = s.recv(1024)
        print('received', data.decode())

if __name__ == '__main__':
    print('Socket client example - requires server listening at port 9999 to work')

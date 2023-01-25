import socket

def main():
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(("192.168.85.132", 8888))
    quote = c.recv(1024)
    print(f"Quotes of the day: {quote}")
    c.close()

main()

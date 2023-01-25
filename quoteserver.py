import socket
import threading
import random

quotes = ["Quote 1", "Quote 2", "Quote 3", "Quote 4", "Quote 5"]

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 8888))
    s.listen(5)
    print("Server started at 192.168.85.132:8888")

    while True:
        c, address = s.accept()
        print(f"Connection from {address} has been established.")
        quote = random.choice(quotes)
        c.send(quote.encode())
        c.close()

main()

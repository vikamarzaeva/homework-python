import socket

def get_ip():
    dns, ip = input('').split()
    ip_address = socket.gethostbyname(dns)
    if ip_address == ip:
        print(f"http://{dns} - {ip_address}")
    else:
        print(f"[ERROR] http://{dns} IP mismatch: {ip} {ip_address}")

if __name__ == '__main__':
    get_ip()

import socket

def get_ip(dns):
    ip_addr = []
    for i in dns:
        ip_addr.append(socket.gethostbyname(i))
    return ip_addr

def check_ip_addr(dns, ip):
    current_ip_addr = []
    for i in dns:
        current_ip_addr.append(socket.gethostbyname(i))
    for k in range(len(ip)):
        if current_ip_addr[k] == ip[k]:
            print(f"http://{dns[k]} - {ip[k]}")
        else:
            print(f"[ERROR] http://{dns[k]} IP mismatch: {ip[k]} {current_ip_addr[k]}")

if __name__ == '__main__':
    dns = ['drive.google.com', 'google.com', 'mail.google.com']
    ip = get_ip(dns)
    check_ip_addr(dns, ip)
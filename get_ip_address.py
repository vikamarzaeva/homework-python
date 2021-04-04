import socket

def get_ip():
    dns={
          "drive.google.com" : "142.250.186.78",
          "google.com" : "64.233.162.113",
          "mail.google.com" : "172.217.18.101"
        }

    for key in dns:
        ip_address = socket.gethostbyname(key)
        if ip_address == dns.get(key):
            print(f"http://{key} - {ip_address}")
        else:
            print(f"[ERROR] http://{key} IP mismatch: {dns.get(key)} {ip_address}")
if __name__ == '__main__':
    get_ip()

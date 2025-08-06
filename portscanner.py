import socket
import argparse
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

found_ports_lock = Lock()
found_ports = []

def scan_port(host, port, service_name):
    """Scans a single port on a given host."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        try:
            sock.connect((host, port))
            print(f"[{service_name.upper()}] Port {port} is open.")
            with found_ports_lock:
                found_ports.append(port)
        except (socket.timeout, ConnectionRefusedError):
            pass

def main():
    """Main function to parse arguments and run the port scan."""
    parser = argparse.ArgumentParser(
        prog='PortScanner',
        description='Scans for open ports on a specified target.',
        epilog='Example: python PortScanner.py 127.0.0.1'
    )
    parser.add_argument('target', type=str, help="Target IP address for port scanning.")
    args = parser.parse_args()

    host = args.target

    common_ports = {
        21: 'ftp',
        22: 'ssh',
        23: 'telnet',
        80: 'http',
        443: 'https',
        445: 'smb',
        8080: 'http-alt',
        3306: 'mysql',
        5432: 'postgresql',
        554: 'rtsp'
    }
    
    print(f"Scanning target: {host}...\n")
    
    with ThreadPoolExecutor(max_workers=50) as executor:
        for port, service in common_ports.items():
            executor.submit(scan_port, host, port, service)
    
    if not found_ports:
        print("No open ports found.")

if __name__ == '__main__':
    main()
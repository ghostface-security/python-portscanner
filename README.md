# Python Network Port Scanner

This Python script is a command-line tool designed for network reconnaissance, specifically to identify open ports on a specified target. It utilizes multi-threading to efficiently scan a list of common service ports, demonstrating fundamental networking concepts and the importance of network security.
⚠️ Disclaimer - IMPORTANT: Ethical Use Only ⚠️

This tool (python-portscanner) is provided strictly for educational, research, and ethical hacking purposes. Its use is limited to testing systems for which you have explicit, prior, and written authorization from the owner.

The creator of this tool is not responsible for any misuse, illegal activities, or damage caused by its deployment or operation. By using this tool, you acknowledge and agree to assume full responsibility for your actions and to comply with all applicable laws and regulations.
Project Purpose & Learning Objectives

This project was developed to:

    Demonstrate Network Scanning: Illustrate how to programmatically identify open ports on a network host using Python's socket module.

    Showcase Concurrency: Utilize ThreadPoolExecutor to perform scans concurrently, improving efficiency for multiple ports.

    Highlight Network Security Fundamentals: Emphasize the importance of firewalls, proper port management, and securing network services.

    Understand Service Fingerprinting (Basic): Associate common open ports with their default services (e.g., 22 for SSH, 80 for HTTP).

How It Works

The portscanner.py script operates by:

    Parsing Arguments: It accepts a single command-line argument: the target IP address or hostname to scan.

    Defining Common Ports: It has a predefined dictionary of common ports and their associated service names (e.g., FTP, SSH, HTTP, HTTPS, MySQL).

    Concurrent Scanning: It uses ThreadPoolExecutor to create a pool of worker threads. Each thread attempts to establish a TCP connection to a specific port on the target host with a short timeout.

    Identifying Open Ports: If a connection is successfully established (meaning the port is open and listening), it prints a message indicating the open port and its service.

    Collecting Results: All found open ports are collected and can be reviewed after the scan completes.

Code Snippet (Core Logic):

def scan_port(host, port, service_name):
    """Scans a single port on a given host."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1) # Set a short timeout for efficiency
        try:
            sock.connect((host, port))
            print(f"[{service_name.upper()}] Port {port} is open.")
            with found_ports_lock: # Thread-safe addition to results
                found_ports.append(port)
        except (socket.timeout, ConnectionRefusedError):
            # Port is closed or filtered, simply pass
            pass

# ... (in main function) ...
with ThreadPoolExecutor(max_workers=50) as executor:
    for port, service in common_ports.items():
        executor.submit(scan_port, host, port, service)

Installation

To use this script, simply clone the repository:

git clone https://github.com/ghostface-security/python-portscanner.git && cd python-portscanner

No external Python libraries are required beyond what's typically included with a standard Python 3 installation (socket, argparse, concurrent.futures, threading).
Usage

    Run the script from your terminal:

    python3 portscanner.py <target_ip_address_or_hostname>

    Example (scanning your local machine):

    python3 portscanner.py 127.0.0.1

    Example (scanning a specific hostname):

    python3 portscanner.py scanme.nmap.org # A legitimate target for scanning practice

Ethical Use Cases

    Personal Network Auditing: Scan your own home network or devices to identify accidentally open ports or misconfigurations.

    Educational Demonstrations: Use in a controlled lab environment to teach about TCP/IP, ports, services, and basic network reconnaissance.

    Security Research: Analyze the open ports of publicly available, authorized test systems.

    Troubleshooting: Verify if a service is running and accessible on a specific port.

Defensive Countermeasures

This tool highlights the importance of robust network security. To protect against unauthorized port scanning and exploitation of open services:

    Firewalls: Implement and properly configure firewalls (e.g., ufw on Linux, Windows Firewall) to block unwanted incoming connections. Only open ports that are absolutely necessary for your services.

    Least Privilege for Services: Ensure network services run with the minimum necessary user privileges.

    Regular Patching: Keep all operating systems and network services updated to patch known vulnerabilities.

    Disable Unused Services: Turn off any services that are not actively being used to reduce the attack surface.

    Intrusion Detection/Prevention Systems (IDS/IPS): Deploy systems that can detect and/or block suspicious scanning activity.

    Network Segmentation: Divide your network into isolated segments to limit the lateral movement of attackers if one segment is compromised.

License

This project is licensed under the MIT License - see the LICENSE file for details.


import socket
from datetime import datetime


def check_dns(hostname):
    """Resolve a hostname to an IP address."""
    print(f"\n[DNS CHECK] {hostname}")

    try:
        ip_address = socket.gethostbyname(hostname)
        print(f"SUCCESS: Resolved to {ip_address}")
        return True
    except socket.gaierror:
        print("FAILED: Could not resolve hostname.")
        return False


def check_https(hostname):
    """Test TCP connectivity to HTTPS port 443."""
    print(f"\n[HTTPS CHECK] {hostname}:443")

    try:
        with socket.create_connection(
            (hostname, 443), timeout=5
        ):
            print("SUCCESS: TCP connection established.")
            return True
    except (OSError, TimeoutError) as error:
        print(f"FAILED: {error}")
        return False


def main():
    print("=" * 45)
    print("     NETWORK TROUBLESHOOTING TOOLKIT")
    print("=" * 45)
    print("Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    hostname = input(
        "\nEnter a hostname (example: example.com): "
    ).strip()

    if not hostname or any(c.isspace() for c in hostname):
        print("Please enter a valid hostname.")
        return

    dns_ok = check_dns(hostname)
    https_ok = check_https(hostname) if dns_ok else False

    print("\n" + "=" * 45)
    print("SUMMARY")
    print("DNS resolution:", "PASS" if dns_ok else "FAIL")
    print("HTTPS TCP connectivity:", "PASS" if https_ok else "FAIL")
    print("=" * 45)


if __name__ == "__main__":
    main()

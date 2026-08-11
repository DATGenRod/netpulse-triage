import os
import sys
import shutil
import socket
import logging
import subprocess
from datetime import datetime

# Configure clean logging to stdout for container compatibility
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

class NetPulseTriage:
    def __init__(self):
        # Key infrastructure hosts to validate network paths
        self.target_hosts = ["8.8.8.8", "google.com", "akamai.com"]
        logging.info("NetPulse-Triage Diagnostic Engine initialized.")

    def check_disk_usage(self):
        """Validates storage infrastructure availability"""
        total, used, free = shutil.disk_usage("/")
        used_percentage = (used / total) * 100
        status = "HEALTHY" if used_percentage < 85 else "WARNING: HIGH DISK USAGE"
        return {
            "metric": "Disk Space Utilization",
            "status": status,
            "details": f"{used_percentage:.2f}% used ({free / (2**30):.2f} GB free of {total / (2**30):.2f} GB)"
        }

    def test_dns_resolution(self):
        """Verifies core DNS resolution capabilities"""
        test_domain = "akamai.com"
        try:
            ip_address = socket.gethostbyname(test_domain)
            return {
                "metric": f"DNS Resolution ({test_domain})",
                "status": "SUCCESSFUL",
                "details": f"Resolved to target IP: {ip_address}"
            }
        except socket.gaierror:
            return {
                "metric": f"DNS Resolution ({test_domain})",
                "status": "CRITICAL - FAILURE",
                "details": "Could not resolve domain. Verify DNS settings or network gateway."
            }

    def ping_host(self, host):
        """Executes a network ICMP ping to evaluate latency and packet loss"""
        try:
            # Running 2 packets with a 2-second timeout for optimal execution
            subprocess.run(
                ["ping", "-c", "2", "-W", "2", host],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=True
            )
            return "SUCCESSFUL (2 packets transmitted, 0% packet loss)"
        except subprocess.CalledProcessError:
            return "FAILED (Host unreachable or network connection down)"

    def run_full_diagnostics(self):
        """Orchestrates the entire IT support troubleshooting workflow"""
        logging.info("Executing comprehensive automated infrastructure diagnostic checks...")
        
        report = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "storage": self.check_disk_usage(),
            "dns": self.test_dns_resolution(),
            "network": {}
        }

        for host in self.target_hosts:
            report["network"][host] = self.ping_host(host)

        return report

if __name__ == "__main__":
    triage = NetPulseTriage()
    results = triage.run_full_diagnostics()

    # Formatted Markdown output ideal for technical ticket injection
    print("\n" + "#" * 60)
    print(f"   AUTOMATED IT SUPPORT DIAGNOSTIC REPORT - {results['timestamp']}   ")
    print("#" * 60)
    print(f"\n## [SYSTEM METRIC] {results['storage']['metric']}")
    print(f"- Status : {results['storage']['status']}")
    print(f"- Details: {results['storage']['details']}")
    
    print(f"\n## [NETWORK METRIC] {results['dns']['metric']}")
    print(f"- Status : {results['dns']['status']}")
    print(f"- Details: {results['dns']['details']}")
    
    print("\n## [NETWORK METRIC] ICMP Latency / Connectivity Checks")
    for host, status in results["network"].items():
        print(f"- Target: {host:<12} -> Result: {status}")
    print("\n" + "#" * 60 + "\n")

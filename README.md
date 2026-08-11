# NetPulse-Triage - Automated Infrastructure & Network Diagnostic CLI

A command-line interface (CLI) diagnostic tool built in Python and containerized with Docker. Designed for Technical Support workflows and Systems Administration, this utility automates basic troubleshooting steps—validating local disk capacity, testing domain DNS resolution, and executing ICMP network availability checks—before generating a clean Markdown report ready for engineering ticketing systems.

## Professional Context & Value Proposition
Drawing from my background in **Seller Partner Support and GO AI Operations**, I know that minimizing time-to-resolution (TTR) is critical when technical infrastructure issues arise. Instead of running manual, repetitive commands during an incident, **NetPulse-Triage** automates the baseline system checks. This project bridges customer support insight with technical automation, delivering a standardized diagnostic output that prevents human error during escalation.

## Tech Stack & Key Features
- **Language:** Python 3.11 (Native Subprocesses, Socket Programming, System Auditing).
- **Containerization:** Docker (Slim Debian footprint customized with system-level network utilities).
- **Network Validation:** Live ICMP verification targeting key public endpoints (e.g., Akamai and public DNS systems).
- **Ticket Readiness:** Outputs a structured Markdown summary optimized for direct injection into ITSM platforms like Jira or ServiceNow.

## Repository Structure
```text
netpulse-triage/
├── Dockerfile                  # Base image configuration with native network utilities
└── app/
    └── main.py                 # Diagnostic Orchestrator Engine
```

## Setup and Deployment (How to Replicate)
Since the tool interacts with networking layers, containerization ensures it executes uniformly across any Ubuntu/Linux environment without host contamination.

### 1. Build the Docker Image
Compile the custom container environment from the project root:
```bash
docker build -t netpulse-triage .
```

### 2. Run the Diagnostic CLI
Launch the automated utility. Docker will bridge the host network interface to execute the outbound ping requests securely:
```bash
docker run --rm netpulse-triage
```

## Expected Output Verification
Once triggered, the internal engine runs the diagnostics sequentially and displays a ticket-ready report:

```text
############################################################
   AUTOMATED IT SUPPORT DIAGNOSTIC REPORT   
############################################################

## [SYSTEM METRIC] Disk Space Utilization
- Status : HEALTHY
- Details: 12.34% used (35.50 GB free of 40.00 GB)

## [NETWORK METRIC] DNS Resolution (akamai.com)
- Status : SUCCESSFUL
- Details: Resolved to target IP: 23.212.44.15

## [NETWORK METRIC] ICMP Latency / Connectivity Checks
- Target: 8.8.8.8      -> Result: SUCCESSFUL (2 packets transmitted, 0% packet loss)
- Target: google.com   -> Result: SUCCESSFUL (2 packets transmitted, 0% packet loss)
- Target: akamai.com   -> Result: SUCCESSFUL (2 packets transmitted, 0% packet loss)

############################################################
```

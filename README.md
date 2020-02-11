# IOVisor-eDPFM
IOVisor-eBPF Dynamic Packet Filtering and Monitoring for K-ONE project

Instructions

1. Clone the directory

2. Do not run any scripts from the installation folder, the script files are just for testing purposes

- for eBPF based packet monitoring
python IOVisor-eDPFM/eBPF/packet_monitor.py

DONE SO FAR
* Packet source/destination IP parse
* Parsed information transmitted to and saved from the database saver

BIBIM-BAP
* Packet's source IP address and destination IP address will be printed.
* Packet monitor fails to parse some packets from 152 packets when [ping -f]ed -> Due to the eBPF Map ring buffer

WORKING ON
* Packet monitor performance upgrade

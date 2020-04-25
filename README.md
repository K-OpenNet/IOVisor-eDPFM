# IOVisor-eDPFM
IOVisor-eBPF Dynamic Packet Filtering and Monitoring for K-ONE project

Instructions

1. Install bcc (refer to https://github.com/iovisor/bcc/blob/master/INSTALL.md)

2. Clone the directory

3. Do not run any scripts from the installation folder, the script files are just for testing purposes

- eBPF based packet monitoring program has same functionalities with /bcc/example/networking/net_monitor.py. If you intend to just monitor your network interface, I advise you to check it out.

4. Run kafka zookeeper(either from the data rx / data tx) and a broker server

$ kafka/kafka_2.12-2.4.0/bin/zookeeper-server-start.sh config/zookeeper.properties

$ kafka/kafka_2.12-2.4.0/bin/kafka-server-start.sh config/server.properties

5. 

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

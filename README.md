# IOVisor-eDPFM
IOVisor-eBPF Dynamic Packet Filtering and Monitoring for K-ONE project

Instructions

1. Install bcc (refer to https://github.com/iovisor/bcc/blob/master/INSTALL.md)

2. Clone the directory

3. Do not run any scripts from the installation folder, the script files are just for testing purposes

- eBPF based packet monitoring program has same functionalities with /bcc/example/networking/net_monitor.py. If you intend to just monitor your network interface, I advise you to check it out.

4. Run kafka zookeeper(either from the data rx / data tx) and a broker server

$ sudo kafka/kafka_2.12-2.4.0/bin/zookeeper-server-start.sh config/zookeeper.properties

$ sudo kafka/kafka_2.12-2.4.0/bin/kafka-server-start.sh config/server.properties

5'. Change the network interface names and kafka server/zookeeper IP addresses in the source code. 

* later the source code will be edited so you can give ip interface names as inputs

$ sudo vim eBPF/kafka_stat_n_packet_monitor.py

5. Run eBPF based packet monitor

$ sudo python eBPF/kafka_stat_n_packet_monitor.py

* 


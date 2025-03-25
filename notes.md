# Notes:

## Python Sockets Simply Explained

- Client and Server Arhictecture
- Socket Theory
    - socket: communication endpoint
    - bluetooch, internet, OS, infrared
    - `socket.AF_NET`: internet
    - TCP: `sock_stream`
        - connection-based
        - detects packet loss
        - sequential
        - byte stream
        - keeps up the connection  
    - UDP: `sock_dgram` 
        - individual messages
        - more real-time (faster)

## TCP/IP for Programmers

[ ] get MAC addresses

- Logical Devices: Firewall, Router, Modem, Access Point
- Modem -> Router -> Switch 
- Switch connected to WAP for WiFi access
- And can Firewalls in between MRS

- Cacheing: storing data locally so that they can respond to clients more quickly
- Protocol: Network Protocols, Storage Protocols, Communication Protocols
- TCP/IP (Network)
    - v4
    - v6

####  Ethernet Standard
- MAC addresses: hard coded addresses, difference between devices
- Collision Domains: both computers listen at the same time and then talk at the same time.
    - can cause a Broadcast storm

####  MAC addresses (Data Link Layer; Layer 2)
- Universally Unique Identifier
- Part is the Vendor ID, Part is the Serial Number
- for ports?

#### Layer 2 networking (ethernet layer networking)
- Hubs
- Bridges: connecting hubs
    - determine if the MAC address being looked for is on the other hub, if not it blocks the connection
- Switch: what if every port was a switch?
    - blasts all the ports for MAC address and finds out MAC address at a certain port
    - backplane: communication for all these ports together

#### Layer 3 Networking
- connecting multiple networks together
- LAN, WAN, CAN, MAN, internet
- Switch -> Router -> WAN
- can manually address routable addresses (TCP/IP)
- LAN -> WAN -> Internet

#### TCP/IP v4 - Routable Suite
- multiple protocols
- TCP: how devices talk to each other
- IP: Addressing Protocol
- ICMP (Internet Communication Message Protocol)
- Subnet Mask

#### Private IP Address Blocks

#### Switches
- Layer 2 Networking (IP addresses at Layer 3)
- Contains MAC Address Tables
- for Switches and IP to work together we use ARP (Address Resolution Protocol)
    - ARP: resolves MAC address to IP address
    - Cacheing issues when you change IP and MAC address doesn't change

#### TCP Ports
- Firewall blocks ports
- generally preconfigured but can be manually set

#### Routers and Default Gateways
- Default Gateway: your computer talking to another computer
    - Router/Modem, it connects networks

#### NAT and Port Forwarding
- NAT killed IPv6
- numerous connected devices can share the same external IP address

#### Internet Facing Static IP Addresses
- directly connected to the internet
- no need for port forwarding

#### Firewalls
- block TCP ports
- database cluster
    - databases communicating with each other
    - put them on their own network, and put a firewall and router in between their network and a web network

#### Domain Name Service
- Resolves fully qualified domain names to IP addresses
- hosts file
- reverse DNS: checks if the IP address is connected to the right domain name

#### DHCP - Dynamic Host Configuration Protocol
- people coming in and out: dynamically assign IP addresses
- scope: pool of IP addresses that DHCP can assign from
- problems with expirations
- write code for DNS names not IP addresses

#### VPN
- tunnel that allows remote computers to remotely interact to a LAN
- if it senses that the tunnel has been comprised it closes the tunnel and makes a new one

#### Command Line Tools
- ping -c 1
- arp -a
- traceroute
- ipconfig


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

[ ] - get MAC addresses

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

#### Layer 2 networking
- Hubs
- Bridges: connecting hubs
    - determine if the MAC address being looked for is on the other hub, if not it blocks the connection
- Switch: what if every port was a switch?
    - blasts all the ports for MAC address and finds out MAC address at a certain port

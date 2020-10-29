# Internet Protocol (计算机网络)

> https://www.guru99.com/router-vs-switch-difference.html#:~:text=Router%20operations%20revolve%20around%20IP,restricted%20to%20wired%20network%20connections.

## How Router Works?

A router connects multiple networks and tracks network traffic between them. It has one connection to the internet and one connection to your private local network.

Moreover, many routers contain built-in switches that allow you to connect multiple wired devices. Many routers also contain wireless radios that allows you to connect Wi-Fi devices.

## How Switch work?

A network switch is also called bridging hub, switching, or MAC bridge. Switches devices use MAC addresses to forward data to the right destination. Operating system at the data link layer uses packet switching to receive, process, and forward data.

A switch offers support to handle the data and knows the particular addresses to send the message. It can decide which computer is the message intended for and send the message directly to the right computer. The efficiency of the switch can be improved by providing a faster network speed.

## Difference between Router and Switch

Here are some important differences between the Router and Switch:

[![img](https://www.guru99.com/images/1/020820_1135_RoutervsSwi3.png)](https://www.guru99.com/images/1/020820_1135_RoutervsSwi3.png)

| **Router**                                                   | **Switch**                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Routers operate at Layer 3 (Network) of the OSI model.       | Network switches operate at layer two (Data Link Layer) of the OSI model. |
| Router will offer NAT, NetFlow and QoS Services              | Switch will not offer such services.                         |
| Store IP address in the routing table and maintain an address on its own. | Store MAC address in a lookup table and maintain an address on its own. However, Switch can learn the MAC address. |
| Networking device 2/4/8 ports.                               | A switch is a multi-port bridge. 24/48 ports.                |
| Less Duplex                                                  | In Full Duplex, So, no Collision occurs.                     |
| The speed limit is 1-10 Mbps for wireless and 100 Mbps for wired connection. | The speed limit for the switch is 10/100Mbps.                |
| Helps users to take the faster routing decision              | Likely to take a more complicated routing decision           |
| The router can perform NAT                                   | Switches can't perform NAT                                   |
| In various types of network environments (MAN/ WAN), the router works faster compares to Switch. | In a LAN environment, a switch is faster than Router.        |
| In Router, every port has its own broadcast domain.          | The switch has one broadcast domain except VLAN implemented. |
| Router operations revolve around IP Addresses.               | Switches work with MAC addresses as it operates within the confines of a single network. |
| Routers can work within both wired and wireless network situations. | Switches are restricted to wired network connections.        |
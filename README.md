# Botnet Attack Project

## Goal

We want to collect a variety of attacks against IoT devices. These attacks should abuse common vulnerabilities of devices. The attacks or scans should be easily executable within a framework.

## Framework

We use the [routersploit](https://github.com/gh0stsec/routersploit) framework for our attacks.
The framework is written in python. It can be executed with a simple `./rsf.py` using the shebang interpreter.
Routersploit supports separation between "exploits" and "scanners". We decided to add our attacks to the scanners module that then triggers various exploits. The forked project can be found [here](https://github.com/Toberd/routersploit).

## Basic Portscan

To get used to the routersploit framework we started our project by implementing a simple portscan.
It performs a TCP three-way-handshake to check if a certain port of a host is open. If the handshake could be done successfully the port is considered to be open. Otherwise it is closed. The result is printed to the console.

<img src="demo_portscan.jpg" width="600px" alt="Demo">

## Nmap

Nmap is a tool for scanning and analyzing a device for open ports. On top of that, once it found an open port it can have a deeper look if the port leads to a commonly known vulnerability.
There are many scripts available for different types of protocols, e.g. http, ssh, telnet.
Our idea is to pick some cool and relevant scripts and put them into our routersploit framework. They therefore need to be rewritten in Python since they are currently in the NSE (Nmap Scripting Engine) format.

## Testing

Since we cannot run our scanners in a real world IoT lab we need some sort of simulation.
For some protocols there exist docker images that let us spawn a single service running behind a single port (e.g. mysql, telnet).
Our scripts can be executed individually. This is why we think that spawning single services on different containers is perfectly enough. There is no need to combine a lot of services together to simulate a complete IoT device at once.
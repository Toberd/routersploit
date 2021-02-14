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

<img src="demo_portscan.jpg" width="400px" alt="Demo">
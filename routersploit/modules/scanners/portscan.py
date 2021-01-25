import socket

from routersploit import (
    exploits,
    print_info,
    print_status,
    print_error,
)


class Exploit(exploits.Exploit):
    """
    Scanner implementation for all vulnerabilities.
    """
    __info__ = {
        'name': 'Portscan',
        'description': 'Scanner for open ports.',
        'authors': [
            'Dimitri Harkovski <s8ddhark[at]stud.uni-saarland.de>',
            'Tobias Berdin <s8toberd[at]stud.uni-saarland.de>'
        ],
        'references': (
            '',
        ),
        'devices': (
            'Multi',
        ),
    }
    modules = None

    target = exploits.Option('', 'Target IP address e.g. 192.168.1.1')  # target address

    def run(self):
        for port in range(50):  # TODO adjust range
            print_status("Checking port {}...".format(port))
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                s.connect((self.target, port))
                print_status("Open port {}".format(port))
            except:
                print_error("No open port {}".format(port))
            s.close()

    def check(self):
        print_info("Not implemented yet")
        # TODO

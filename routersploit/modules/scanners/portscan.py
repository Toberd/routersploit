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
    min_port = exploits.Option(1, 'Minimum port to be scanned (default 1)')  # minimum port to be scanned
    max_port = exploits.Option(10, 'Maximum port to be scanned (default 10)')  # maximum port to be scanned

    def run(self):
        if int(self.min_port) > int(self.max_port):
            print_error("Minimum port must not be higher than maximum port")
            return
        for port in range(int(self.min_port), int(self.max_port)):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                s.connect((self.target, port))
                print_status("Open port {}".format(port))
            except:
                print_error("No open port {}".format(port))
            s.close()
        print_status("Done")

    def check(self):
        print_info("Not implemented yet")
        # TODO

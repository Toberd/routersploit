import socket

from routersploit import (
    exploits,
    print_info,
    print_status,
    print_error,
)


class Exploit(exploits.Exploit):
    """
    Scanner implementation for xss vulnerability.
    """
    __info__ = {
        'name': 'XSS Scanner',
        'description': 'Scanner for Cross-Site Scripting.',
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
    timeout = exploits.Option(1, 'Timeout for the connection e.g 1 (second)')  # timeout

    ports = [80, 443, 8000]  # default ports for http / https servers

    def run(self):
        for port in self.ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(float(self.timeout))
            try:
                s.connect((self.target, port))
                # TODO implement xss scan here
            except:
                print_error("Port {} is not open".format(port))
            s.close()

    def check(self):
        print_info("Not implemented yet")
        # TODO

from __future__ import absolute_import

from .autopwn import Exploit as BaseScanner


class Exploit(BaseScanner):
    """
    Scanner implementation for generic vulnerabilities.
    """
    __info__ = {
        'name': 'Generic Scanner',
        'description': 'Scanner module for generic devices',
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
    modules = ['misc/generic']

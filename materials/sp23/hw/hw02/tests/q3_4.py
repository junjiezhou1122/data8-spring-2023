OK_FORMAT = True
test = {   'name': 'q3_4',
    'points': [1, 1, 1, 1],
    'suites': [   {   'cases': [   {   'code': '>>> # It looks like you multiplied and subtracted in the wrong\n>>> # order.\n>>> sum(celsius_temps_rounded) != 356705.0\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> # Don't forget to round your final results\n>>> celsius_temps_rounded.item(1) == 31.0\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> sum(celsius_temps_rounded)\n1280677.0', 'hidden': False, 'locked': False},
                                   {'code': '>>> len(celsius_temps_rounded)\n65000', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

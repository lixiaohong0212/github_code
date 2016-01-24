#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Copyright (c) 2015 lixiaohong0212 <lixiaohong0212@gmail.com>
# All rights reserved


"""
"""

# $
__author__ = [
    'lixiaohong <lixiaohong0212@gmail.com>',
]
__version__ = ': 0.1 $'


import socket
import sys,json
sys.path.append('./gen-py')

from test_t import TestT
from test_t.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import arrow

class TestData(object):
    def getdata(self, client_string=''):

        tmp_dict = {
            'client_cmd': arrow.utcnow().to('local').format('HH:mm:ss')
        }
        return json.dumps(tmp_dict)


handler = TestData()
processor = TestT.Processor(handler)
transport = TSocket.TServerSocket('127.0.0.1', 9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

#server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

print "Starting thrift server in python..."
server.serve()
print "done!"



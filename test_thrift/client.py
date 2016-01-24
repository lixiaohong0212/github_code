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

import sys,json
sys.path.append('./gen-py')

from test_t import TestT

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

transport = TSocket.TSocket('127.0.0.1', 9090)
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = TestT.Client(protocol)
transport.open()

tmp_dict = {
    'lawyerid': 114196
}
client_string = json.dumps(tmp_dict)
msg = client.getdata(client_string)
print "server - " + msg

transport.close()

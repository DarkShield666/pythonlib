#!/usr/bin/python
# -*- coding: utf-8 -*-
# python3

# pip install hbase-thrift, 可以查看到安装路径
# 去github下载 https://github.com/626626cdllp/infrastructure/tree/master/hbase
# 替换python3 Hbase文件/usr/local/lib/python3.6/dist-packages/hbase/Hbase.py和ttypes.py
# (参考学习) https://blog.csdn.net/luanpeng825485697/article/details/81048468

# from thrift.transport import TSocket, TTransport
# from thrift.protocol import TBinaryProtocol
# from hbase import Hbase
# from hbase.ttypes import *


from thrift.transport import TSocket
from hbase import Hbase
from hbase.ttypes import *


class HbaseCn:
    def __init__(self, host, port):
        self.transport = TSocket.TSocket(host, port)
        self.transport = TTransport.TFramedTransport(self.transport)
        self.protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
        self.Hbase_client = Hbase.Client(self.protocol)
        self.transport.open()

    def query_data(self, tableName, row, column):
        data = self.Hbase_client.get(tableName, row, column)
        return data[0].value

    def insert_or_update_data(self, tableame, row, column, data):
        self.Hbase_client.mutateRow(tableame, row, [Mutation(column=column, value=data)])

    def hbase_close(self):
        self.transport.close()

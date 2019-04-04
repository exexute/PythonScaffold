#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-04 09:52:02
# @Author  : owefsad (1528360120@qq.com)
# @Link    : http://blog.51cto.com/executer
# @Version : $Id$


class SpiderMetaClass(type):
	def __new__(cls, name, bases, attrs):
		attrs["read_"+name[1:]] = lambda self, product, stype=name[1:]: print(stype, ",", product)


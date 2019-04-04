#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-03 23:31:59
# @Author  : owefsad (1528360120@qq.com)
# @Link    : http://blog.51cto.com/executer
# @Version : $Id$

import shodan

API_KEY=""

api=shodan.Shodan(API_KEY)

def search(keyword):
  results=api.search(keyword)
  return results['matches']

def parse(result):
  return (result['ip_str'], result['port'])

def get(keyword):
  ans=[]
  for result in search(keyword):
    ans.append(parse(result))
  return ans

if __name__=="__main__":
  for result in search("vsftpd 2.3.4"):
    parse(result)





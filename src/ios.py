#!/usr/bin/python
# -*- coding: utf-8 -*- 
import commands
import re

def get_device_list():
  _,res = commands.getstatusoutput('instruments -s devices')
  res_array = res.split("\n")
  pattern = re.compile(r'iP*')
  start = False
  list = []
  
  for item in res_array:
    if (start == True and pattern.match(item)):
      list.append([re.findall(r'(.+?) \[',item)[0], re.findall(r'\[(.+?)\]',item)[0]])
    if (item == 'Known Devices:'):
      start = True
  return list
  
def lanch_sim(id):
  commands.getstatusoutput('instruments -w ' + id)
  
#print(get_device_list())
#lanch_sim('1845594B-0BF7-4E3F-A4A9-708A140BFBD7')

#!/usr/bin/python
# -*- coding: utf-8 -*- 
import commands
import re

def android_device_list(sdk_path):
  _,res = commands.getstatusoutput( sdk_path + "tools/" + 'emulator -list-avds')
  res_array = res.split("\n")
  return res_array
  
def ios_device_list():
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

#print(_android_device_list())
#lanch_sim('1845594B-0BF7-4E3F-A4A9-708A140BFBD7')

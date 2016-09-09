#!/usr/bin/python
# -*- coding: utf-8 -*- 
import commands
import re

class Simulator:
  
  sdk_path = ""
  
  def __init__(self, path):
    self.sdk_path = path + "tools/"

  def android_device_list(self):
    _,res = commands.getstatusoutput( self.sdk_path + 'emulator -list-avds')
    res_array = res.split("\n")
    list = []
    for item in res_array:
       list.append([item, self.sdk_path + "emulator @" + item + '&amp;'])
    return list
    
  def ios_device_list(self):
    _,res = commands.getstatusoutput('instruments -s devices')
    res_array = res.split("\n")
    pattern = re.compile(r'iP*')
    start = False
    list = []
    
    for item in res_array:
      if (start == True and pattern.match(item)):
        udid = re.findall(r'\[(.+?)\]',item)[0]
        list.append([re.findall(r'(.+?) \[',item)[0], udid, 'instruments -w ' + udid])
      if (item == 'Known Devices:'):
        start = True
    return list
    
  def list(self, ios, android):
      print('<?xml version="1.0"?>')
      print('<items>')
      for item in ios:
        print("  <item uid=\"octal\" valid=\"yes\" arg=\""+item[2]+"\">")
        print("    <title>"+item[0]+"</title>")
        print('    <subtitle>UDID: '+ item[1] +'</subtitle>')
        print('    <icon>ios.png</icon>')
        print('  </item>')
      for item in android:
        print("  <item uid=\"octal\" valid=\"yes\" arg=\""+item[1]+"\">")
        print("    <title>"+item[0]+"</title>")
        print('    <subtitle>Android: '+ item[0] +'</subtitle>')
        print('    <icon>android.png</icon>')
        print('  </item>')
      print('</items>')
   
  def run(self):
    self.list(self.ios_device_list(), self.android_device_list())
      
#sim = Simulator('/Users/Yourtion/Codes/Apps/AndroidSDK/')
#print(sim.ios_device_list())
#lanch_sim('1845594B-0BF7-4E3F-A4A9-708A140BFBD7')

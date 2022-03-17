import os, sys, time, socket

from .messagram import *


class Json_Handle:
    """Verify if string is json or not."""
    def verify_json_data(data):
         if   isinstance(test_string,str):
            return False
         elif isinstance(test_string,dict):
            return True


class Buffer:
  global data
  global cmd
  global cmd_argv
  
  """
      Be aware, you might see some mistake since i language switch ALOT
    I work on these wrappers in most languages used today in 2022
  """
  
  def parse_cmd(data: str) -> str:
      """
    {
      "status": "true/false",
      "cmd": "msg",
      "userid": "username_here",
      "server_id": "",
      "content": ""
    }
    """
    
    
class Messagram:
  host = "skrillec.ovh"
  port = 30
  global socket
  
  def connect():
      Messagram.socket = socket.socket(AF_INET, SOCK_STREAM)
    Messagram.socket.connect((Messagram.host, Messagram.port))
    
    
  def listener():
      Buffer.data = Messagram.socket.recv(1024)
    if Buffer.cmd == "msg":
      ## get the msg.content
      ## get the msg author
      ## get the msg timestamp

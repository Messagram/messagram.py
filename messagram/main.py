import os, sys, time, socket

from .main import *

class Buffer:
    global data
    global data_argv

class Messagram:
    host = "skrillec.ovh"
    port = 30
    global conn
    def connect():
        Messagram.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Messagram.conn.connect((Messagram.host, Messagram.port))

    def listener():
        while(True):
            data = Messagram.conn.recv(1024)

            ## Validate the JSON data (to avoid errors)

            ## Parse the JSON data

            ## Handle the JSON data (if statement or match statement [py3.10+])

    def send_msg(msg):
        Messagram.conn.send(f"{msg}\n".encode())



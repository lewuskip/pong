#!/usr/bin/env python

import socket
import time
import curses


class Gong(object):
    SN = 1
    PORTS = [1001, 1002, 1003, 1004]
    TRIES_QUANTITY = 3
    TRIES_INTERVAL = 0.100

    def __init__(self, ipAddress):
        self.ip = ipAddress
        self.eventID = 1

    def sendSeries(self, msg):
        print (msg)
        for port in Gong.PORTS:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            sock.sendto(msg, (self.ip, port))

    def click(self):
        for x in range(Gong.TRIES_QUANTITY):
            msg = "event=click, seventID={},gongSN={}".format(self.eventID, Gong.SN)
            time.sleep(Gong.TRIES_INTERVAL)
            self.sendSeries(msg)
        self.eventID += 1



if __name__ == "__main__":
    #gong = Gong("192.168.0.29")
    gong = Gong("192.168.0.255")
    while True:
        time.sleep(3)
        gong.click()





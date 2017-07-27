#!/usr/bin/env python
import os
import io
import sys
import glob
import serial
import time
def main():
    # Open a file


    # Close opend file




    port = serial.Serial(serial_ports()[0], baudrate=115200, timeout=1.0)
    count = 0
    os.system("rm send.txt")
    while 1:
        #fo = open("foo.txt", "a")
        #string = "Log gonderildi " + str(count) + "...\n"
        toSend = open("send.txt", "wb")
        string = readlineCR(port)
        toSend.write(string)

        os.system("./TX_Demo send.txt")
        toSend.close
        #print string
        #time.sleep(0.1)
        #os.system("rm send.txt")

        #toSend = open("send.txt", "wb")
        #toSend.write(string);
        #toSend.close

    



def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

def readlineCR(port):
    rv = ""
    while True:
        ch = port.read()
        rv += ch
        if ch=='\r' or ch=='':
            return rv


if __name__ == "__main__":
	main();

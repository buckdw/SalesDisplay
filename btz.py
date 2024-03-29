import serial
import serial.tools.list_ports
import time

from velleman import *

def find_serial_port(filter):
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        usb_port = str(port)
        if filter in usb_port:
            return usb_port
    return None

if __name__ == "__main__":
    port = find_serial_port("cu.usb")
    print(port)
    serial_connection = serial.Serial(port
                                      , baudrate='9600'
                                      , parity=serial.PARITY_NONE
                                      , stopbits=1
                                      , bytesize=serial.EIGHTBITS
                                      , xonxoff=True
                                      , rtscts=False
                                      , dsrdtr=False
                                      )

    line = send_page(ID00
                     , 1
                     , 'A'
                     , COLOR_RED
                     , WAIT_3S
                     , 'baanthaizeeland.nl'
                     )
    print(line)
    time.sleep(3)
    serial_connection.write(line.encode())

    line = send_page(ID00
                     , 1
                     , 'B'
                     , COLOR_RED
                     , WAIT_3S
                     , 'Gino, Noi'
                     )
    print(line)
    time.sleep(3)
    serial_connection.write(line.encode())

    line = send_page(ID00
                     , 1
                     , 'C'
                     , COLOR_RED
                     , WAIT_3S
                     , 'Tel: 06 2918 6535'
                     )
    print(line)
    time.sleep(3)
    serial_connection.write(line.encode())

    line = send_page(ID00
                     , 1
                     , 'D'
                     , COLOR_RED
                     , WAIT_3S
                     , '30 min: EUR 35.00'
                     )
    print(line)
    time.sleep(3)
    serial_connection.write(line.encode())

    line = send_page(ID00
                     , 1
                     , 'E'
                     , COLOR_RED
                     , WAIT_3S
                     , '45 min: EUR 50.00'
                     )
    print(line)
    time.sleep(3)
    serial_connection.write(line.encode())

    line = send_page(ID00
                     , 1
                     , 'F'
                     , COLOR_RED
                     , WAIT_3S
                     , '60 min: EUR 60.00'
                     )
    print(line)
    time.sleep(3)
    serial_connection.write(line.encode())

    line = send_page(ID00
                     , 1
                     , 'G'
                     , COLOR_RED
                     , WAIT_3S
                     , '90 min: EUR 85.00'
                     )
    print(line)
    time.sleep(3)
    serial_connection.write(line.encode())

    line = send_page(ID00
                     , 1
                     , 'H'
                     , COLOR_RED
                     , WAIT_3S
                     , '120 min: EUR 110.00'
                     )
    print(line)
    time.sleep(3)
    serial_connection.write(line.encode())

    line = send_page(ID00
                     , 1
                     , 'I'
                     , COLOR_RED
                     , WAIT_3S
                     , '60 min + toksen: EUR 70.00'
                     )
    print(line)
    time.sleep(3)
    serial_connection.write(line.encode())

    line = link_pages(ID00, 'ABCDEFGHI')
    print(line)
    time.sleep(3)
    serial_connection.write(line.encode())
    serial_connection.close()

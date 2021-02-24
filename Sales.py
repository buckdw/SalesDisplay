import serial
import time

from velleman import *

if __name__ == "__main__":
    serial_connection = serial.Serial('/dev/cu.usbserial-1410'
                                      , baudrate='9600'
                                      , parity=serial.PARITY_NONE
                                      , stopbits=1
                                      , bytesize=serial.EIGHTBITS
                                      , xonxoff=True
                                      , rtscts=False
                                      , dsrdtr=False
                                      )
#  line = send_page(ID00
#                   , 1
#                   , 'A'
#                   , COLOR_RED
#                   , WAIT_3S
#                   , FUNCTION_SPEED_1
#                   )
#  print(line)
#  time.sleep(3)
#  serial_connection.write(line.encode())

    line = send_page(ID00
                     , 1
                     , 'A'
                     , COLOR_RED
                     , WAIT_3S
                     , 'baanthaimassage.nl'
                     )
    print(line)
    time.sleep(3)
    serial_connection.write(line.encode())

    line = send_page(ID00
                     , 1
                     , 'B'
                     , COLOR_AMBER
                     , WAIT_3S
                     , 'Noi en Pui'
                     )
    print(line)
    time.sleep(3)
    serial_connection.write(line.encode())

    line = send_page(ID00
                     , 1
                     , 'C'
                     , COLOR_AMBER
                     , WAIT_3S
                     , 'Tel: 06 1086 0150'
                     )
    print(line)
    time.sleep(3)
    serial_connection.write(line.encode())

    line = send_page(ID00
                     , 1
                     , 'D'
                     , COLOR_GREEN
                     , WAIT_3S
                     , '30 min: EUR 35.00'
                     )
    print(line)
    time.sleep(3)
    serial_connection.write(line.encode())

    line = send_page(ID00
                     , 1
                     , 'E'
                     , COLOR_GREEN
                     , WAIT_3S
                     , '45 min: EUR 50.00'
                     )
    print(line)
    time.sleep(3)
    serial_connection.write(line.encode())

    line = send_page(ID00
                     , 1
                     , 'F'
                     , COLOR_GREEN
                     , WAIT_3S
                     , '60 min: EUR 60.00'
                     )
    print(line)
    time.sleep(3)
    serial_connection.write(line.encode())

    line = send_page(ID00
                     , 1
                     , 'G'
                     , COLOR_GREEN
                     , WAIT_3S
                     , '90 min: EUR 85.00'
                     )
    print(line)
    time.sleep(3)
    serial_connection.write(line.encode())

    line = send_page(ID00
                     , 1
                     , 'H'
                     , COLOR_GREEN
                     , WAIT_3S
                     , '120 min: EUR 105.00'
                     )
    print(line)
    time.sleep(3)
    serial_connection.write(line.encode())

    line = link_pages(ID00, 'ABCDEFGH')
    print(line)
    time.sleep(3)
    serial_connection.write(line.encode())
    serial_connection.close()
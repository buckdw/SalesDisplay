import serial
import time


ID00 = '<ID00>'
ID01 = '<ID01>'
ID02 = '<ID02>'

WAIT_1S = '<WB>'
WAIT_2S = '<WC>'
WAIT_3S = '<WD>'
WAIT_4S = '<WE>'

PAGE_A = '<PA>'
PAGE_B = '<PB>'
PAGE_C = '<PC>'
PAGE_D = '<PD>'
PAGE_E = '<PE>'
PAGE_F = '<PF>'
PAGE_G = '<PG>'
PAGE_H = '<PH>'
PAGE_I = '<PI>'
PAGE_J = '<PJ>'
PAGE_K = '<PK>'
PAGE_L = '<PL>'
PAGE_M = '<PM>'

COLOR_RED = '<CA>'
COLOR_GREEN = '<CF>'
COLOR_AMBER = '<CI>'
COLOR_RYG = '<CR>'

FUNCTION_SPEED_1 = '<FX>'
FUNCTION_SPEED_2 = '<FY>'
FUNCTION_SPEED_3 = '<FZ>'


def checksum(buffer):
    checksum_i = int(0)

    for element in buffer:
        element_i = ord(element)
        checksum_i ^= element_i
    return checksum_i


def init_id(id_number):
    display_buffer = '<ID>{id_number}<E>'.format(id_number=id_number)
    return display_buffer

#
#   delete_all:
#
def delete_all(id):

    def data_packet():
        checksum_buffer = '<D*>'
        return checksum_buffer

    cs = checksum(data_packet())
    display_buffer = '{id}{data_packet}{cs:02X}<E>'.format(
        id=id
        , data_packet=data_packet()
        , cs=cs
    )
    return display_buffer

#
#   delete_page:
#
def delete_page(id, page_id, line):

    def data_packet(page, line):
        checksum_buffer = '<DLXP{page_id}{line}>'.format(page_id=page_id, line=line)
        return checksum_buffer

    cs = checksum(data_packet(page_id, line))
    display_buffer = '{id}{data_packet}{cs:02X}<E>'.format(
        id=id
        , data_packet=data_packet(page_id, line)
        , cs=cs
    )
    return display_buffer

#
#   link_pages:
#       tell Vellemann Display which programmmed pages to show
#
def link_pages(id, pages):

    def data_packet(pages):
        checksum_buffer = '<TA>00010100009912312359{pages}'.format(pages=pages)
        return checksum_buffer

    cs = checksum(data_packet(pages))
    display_buffer = '{id}{data_packet}{cs:02X}<E>'.format(
        id=id
        , data_packet=data_packet(pages)
        , cs=cs
    )
    return display_buffer

#
#   display_page
#       define a Page within Vellemann Display
#
def send_page(id, line_id, page, color, wait, request):

    def data_packet(line_id, page, color, wait, request):
        checksum_buffer = '<L{line_id}>{page}<FE><MA>{wait}<FE>{color}{request}'.format(
              line_id=line_id
            , page=page
            , wait=wait
            , color=color
            , request=request
        )
        return checksum_buffer

    cs = checksum(data_packet(line_id, page, color, wait, request))
    display_buffer = '{id}{data_packet}{cs:02x}<E>'.format(
        id=id
        , data_packet=data_packet(line_id, page, color, wait, request)
        , cs=cs
    )
    return display_buffer


if __name__ == "__main__":
    serial_connection = serial.Serial('/dev/cu.usbserial'
                                      , baudrate='9600'
                                      , parity=serial.PARITY_NONE
                                      , stopbits=1
                                      , bytesize=serial.EIGHTBITS
                                      , xonxoff=True
                                      , rtscts=True
                                      , dsrdtr=True
                                      )

    line = send_page(ID02, 1, PAGE_A, COLOR_RED, WAIT_4S, 'SokoZuur: E88.000')
    print(line)
    serial_connection.write(line.encode())
    time.sleep(1)

    line = send_page(ID02, 1, PAGE_B, COLOR_RED, WAIT_4S, 'Buzl: E41.000')
    print(line)
    serial_connection.write(line.encode())
    time.sleep(1)

    line = send_page(ID02, 1, PAGE_C, COLOR_RED, WAIT_4S, 'Zeug: E41.000')
    print(line)
    serial_connection.write(line.encode())
    time.sleep(1)

    line = send_page(ID02, 1, PAGE_D, COLOR_RED, WAIT_4S, 'Zeug: E41.000')
    print(line)
    serial_connection.write(line.encode())
    time.sleep(1)

    line = link_pages(ID02, 'ABCD')
    print(line)
    serial_connection.write(line.encode())
    time.sleep(1)

    serial_connection.close()
import serial


ID01 = '<ID01>'
ID02 = '<ID02>'

WAIT_1S = '<WB>'
WAIT_2S = '<WC>'
WAIT_3S = '<WD>'

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
    display_buffer = '<ID>{id_number}<E>\n\r'.format(id_number=id_number)
    return display_buffer

#
#   link_pages:
#       tell Vellemann Display which programmmed pages to show
#
def delete_page(id, page_id, line):

    def data_packet(page, line):
        checksum_buffer = '<DLXP{page_id}{line}>'.format(page_id=page_id, line=line)
        return checksum_buffer

    cs = checksum(data_packet(page_id, line))
    display_buffer = '{id}{checksum_buffer}{checksum:02X}<E>\n\r'.format(
        id=id
        , checksum_buffer=data_packet(page_id, line)
        , checksum=cs
    )
    return display_buffer

#
#   link_pages:
#       tell Vellemann Display which programmmed pages to show
#
def link_pages(pages):

    def data_packet(pages):
        checksum_buffer = '<TA>00010100009912302359{pages}'.format(pages=pages)
        return checksum_buffer

    cs = checksum(data_packet(pages))
    display_buffer = '<ID01>{checksum_buffer}{checksum:02X}<E>\n\r'.format(
        checksum_buffer=data_packet(pages)
        , checksum=cs
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
    display_buffer = '{id}{checksum_buffer}{checksum:02x}<E>\n\r'.format(
        id=id
        , checksum_buffer=data_packet(line_id, page, color, wait, request)
        , checksum=cs
    )
    return display_buffer


if __name__ == "__main__":
    serial_connection = serial.Serial('/dev/cu.usbserial'
                                      , baudrate='9600'
                                      , parity=serial.PARITY_NONE
                                      , stopbits=1
                                      , bytesize=serial.EIGHTBITS
                                      , xonxoff=True
                                      )

    line = init_id('01')
    print(line)
    serial_connection.write(line.encode())

 #   for i in range(8):
 #       line = delete_page(ID01, 'C', i+1)
 #       print(line)
 #       serial_connection.write(line.encode())

    line = send_page(ID01, 1, PAGE_A, COLOR_GREEN, WAIT_3S, 'SokoZuur: E12.789')
    print(line)
    serial_connection.write(line.encode())

    line = send_page(ID01, 2, PAGE_A, COLOR_RED, WAIT_3S, 'Buzl: E41.000')
    print(line)
    serial_connection.write(line.encode())

    line = send_page(ID01, 3, PAGE_A, COLOR_RED, WAIT_3S, 'Zeug: E41.000')
    print(line)
    serial_connection.write(line.encode())

    line = send_page(ID01, 4, PAGE_A, COLOR_RED, WAIT_3S, 'Zeug: E41.000')
    print(line)
    serial_connection.write(line.encode())

    line = link_pages('A')
    print(line)
    serial_connection.write(line.encode())

    serial_connection.close()
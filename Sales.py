import serial

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
COLOR_GREEN = '<CD>'
COLOR_AMBER = '<CG>'
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


def link_pages(pages):

    def format_checksum_buffer(pages):
        checksum_buffer = '<TA>00010100009912302359{pages}'.format(
            pages=pages
        )
        return checksum_buffer

    checksum_request = checksum(format_checksum_buffer(pages))
    display_buffer = '<ID00>{checksum_buffer}{checksum:02X}<E>\n\r'.format(
        checksum_buffer=format_checksum_buffer(pages)
        , checksum=checksum_request
    )
    return display_buffer


def display_page(page, color, request):

    def format_checksum_buffer(page, color, request):
        checksum_buffer = '<L1>{page}<FE><MA><WC><FE>{color}{request}'.format(
            page=page
            , color=color
            , request=request
        )
        return checksum_buffer

    checksum_request = checksum(format_checksum_buffer(page, color, request))
    display_buffer = '<ID00>{checksum_buffer}{checksum:02x}<E>\n\r'.format(
        checksum_buffer=format_checksum_buffer(page, color, request)
        , checksum=checksum_request
    )
    return display_buffer


if __name__ == "__main__":
    ser = serial.Serial('/dev/cu.usbserial')

    line = display_page(PAGE_A, COLOR_RED, FUNCTION_SPEED_1)
    print(line)
    ser.write(line.encode())

    line = display_page(PAGE_A, COLOR_RED, 'SokoZuur: E12.789')
    print(line)
    ser.write(line.encode())

    line = display_page(PAGE_B, COLOR_RED, 'Buzl: E41.000')
    print(line)
    ser.write(line.encode())

    line = link_pages('AB')
    print(line)
    ser.write(line.encode())

    ser.close()
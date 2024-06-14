#
# if changed run `configuration-generate.py`
# if `RAM_ADDR_WIDTH` is modified recompile `os`
#
RAM_FILE = "os/os.mem" # path to initial RAM content
RAM_ADDR_WIDTH = 14    # 2^14*4 (65536) bytes of RAM
UART_BAUD_RATE = 9600  # 9600 baud, 8 bits, 1 stop bit, no parity

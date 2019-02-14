import errno
import random
import string
import serial


def increment_data(data):
    """Increment each character."""
    return ''.join(chr(ord(n) + 1) for n in data)


def create_random_data(data_len):
    """Generate random data with specified length."""
    return 't' + ''.join([random.choice(
        string.digits) for n in range(data_len)])


TEST_STRING_FOR_STOP_BITS = "tttt"
SHORT_TEST_STRING = "t111"
SHORT_TEST_STRING_INC = increment_data(SHORT_TEST_STRING)
LONG_TEST_STRING = create_random_data(42)
LONG_TEST_STRING_INC = increment_data(LONG_TEST_STRING)

REG_1_WRITE = "\"wr 1 10 1\""
REG_1_READ = "\"rr 1 1\""
REG_1_READ_DATA = "0,0x0A"
REG_WRONG_READ = "\"rr -1 10\""
REG_WRONG_READ_DATA = [errno.EINVAL]

UART_DATA_BITS_7 = serial.SEVENBITS
UART_DATA_BITS_8 = serial.EIGHTBITS

UART_PARITY_NONE = serial.PARITY_NONE
UART_PARITY_EVEN = serial.PARITY_EVEN
UART_PARITY_ODD = serial.PARITY_ODD

UART_STOP_BITS_1 = serial.STOPBITS_ONE
UART_STOP_BITS_2 = serial.STOPBITS_TWO

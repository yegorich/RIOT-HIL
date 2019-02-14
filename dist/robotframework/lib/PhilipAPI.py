import serial

from riot_pal import LLMemMapIf, PHILIP_MEM_MAP_PATH
from robot.version import get_version
from time import sleep


class PhilipAPI(LLMemMapIf):

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    ROBOT_LIBRARY_VERSION = get_version()

    def __init__(self, port, baudrate):
        super(PhilipAPI, self).__init__(PHILIP_MEM_MAP_PATH, 'serial', port, baudrate)

    def reset_dut(self):
        ret = list()
        ret.append(self.write_reg('sys.cr', 0xff))
        ret.append(self.execute_changes())
        sleep(1)
        ret.append(self.write_reg('sys.cr', 0x00))
        ret.append(self.execute_changes())
        sleep(1)
        return ret

    def setup_uart(self, mode=0, baudrate=115200,
                   databits=serial.EIGHTBITS, parity=serial.PARITY_NONE,
                   stopbits=serial.STOPBITS_ONE, rts=True):
        '''Setup tester's UART.'''
        ret = list()
        ret.append(self.write_reg('uart.mode', int(mode)))

        ret.append(self.write_reg('uart.baud', int(baudrate)))

        if databits == serial.SEVENBITS:
            ret.append(self.write_reg('uart.ctrl.data_bits', 1))
        elif databits == serial.EIGHTBITS:
            ret.append(self.write_reg('uart.ctrl.data_bits', 0))

        if parity == serial.PARITY_NONE:
            ret.append(self.write_reg('uart.ctrl.parity', 0))
        elif parity == serial.PARITY_EVEN:
            ret.append(self.write_reg('uart.ctrl.parity', 1))
        elif parity == serial.PARITY_ODD:
            ret.append(self.write_reg('uart.ctrl.parity', 2))

        if stopbits == serial.STOPBITS_ONE:
            ret.append(self.write_reg('uart.ctrl.stop_bits', 0))
        elif stopbits == serial.STOPBITS_TWO:
            ret.append(self.write_reg('uart.ctrl.stop_bits', 1))

        # invert RTS level as it is a low active signal
        if rts:
            ret.append(self.write_reg('uart.ctrl.rts', 0))
        else:
            ret.append(self.write_reg('uart.ctrl.rts', 1))

        # reset status register
        ret.append(self.write_reg('uart.status', 0x00))

        # apply changes
        ret.append(self.execute_changes())
        sleep(1)
        return ret

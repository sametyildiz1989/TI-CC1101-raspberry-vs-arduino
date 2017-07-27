from fcntl import ioctl
from ctypes import *

I2C_M_TEN           = 0x0010    # this is the ten bit chip address
I2C_M_RD            = 0x0001    # read data, from slave to master
I2C_M_STOP          = 0x8000    # if I2C_FUNC_PROTOCOL_MANGLING
I2C_M_NOSTART       = 0x4000    # if I2C_FUNC_NOSTART
I2C_M_REV_DIR_ADDR  = 0x2000    # I2C_FUNC_PROTOCOL_MANGLING
I2C_M_IGNORE_NAK    = 0x1000    # I2C_FUNC_PROTOCOL_MANGLING
I2C_M_NO_RD_ACK     = 0x0800    # I2C_FUNC_PROTOCOL_MANGLING
I2C_M_RECV_LEN      = 0x0400    # length will be first received byte

I2C_SLAVE           = 0x0703    # use this slave address
I2C_SLAVE_FORCE     = 0x0706    # use this slave addres, even if
                                # is already is use by a driver
I2C_TENBIT          = 0x0704    # 0 for 7 bit addrs, !=0 for 10-bit
I2C_FUNCS           = 0x0705    # get the adapter functionality mask
I2C_RDWR            = 0x0707    # combined R/W transfer (one STOP only)
I2C_PEC             = 0x0708    # !=0 to use PEC with SMBus
I2C_SMBUS           = 0x0720    # SMBus transfer

class i2c_msg(Structure):
    _fields_ = [
        ('addr',    c_uint16),
        ('flags',   c_uint16),
        ('len',     c_uint16),
        ('buf',     POINTER(c_uint8))
    ]

class i2c_rdwr_ioctl_data(Structure):
    _fields_ = [
        ('msgs',   POINTER(i2c_msg)),
        ('nmsgs',   c_uint32)
    ]

with open('/dev/i2c-1', 'r+b') as i2c:
    # first send a write with the config register address
    messages_array      = i2c_msg*2
    messages            = messages_array()
    messages[0].addr    = 0x48
    messages[0].flags   = 0
    messages[0].len     = 1
    reg                 = c_uint8(0x00)
    messages[0].buf     = pointer(reg)
    #Then send a read request for 2 bytes
    messages[1].addr    = 0x48
    messages[1].flags   = I2C_M_RD
    messages[1].len     = 2
    result_type         = c_uint8*2
    result              = result_type()
    messages[1].buf     = cast(pointer(result), POINTER(c_uint8))
    # now build the ioctl request with the messages
    request             = i2c_rdwr_ioctl_data()
    request.msgs        = messages
    request.nmsgs       = 2
    ioctl(i2c.fileno(), I2C_RDWR, request)
    print('Result = 0x{0:0X}{1:0X}'.format(result[0], result[1]))

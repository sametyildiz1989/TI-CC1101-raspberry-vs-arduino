import smbus

BUS     = 1 #which smbus to use --> /dev/i2c-1 kullanacaz
ADDRESS = 0x48 # address of the device to talk to over I2C/smbus

#setup SMBus access
bus = smbus.SMBus(BUS)

# Read two bytes from register 01, the config register
config = bus.read_word_data(ADDRESS, 0x01) & 0xFFFF
print('Config value: 0x{0:04X}'.format(config))

# write two bytes to the config register
new_config = 0b0100001110000011
bus.write_word_data(ADDRESS, 0x01, new_config)

#read two bytes from register 00,the ADC value
value = bus.read_word_data(ADDRESS, 0x00) & 0xFFFF
#Swap byte order from little endian to big endian
value = ((value & 0xFF) << 8) | (value >> 8)
print('Raw ADC value: 0x{0:04X}'.format(value))

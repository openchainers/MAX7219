from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.legacy import show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT


serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=1, block_orientation=0, rotate=0)
print("Created device")

message = "Hello, World!"
print(message)
show_message(device, message, fill="white", font=proportional(LCD_FONT), scroll_delay=1)

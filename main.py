import network
import machine
import time

red = machine.Pin(27, machine.Pin.OUT)
blue = machine.Pin(25, machine.Pin.OUT)

machine.freq(240000000)

red.value(1)
blue.value(0)
print("Initialising network")

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(ssid="ESP32_Minecraft_Lan", password="enderman", authmode=3)

time.sleep(2)

red.value(0)
blue.value(1)
print("Network's live!")

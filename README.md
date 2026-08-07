# ESP32-Minecraft-Micropython-Lan-Router
Turn an ESP32 running MicroPython into an offline, zero-latency Wi-Fi access point for Minecraft LAN gaming without needing an internet connection or home router.

## Setup Steps

1. **Flash MicroPython:** Install the latest MicroPython firmware onto your ESP32 board using Thonny IDE or `esptool`.
2. **Upload Code:** Save `main.py` directly to the ESP32 root directory.
3. **Power On ESP32:** Plug the ESP32 into a USB power bank or power source.

---

### Joining the Network

#### For Bedrock / Pocket Edition (Mobile, Console, Windows):
1. **Load World First:** Connect to cellular data or home Wi-Fi, open Minecraft, and spawn into your minecraft world.
2. **Switch Wi-Fi:** While inside the loaded world, switch your device's Wi-Fi connection to `ESP32_Minecraft_Lan` (Password: `enderman`).
3. **Play:** Other players connected to the ESP32 network can now open Minecraft and tap on the Play button, there will be an option to join your friends world.

#### For Java Edition (PC):
1. **Connect Wi-Fi:** Connect your PC directly to `ESP32_Minecraft_Lan` (Password: `enderman`).
2. **Search Tutorial:** Watch a quick tutorial on how to Host and Join a Minecraft Java LAN World.

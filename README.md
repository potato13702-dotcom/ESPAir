# ESP32 MicroPython Minecraft LAN Router

> **Built by a 13-year-old 8th-grade student maker!** 🚀  
> This project turns an inexpensive ESP32 microcontroller into a dedicated, offline local access point tailored specifically for lag-free Minecraft LAN gaming.

---

## About the Project

This project uses MicroPython to transform an ESP32 into a standalone, zero-latency Wi-Fi access point (AP). It creates a dedicated local bridge for Minecraft multiplayer sessions without requiring a home router, cellular data, or an active internet connection.

---

## Hardware & Status Indicator Setup (Optional)

The project uses a **4-pin Common Cathode RGB LED** (or two separate LEDs) to provide instant visual feedback on the network status:

| Status | LED Color | Pin Connection | Description |
| :--- | :--- | :--- | :--- |
| **Initializing** | 🔴 Red | GPIO 27 | ESP32 is booting up and initializing the AP network. |
| **Network Live** | 🔵 Blue | GPIO 25 | Network is active and ready for players to connect! |

* **GND Pin:** Connected to ESP32 Ground (`GND`).
* **Red Anode Pin:** Connected to GPIO 27.
* **Blue Anode Pin:** Connected to GPIO 25.

---

## Setup Steps

1. **Flash MicroPython:** Install the latest MicroPython firmware onto your ESP32 board using Thonny IDE or `esptool`.
2. **Upload Code:** Copy the code from `main.py` and paste it into your ESP32's main.py folder running Micropython.
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

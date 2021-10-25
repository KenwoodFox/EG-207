EG-207
======

[![Delint Python](https://github.com/KenwoodFox/EG-207-CCEMS/actions/workflows/delint-python.yml/badge.svg)](https://github.com/KenwoodFox/EG-207-CCEMS/actions/workflows/delint-python.yml)
[![Make Arduino](https://github.com/KenwoodFox/EG-207-CCEMS/actions/workflows/make-arduino.yml/badge.svg)](https://github.com/KenwoodFox/EG-207-CCEMS/actions/workflows/make-arduino.yml)
[![Make Docs](https://github.com/KenwoodFox/EG-207-CCEMS/actions/workflows/make-docs.yml/badge.svg)](https://github.com/KenwoodFox/EG-207-CCEMS/actions/workflows/make-docs.yml)
[![Submit Release](https://github.com/KenwoodFox/EG-207-CCEMS/actions/workflows/publish-release.yml/badge.svg)](https://github.com/KenwoodFox/EG-207-CCEMS/actions)
[![Discord](https://img.shields.io/discord/886985777085566986.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://discord.gg/vbgyRJBJCs)

Feel free to fork or create your own PRs! Join us on our [discord](https://discord.gg/vbgyRJBJCs)!


# Building and Installation

## From Source

### Requisites

Start by collecting all the neccicary requirements.

#### Arch

```
pacman -S base-devel curl
```

#### Ubuntu/Debian

```
sudo apt install build-essential curl
```

Navigate to the arduino code and invoke make

```
cd arduino/src
make
```

to upload to the sensor package, use 

```
make upload
```

## From a release

Download a binary from the [releases](https://github.com/KenwoodFox/EG-207-CCEMS/releases) page.

Have either `arduino-cli` or the `arduino-ide` available, and flash the sensor package with a pre-made hex.

```
arduino-cli upload -i CCEMS_v0.2.hex
```

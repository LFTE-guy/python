# Byte Strand Inspector (`hexa.py`)

A minimal, first-principles Python utility for inspecting text payloads at the raw byte level across four fundamental data representations: **ASCII, Decimal, Hexadecimal, and Binary**.

## Purpose

High-level abstractions often obscure how data actually looks in memory. In reverse engineering, network protocol analysis, and cryptography, text isn't just text—it is a sequence of 8-bit bytes. 

I built this lightweight tool to:
* Bridge the gap between human-readable strings and raw memory representations.
* Validate character-to-byte translations without relying on heavy external tools or black-box decoders.
* Inspect space delimiters (`0x20`), ASCII anchors, and individual byte boundaries in real-time.

## How It Works

`hexa.py` iterates through input strings at the single-character (byte) level. Rather than treating input as a high-level string object, it uses `ord()` to pull out the raw underlying integer value before projecting it into Hex (`0x..`) and Binary (`0b..`) formats.

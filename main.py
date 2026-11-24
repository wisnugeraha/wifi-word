#!/usr/bin/env python3
"""Maybe — make.fun entry (u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)"""
import os

ENTRY_LINE = "maybe"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w") as f:
    f.write(ENTRY_LINE + "\n")

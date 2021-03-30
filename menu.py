#!/usr/bin/env python3
from __future__ import print_function

from telemetry import client
import asyncio


import sys, select
import termios
from timeit import default_timer as timer
from argparse import ArgumentParser

import asyncio
from mavsdk import System

try:
    from pymavlink import mavutil
except ImportError as e:
    print("Failed to import pymavlink: " + str(e))
    print("")
    print("You may need to install it with:")
    print("    pip3 install --user pymavlink")
    print("")
    sys.exit(1)

try:
    import serial
except ImportError as e:
    print("Failed to import pyserial: " + str(e))
    print("")
    print("You may need to install it with:")
    print("    pip3 install --user pyserial")
    print("")
    sys.exit(1)

if __name__ == "__main__":
  # Declarations
  loop = asyncio.get_event_loop()
  i = ""

  # Menu
  while(i != "7"):
    print("Menu")
    print("\t1 - Connect a drone")
    print("\t2 - Download")
    print("\t3 - Upload")
    print("\t4 - List directory")
    print("\t5 - Reset server")
    print("\t6 - Test connection")

    i = input("Select an option: ")

    if(i == "1"):
      drone = loop.run_until_complete(client.connect_())
    if(i == "2"):
      remote_path = input("Insert the remote path: ")
      local_path = input("Insert the local path: ")
      client.download_(drone, remote_path, local_path)
    if(i == "3"):
      local_path = input("Insert the remote path: ")
      remote_path = input("Insert the remote path: ")
      client.upload_(drone, local_path, remote_path)
    if(i=="4"):
      remote_path =input("Insert a directory")
      client.list_directory_(drone, remote_path)
    if(i=="5"):
      client.reset_(drone)
    if(i=="6"):
      client.test_connection(drone)

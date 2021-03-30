#!/usr/bin/env python3

from __future__ import print_function
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


async def connect_():
  print("Connecting to the drone...")
  mav = mavutil.mavlink_connection("/dev/ttyUSB0", autoreconnect=True, baud=57600)
  print("Drone is connected!")
  print()
  return mav

def test_connection(mav):
  print(mav.wait_heartbeat())

def list_directory_(mav, path):
  #print(dir(mav))
  mav.

  '''

def download_(system ,remote_file_path, local_path):
  print("Download file: " + remote_file_path + "to " + local_path)

  for progress in system.ftp.download(remote_file_path, local_path):
    print("\tDownloading [" + str(progress.bytes_transferred/progress.total_bytes) + "%]")

def upload_(system, local_file_path, remote_dir):
  print("Upload file: " + local_file_path + " to " + remote_dir)

  for progress in system.ftp.upload(local_file_path, remote_dir):
    print("\tUploading [" + str(progress.bytes_transferred/progress.total_bytes) + "%]")

async def list_directory_(system, remote_dir):
  await system.ftp.list_directory(remote_dir)

async def reset_(system):
  print("Reseting the remote server...")
  await system.ftp.reset()
'''
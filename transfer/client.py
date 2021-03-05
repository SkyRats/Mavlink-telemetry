#!/usr/bin/env python3

import asyncio
from mavsdk import System

async def connect_(system):

  print("Connecting a drone...")
  print("\tConnection URL format should be: ")
  print("\tFor TCP : tcp://:[server_host][:server_port]")
  print("\tFor UDP : udp://[bind_host][:bind_port]")
  print("\tFor Serial : serial:///path/to/serial/dev[:baudrate]")
  url = "udp://:14550"

  await system.connect(system_address="udp://:14550")
  print("Waiting for drone to connect...")

  async for state in system.core.connection_state():
    if state.is_connected:
      print(f"Drone discovered with UUID: {state.uuid}")
      break

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

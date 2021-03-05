#!/usr/bin/env python3

from transfer import client
import asyncio

if __name__ == "__main__":
  # Declarations
  drone = client.System()
  loop = asyncio.get_event_loop()
  i = ""

  # Menu
  while(i != "6"):
    print("Menu")
    print("\t1 - Connect a drone")
    print("\t2 - Download")
    print("\t3 - Upload")
    print("\t4 - List directory")
    print("\t5 - Reset server")
    print("\t6 - Exit")

    i = input("Select an option: ")

    if(i == "1"):
      loop.run_until_complete(client.connect_(drone))
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

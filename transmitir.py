#!/usr/bin/env python3

import asyncio
from mavsdk import System

async def run():
    drone = System()
    await drone.connect(system_address="udp://:14550")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"Drone discovered with UUID: {state.uuid}")
            break

    print("Requesting a list of directories...")
    try:
        await drone.ftp.list_directory("./")
        print("First test completed")
    except:
        print("First test failed")

    try:
        drone

if __name__ == "__main__":
     loop = asyncio.get_event_loop()
     loop.run_until_complete(run())

#!/usr/bin/env python3

from mavsdk import System
import asyncio

async def run():

  drone = System()

  await drone.connect(system_address="serial:///dev:ttyACM0")
  async for state in drone.core.connection_state():
    if state.is_connected:
      print(f"Drone discovered with UUID: {state.uuid}")
      break

  async for distance in drone.telemetry.distance_sensor():
    print(f"Distance: {distance.current_distance_m}")

if __name__ == "__main__":
  loop = asyncio.get_event_loop()
  loop.run_until_complete(run())

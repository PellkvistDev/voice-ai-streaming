import asyncio
import websockets

async def handler(websocket, path):
    print("Client connected")
    async for message in websocket:
        print("Received:", message)
        await websocket.send("Echo: " + message)

async def main():
    # Start WebSocket server
    async with websockets.serve(handler, "0.0.0.0", 10001):
        print("WebSocket server started on port 10001")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())

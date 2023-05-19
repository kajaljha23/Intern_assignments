import asyncio
import websockets


async def client():
    async with websockets.connect('ws://localhost:8000') as websocket:
        message = "Kl intern!"
        await websocket.send(message)
        print(f"Sent message to server: {message}")

        # Receive and print the response from the server
        response = await websocket.recv()
        print(f"Received response from server: {response}")

asyncio.get_event_loop().run_until_complete(client())

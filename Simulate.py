from OSI_Layers.Application import ApplicationLayer
from OSI_Layers.Physical import PhysicalLayer

def main():
    port = 7777  # Keep the same port for all layers
    app = ApplicationLayer(port)

    # Sending message
    message = "Hello, OSI!"
    print(f"Original Message: {message}")

    PhysicalLayer.server_ready.wait()
    app.send(message)

    # Receiving message
    received_message = app.receive()
    print(f"Received Message: {received_message}")

if __name__ == "__main__":
    main()

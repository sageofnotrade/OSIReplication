from OSI_Layers.Application import ApplicationLayer
import time

def main():
    port = 12345  # Keep the same port for all layers
    app = ApplicationLayer(port)

    # Sending message
    message = "Hello, OSI!"
    print(f"Original Message: {message}")
    app.send(message)

    
    # Receiving message
    received_message = app.receive()
    print(f"Received Message: {received_message}")

if __name__ == "__main__":
    main()

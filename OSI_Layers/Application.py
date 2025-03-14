from OSI_Layers.Presentation import PresentationLayer

class ApplicationLayer:
    def __init__(self, port=12345):
        self.presentation = PresentationLayer(port=port)

    def send(self, message):
        """Create a simple HTTP-like request and send it."""
        request = f"GET / HTTP/1.1\nHost: localhost\n\n{message}"
        print(f"Application Layer Sending: {message}")
        self.presentation.send(request)

    def receive(self):
        """Receive data and extract message."""
        received_request = self.presentation.receive()
        print(f"Application Layer Receiving: {received_request}")
        return received_request.split("\n\n")[-1]
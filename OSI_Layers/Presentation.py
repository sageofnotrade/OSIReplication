import base64
from OSI_Layers.Session import SessionLayer

class PresentationLayer:
    def __init__(self, port=7777):
        self.session = SessionLayer(port=port)

    def send(self, data):
        """Encode data in Base64 before sending."""
        encoded_data = base64.b64encode(data.encode()).decode()
        print(f"Presentation Layer Sending: {data}")
        self.session.send(encoded_data)

    def receive(self):
        """Receive and decode Base64 data."""
        encoded_data = self.session.receive()
        print(f"Presentation Layer Receiving{encoded_data}")
        return base64.b64decode(encoded_data.encode()).decode()

from OSI_Layers.Transport import TransportLayer

class SessionLayer:
    def __init__(self, port=12345):
        self.session_id = "SESSION123"
        self.transport = TransportLayer(port=port)

    def send(self, data):
        """Add session ID and send."""
        session_data = f"{self.session_id}:{data}"
        print(f"Session Layer Sending: {data}")
        self.transport.send(session_data)

    def receive(self):
        """Receive and remove session ID."""
        session_data = self.transport.receive()
        print(f"Session Layer Receiving: {session_data}")
        return session_data.split(":", 1)[1]

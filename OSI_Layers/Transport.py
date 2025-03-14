from OSI_Layers.Network import NetworkLayer

class TransportLayer:
    def __init__(self, port=12345):
        self.sequence_number = 0
        self.network = NetworkLayer(port=port)

    def send(self, data):
        """Add a sequence number and send."""
        self.sequence_number += 1
        segment = f"SEQ{self.sequence_number}:{data}"
        print(f"Transport Layer Sending: {segment}")
        self.network.send(segment)

    def receive(self):
        """Receive and remove sequence number."""
        segment = self.network.receive()  # This is received as bytes
        segment_str = segment.decode()  # ✅ Convert from bytes to string

        print(f"Transport Layer Receiving: {segment_str}")  # ✅ Debugging print
        return segment_str.split(":", 1)[1]  # ✅ Now it will not throw an error

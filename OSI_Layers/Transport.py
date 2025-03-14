from OSI_Layers.Network import NetworkLayer

class TransportLayer:
    def __init__(self, port=12345):
        self.sequence_number = 0
        self.network = NetworkLayer(port=port)

    def send(self, data):
        """Add a sequence number and send."""
        self.sequence_number += 1
        segment = f"SEQ{self.sequence_number}:{data}"
        print(f"Transport Layer Sending: {data}")
        self.network.send(segment)

    def receive(self):
        """Receive and remove sequence number."""
        segment = self.network.receive()
        print(f"Transport Layer Receiving: {segment}")
        return segment.split(":", 1)[1]

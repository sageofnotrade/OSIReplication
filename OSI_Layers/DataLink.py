from OSI_Layers.Physical import PhysicalLayer

class DataLinkLayer:
    def __init__(self, mac_address="00:1A:2B:3C:4D:5E", port=12345):
        self.mac_address = mac_address
        self.physical = PhysicalLayer(port)

    def send(self, data, mac_address):
        frame = f"[MAC]{mac_address}||{data}[MAC_END]"
        print(f"Data Link Layer Sending: {frame}")
        return frame.encode()

    def receive(self, frame):
        frame_str = frame.decode()
        # Split on the unique delimiter "||"
        data = frame_str.split("||")[1].split("[MAC_END]")[0]
        print(f"Data Link Layer Received: {data}")
        return data.encode()
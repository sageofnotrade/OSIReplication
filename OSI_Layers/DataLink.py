from OSI_Layers.Physical import PhysicalLayer

class DataLinkLayer:
    def __init__(self, mac_address="00:1A:2B:3C:4D:5E", port=7777):
        self.mac_address = mac_address
        self.physical = PhysicalLayer(port=port)

    def send(self, data, mac_address):
        """Encapsulate data into a MAC frame and send it via the Physical Layer."""
        frame = f"[MAC]{mac_address}||{data}[MAC_END]"
        print(f"Data Link Layer Sending: {frame}")
        self.physical.send(frame) 

    def receive(self):
        """Receive a MAC frame, extract data, and return it."""
        received_frame = self.physical.receive()
        
        if "[MAC]" in received_frame and "[MAC_END]" in received_frame:
            data = received_frame.split("||")[1].split("[MAC_END]")[0]
            print(f"Data Link Layer Received: {data}")
            return data.encode()
        else:
            print("[Data Link Layer] Error: Malformed frame received.")
            return b""

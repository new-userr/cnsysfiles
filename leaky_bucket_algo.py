import time
from typing import List

class LeakyBucket:
    def __init__(self, capacity: float, leak_rate: float):
        """
        Initialize the LeakyBucket.
        
        :param capacity: Maximum capacity of the bucket (in packets)
        :param leak_rate: Rate at which packets leak out (packets per second)
        """
        self.capacity = capacity
        self.leak_rate = leak_rate
        self.bucket = 0.0
        self.last_time = time.time()

    def leak(self) -> None:
        """Simulate the leaking of packets from the bucket over time."""
        current_time = time.time()
        elapsed_time = current_time - self.last_time
        leaked_packets = elapsed_time * self.leak_rate
        self.bucket = max(0, self.bucket - leaked_packets)
        self.last_time = current_time

    def add_packet(self, packet_size: float) -> bool:
        """
        Attempt to add a packet to the bucket.
        
        :param packet_size: Size of the packet to be added
        :return: True if packet was added successfully, False otherwise
        """
        self.leak()
        if self.bucket + packet_size <= self.capacity:
            self.bucket += packet_size
            return True
        return False

    def get_fill_level(self) -> float:
        """Return the current fill level of the bucket as a percentage."""
        return (self.bucket / self.capacity) * 100

def simulate_traffic(bucket: LeakyBucket, packets: List[float], delay: float = 1.0) -> None:
    """
    Simulate traffic by adding packets to the bucket.
    
    :param bucket: LeakyBucket instance
    :param packets: List of packet sizes to add
    :param delay: Time delay between packet arrivals (in seconds)
    """
    for packet_size in packets:
        if bucket.add_packet(packet_size):
            print(f"Packet of size {packet_size} added successfully. Bucket fill: {bucket.get_fill_level():.2f}%")
        else:
            print(f"Packet of size {packet_size} dropped due to overflow. Bucket fill: {bucket.get_fill_level():.2f}%")
        time.sleep(delay)

def main():
    bucket_capacity = 5.0  # Maximum capacity of the bucket
    leak_rate = 1.0        # Leak rate (packets per second)
    bucket = LeakyBucket(bucket_capacity, leak_rate)

    # Simulate adding packets
    packets = [3.0, 4.0, 2.0, 1.0, 6.0]
    simulate_traffic(bucket, packets)

if __name__ == "__main__":
    main()
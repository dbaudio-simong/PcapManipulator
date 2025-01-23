"""Module to provide pcap manipulation functions"""
import os

from scapy.all import rdpcap, wrpcap

class PcapManipulator:
    """A simple class to manipulate pcap files
    """
    def __init__(self, input_file, output_file=None):

        self.input_file = input_file
        if output_file:
            self.output_file = output_file
        else:
            self.output_file = self._append_fail_to_filename()

        self.packets = rdpcap(self.input_file)
        self.remaining_packets = None

    def _append_fail_to_filename(self):
        base_name, file_extension = os.path.splitext(self.input_file)
        output_file = f"{base_name}_fail{file_extension}"

        return output_file

    def delete_packets(self, start_num, stop_num):
        """Deletes a range of packets from a pcap file

        Args:
            start_num (int): Number of first packet to be deleted.
            stop_num (int): Number of last packet to be deleted

        Raises:
            ValueError: Invalid range is provided
        """
        # Validate packet indices
        if (start_num < 1 or stop_num < 1 or start_num > len(self.packets) or 
            stop_num > len(self.packets)):
            raise ValueError(f"Invalid range: start_num={start_num}, stop_num={stop_num}, "
                             f"total packets={len(self.packets)}")
         # Adjust indices for 0-based indexing in Python
        start_index = start_num - 1
        stop_index = stop_num - 1

         # Keep packets outside the specified range
        self.remaining_packets = self.packets[:start_index] + self.packets[stop_index + 1:]
        print(f"Packets {start_num} to {stop_num} (inclusive) removed.")

    def get_packets(filename, start_num, stop_num):
        """Get a range of packets from a pcap file

        Args:
            filename (str): Name of the pcap file.
            start_num (int): Number of first packet to be retrieved.
            stop_num (int): Number of last packet to be retrieved.

        Returns:
            list: List of packets in the specified range.
        """
        packets = rdpcap(filename)
        return packets[start_num - 1:stop_num]

    def insert_packets(self, start_num, packets):
        """Inserts packets at a specified position in the pcap file

        Args:
            start_num (int): Position to insert packets at.
            packets (list): List of packets to be inserted.

        Raises:
            ValueError: Invalid start position is provided.
        """
        # Validate packet index
        if start_num < 1 or start_num > len(self.packets) + 1:
            raise ValueError(f"Invalid start position: start_num={start_num}, total packets={len(self.packets)}")

        # Adjust index for 0-based indexing in Python
        start_index = start_num - 1

        # Insert packets at the specified position
        self.remaining_packets = self.packets[:start_index] + packets + self.packets[start_index:]
        print(f"Inserted {len(packets)} packets at position {start_num}.")

    def write_pcap_file(self, overwrite=False):
        """Writes new pcap file, with optional overwrite control."""
        if not self.remaining_packets:
            print("No new pcap file to write. Aborting.")
            return

        # Check if the file already exists
        if os.path.exists(self.output_file):
            if not overwrite:
                print(f"File '{self.output_file}' already exists. Use overwrite=True to overwrite.")
                return
            print(f"File '{self.output_file}' already exists. Overwriting...")

        # Write the pcap file
        wrpcap(self.output_file, self.remaining_packets)
        print(f"New pcap file written to: {self.output_file}")

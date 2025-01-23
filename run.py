"""Example how to run the PcapManipulator class"""
from PcapManipulator import PcapManipulator

# Initialize operator
operator = PcapManipulator(input_file="file.pcapng")

# Delete a range of packets
operator.delete_packets(start_num=3,
                        stop_num=6)

# Write new file, which will be written to file_fail.pcap by default
# Can use overwrite=True parameter if existing file should be overwritten
operator.write_pcap_file()

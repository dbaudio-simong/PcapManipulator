"""Example how to run the PcapManipulator class"""
from PcapManipulator import PcapManipulator

# Initialize operator
operator = PcapManipulator(input_file="file.pcapng", output_file="output.pcapng")

# Delete a range of packets
operator.delete_packets(start_num=3,
                        stop_num=6)

# Insert packets from another file
packets = PcapManipulator.get_packets(filename="another_file.pcapng",
                                      start_num=1,
                                      stop_num=5)

operator.insert_packets(start_num=2, packets=packets)

# Write new file, which will be written to file_fail.pcap by default
# Can use overwrite=True parameter if existing file should be overwritten
operator.write_pcap_file()

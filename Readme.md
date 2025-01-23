# PcapManipulator

PcapManipulator is a Python class for manipulating pcap files.

## Installation

Clone this repository

## Usage

See the run.py file and adapt to your case.

```python
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
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
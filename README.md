# DROP - DROne Parser

This is a [fork](https://github.com/unhcfreg/DROP) of the DROne Parser that is additionally able to parse DATv3 files and output JSON files. The JSON files can be visualized using [Maraudrone's Map](https://github.com/dumbledrone/MaraudronesMap).

## Usage:
`DROP.py -j <DAT_FILE>`

## V3 Samples
Samples of DATv3 files can be downloaded [here](https://drive.proton.me/urls/0PTCBSCKS0#0PuBJtw1ocHY).

## Development
To further extend the capabilities of decoding V3 .DAT files additional message files can be added within the `V3Messages` directory. Therefor the `00example.py` file can be copied and modified.\
The available types are only implemented to support the Phantom 4 Advanced, if the same message type with another payload length is needed, you can include this into the parse function, as already done in `battery_info_1710.py`.

## Credits
Original Version by Devon Clark\


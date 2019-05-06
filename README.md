<!-- -*- encoding: utf-8 -*- -->

pymztinfo.py
============

Display header information of MZT file.

Usage
-----

```bat
python pymztinfo.py MZT_FILE
python pymztinfo.py --help
python pymztinfo.py --verison
```

or

```bat
pymztinfo.exe MZT_FILE
pymztinfo.exe --help
pymztinfo.exe --version
```

Testing environment
-------------------

* Windows 10 x64
* Python 2.7.16 32bit

Files
-----

* pymztinfo.py ... main script
* mkexe.bat ... make exe file, request py2exe
* setup.py ... py2exe config file

Sample
------

```sh
> pymztinfo.exe fillscrn.mzt
Input file : fillscrn.mzt
0x00     : File mode = 0x01 (Binary)
0x01-0x11: Filename  = FILLSCRN
0x12-0x13: File size    = 0x005B (91)
0x14-0x15: Load Address = 0x1200
0x16-0x17: Exec Address = 0x1200
0x18-0x3F: 00 00 00 00 00 00 00 00
           00 00 00 00 00 00 00 00
           00 00 00 00 00 00 00 00
           00 00 00 00 00 00 00 00
           00 00 00 00 00 00 00 00
0x40-0x43: Patch Disable
body length: 0x005B (91)
```

```sh
> pymztinfo.exe S-BASIC_1Z007B.MZT
Input file : S-BASIC_1Z007B.MZT
0x00     : File mode = 0x01 (Binary)
0x01-0x11: Filename  =  S-BASIC
0x12-0x13: File size    = 0x6C80 (27776)
0x14-0x15: Load Address = 0x1200
0x16-0x17: Exec Address = 0x7E0F
0x18-0x3F: 11 30 11 CD 09 00 CD 15
           00 00 00 00 00 00 00 00
           00 00 00 00 00 00 00 00
           00 00 00 00 00 00 00 00
           00 00 00 00 00 00 00 00
0x40-0x43: Patch Enable
Adrs=0x1221 , Size=0x0C (12) , Data (Hex)=ED F4 03 ED F4 04 ED F4 01 ED F4 02
body length: 0x6C80 (27776)
```

License
-------

pymztinfo.py : CC0 / Public Domain

Author
------

by mieki256

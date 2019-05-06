#!python
# -*- mode: python; Encoding: utf-8; coding: utf-8 -*-
# Last updated: <2019/05/01 00:19:33 +0900>
"""
 MZT file header dispaly.

Version:
1.0    first commit.

Author : mieki256
License : CC0 / Public Domain

* Windows10 x64 + Python 2.7.15 32bit
"""

import struct
import argparse
import sys


kana_list = u''
kana_list += u'日月火水木金土生年時分秒円￥￡⤓'
kana_list += u'　。「」、．ヲァィゥェォャュョッ'
kana_list += u'ーアイウエオカキクケコサシスセソ'
kana_list += u'タチツテトナニヌネノハヒフヘホマ'
kana_list += u'ミムメモヤユヨラリルレロワン゛゜'


def get_attr_kind(attr):
    if attr == 0x01:
        return "Binary"
    elif attr == 0x02:
        return "SP-5030 / Hu-BASIC"
    elif attr == 0x05:
        return "MZ-700 S-BASIC"
    elif attr == 0xc8:
        return "CMU-800 Data"
    return "Unknown"


def make_kana_dic():
    kana_dic = {}
    i = 0x70
    for c in list(kana_list):
        kana_dic[i] = c
        i += 1
    return kana_dic


def get_filename(fn, kana):
    if kana:
        kana_dic = make_kana_dic()
    else:
        kana_dic = {}

    indent = ' ' * 23
    newfn = ""
    fnlst = []
    asciicode = True

    for c in list(fn):
        if sys.version_info.major == 2:
            c = ord(c)
        if c == 0x0d:
            break
        fnlst.append(c)
        if 0x20 <= c and c <= 0x5d:
            newfn += chr(c)
        else:
            if kana and c in kana_dic:
                newfn += kana_dic[c]
            else:
                newfn += '?'
            asciicode = False
    if asciicode:
        return newfn
    hexfn = ""
    for c in fnlst:
        hexfn += "%02X " % c
    return "%s\n%s%s" % (newfn, indent, hexfn)


def dump_patch(s):
    b = list(s)
    i = 4
    while True:
        if i >= len(s):
            break
        adrs = ord(b[i + 1]) * 256 + ord(b[i])
        if adrs == 0x0ffff:
            break
        i += 2
        size = ord(b[i])
        i += 1
        bs = ""
        for j in range(size):
            v = ord(b[i])
            i += 1
            bs += "%02X " % v
        ss = "Adrs=0x%04X , " % adrs
        ss += "Size=0x%02X (%d) , " % (size, size)
        ss += "Data (Hex)=%s" % bs
        print(ss)


def dump_hex(s):
    ret = "0x18-0x3F: "
    for i, b in enumerate(list(s)):
        if sys.version_info.major == 2:
            b = ord(b)
        ret += "%02X " % b
        if i % 8 == 7 and i < 39:
            ret += "\n" + ' ' * 11
    return ret


def main():
    """Main."""

    # get command line oprion
    p = argparse.ArgumentParser()
    p.description = "MZT file header display."
    p.add_argument("--version", action='version', version="%(prog)s 1.0")
    p.add_argument("infile", metavar='INFILE', help=".mzt file")
    p.add_argument("--kana", default=False, action='store_true',
                   help="Japanese Kana enable")
    args = p.parse_args()
    infile = args.infile
    kana = args.kana

    # read binary file
    f = open(infile, "rb")
    buf = f.read()
    f.close()

    # MZT header
    head_tape = buf[:24]
    head_fd = buf[24:64]
    patch = buf[64:128]
    body = buf[128:]

    attr, fn, fsize, sadrs, eadrs = struct.unpack("<B17sHHH", head_tape)

    print("Input file : %s" % infile)
    print("0x00     : File mode = 0x%02X (%s)" % (attr, get_attr_kind(attr)))
    print("0x01-0x11: Filename  = %s" % get_filename(fn, kana))
    print("0x12-0x13: File size    = 0x%04X (%d)" % (fsize, fsize))
    print("0x14-0x15: Load Address = 0x%04X" % sadrs)
    print("0x16-0x17: Exec Address = 0x%04X" % eadrs)
    print(dump_hex(head_fd))

    # MZT patch
    if patch[:4] == "PAT:":
        print("0x40-0x43: Patch Enable")
        dump_patch(patch)
    else:
        print("0x40-0x43: Patch Disable")

    print("body length: 0x%04X (%d)" % (len(body), len(body)))


if __name__ == '__main__':
    main()

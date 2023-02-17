""" Font Data and Function Module
 -----------------------------------
| Copyright 2022 by Joel C. Alcarez |
| [joelalcarez1975@gmail.com]       |
|-----------------------------------|
|    We make absolutely no warranty |
| of any kind, expressed or implied |
|-----------------------------------|
|   Contact primary author          |
|   if you plan to use this         |
|   in a commercial product at      |
|   joelalcarez1975@gmail.com       |
 -----------------------------------
"""


from array import array

font8x8 = array('B',[8,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, #0x00
0x7e, 0x81, 0xa5, 0x81, 0xbd, 0x99, 0x81, 0x7e, #0x01
0x7e, 0xff, 0xdb, 0xff, 0xc3, 0xe7, 0xff, 0x7e, #0x02
0x6c, 0xfe, 0xfe, 0xfe, 0x7c, 0x38, 0x10, 0x00, #0x03
0x10, 0x38, 0x7c, 0xfe, 0x7c, 0x38, 0x10, 0x00, #0x04
0x38, 0x7c, 0x38, 0xfe, 0xfe, 0xd6, 0x10, 0x38, #0x05
0x10, 0x10, 0x38, 0x7c, 0xfe, 0x7c, 0x10, 0x38, #0x06
0x00, 0x00, 0x18, 0x3c, 0x3c, 0x18, 0x00, 0x00, #0x07
0xff, 0xff, 0xe7, 0xc3, 0xc3, 0xe7, 0xff, 0xff, #0x08
0x00, 0x3c, 0x66, 0x42, 0x42, 0x66, 0x3c, 0x00, #0x09
0xff, 0xc3, 0x99, 0xbd, 0xbd, 0x99, 0xc3, 0xff, #0x0a
0x0f, 0x07, 0x0f, 0x7d, 0xcc, 0xcc, 0xcc, 0x78, #0x0b
0x3c, 0x66, 0x66, 0x66, 0x3c, 0x18, 0x7e, 0x18, #0x0c
0x3f, 0x33, 0x3f, 0x30, 0x30, 0x70, 0xf0, 0xe0, #0x0d
0x7f, 0x63, 0x7f, 0x63, 0x63, 0x67, 0xe6, 0xc0, #0x0e
0x18, 0xdb, 0x3c, 0xe7, 0xe7, 0x3c, 0xdb, 0x18, #0x0f
0x80, 0xe0, 0xf8, 0xfe, 0xf8, 0xe0, 0x80, 0x00, #0x10
0x02, 0x0e, 0x3e, 0xfe, 0x3e, 0x0e, 0x02, 0x00, #0x11
0x18, 0x3c, 0x7e, 0x18, 0x18, 0x7e, 0x3c, 0x18, #0x12
0x66, 0x66, 0x66, 0x66, 0x66, 0x00, 0x66, 0x00, #0x13
0x7f, 0xdb, 0xdb, 0x7b, 0x1b, 0x1b, 0x1b, 0x00, #0x14
0x3e, 0x63, 0x38, 0x6c, 0x6c, 0x38, 0xcc, 0x78, #0x15
0x00, 0x00, 0x00, 0x00, 0x7e, 0x7e, 0x7e, 0x00, #0x16
0x18, 0x3c, 0x7e, 0x18, 0x7e, 0x3c, 0x18, 0xff, #0x17
0x18, 0x3c, 0x7e, 0x18, 0x18, 0x18, 0x18, 0x00, #0x18
0x18, 0x18, 0x18, 0x18, 0x7e, 0x3c, 0x18, 0x00, #0x19
0x00, 0x18, 0x0c, 0xfe, 0x0c, 0x18, 0x00, 0x00, #0x1a
0x00, 0x30, 0x60, 0xfe, 0x60, 0x30, 0x00, 0x00, #0x1b
0x00, 0x00, 0xc0, 0xc0, 0xc0, 0xfe, 0x00, 0x00, #0x1c
0x00, 0x24, 0x66, 0xff, 0x66, 0x24, 0x00, 0x00, #0x1d
0x00, 0x18, 0x3c, 0x7e, 0xff, 0xff, 0x00, 0x00, #0x1e
0x00, 0xff, 0xff, 0x7e, 0x3c, 0x18, 0x00, 0x00, #0x1f
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, #0x20
0x30, 0x78, 0x78, 0x30, 0x30, 0x00, 0x30, 0x00, #0x21
0x6c, 0x6c, 0x6c, 0x00, 0x00, 0x00, 0x00, 0x00, #0x22
0x6c, 0x6c, 0xfe, 0x6c, 0xfe, 0x6c, 0x6c, 0x00, #0x23
0x30, 0x7c, 0xc0, 0x78, 0x0c, 0xf8, 0x30, 0x00, #0x24
0x00, 0xc6, 0xcc, 0x18, 0x30, 0x66, 0xc6, 0x00, #0x25
0x38, 0x6c, 0x38, 0x76, 0xdc, 0xcc, 0x76, 0x00, #0x26
0x60, 0x60, 0xc0, 0x00, 0x00, 0x00, 0x00, 0x00, #0x27
0x18, 0x30, 0x60, 0x60, 0x60, 0x30, 0x18, 0x00, #0x28
0x60, 0x30, 0x18, 0x18, 0x18, 0x30, 0x60, 0x00, #0x29
0x00, 0x66, 0x3c, 0xff, 0x3c, 0x66, 0x00, 0x00, #0x2a
0x00, 0x30, 0x30, 0xfc, 0x30, 0x30, 0x00, 0x00, #0x2b
0x00, 0x00, 0x00, 0x00, 0x00, 0x30, 0x30, 0x60, #0x2c
0x00, 0x00, 0x00, 0xfc, 0x00, 0x00, 0x00, 0x00, #0x2d
0x00, 0x00, 0x00, 0x00, 0x00, 0x30, 0x30, 0x00, #0x2e
0x06, 0x0c, 0x18, 0x30, 0x60, 0xc0, 0x80, 0x00, #0x2f
0x7c, 0xc6, 0xce, 0xde, 0xf6, 0xe6, 0x7c, 0x00, #0x30
0x30, 0x70, 0x30, 0x30, 0x30, 0x30, 0xfc, 0x00, #0x31
0x78, 0xcc, 0x0c, 0x38, 0x60, 0xcc, 0xfc, 0x00, #0x32
0x78, 0xcc, 0x0c, 0x38, 0x0c, 0xcc, 0x78, 0x00, #0x33
0x1c, 0x3c, 0x6c, 0xcc, 0xfe, 0x0c, 0x1e, 0x00, #0x34
0xfc, 0xc0, 0xf8, 0x0c, 0x0c, 0xcc, 0x78, 0x00, #0x35
0x38, 0x60, 0xc0, 0xf8, 0xcc, 0xcc, 0x78, 0x00, #0x36
0xfc, 0xcc, 0x0c, 0x18, 0x30, 0x30, 0x30, 0x00, #0x37
0x78, 0xcc, 0xcc, 0x78, 0xcc, 0xcc, 0x78, 0x00, #0x38
0x78, 0xcc, 0xcc, 0x7c, 0x0c, 0x18, 0x70, 0x00, #0x39
0x00, 0x30, 0x30, 0x00, 0x00, 0x30, 0x30, 0x00, #0x3a
0x00, 0x30, 0x30, 0x00, 0x00, 0x30, 0x30, 0x60, #0x3b
0x18, 0x30, 0x60, 0xc0, 0x60, 0x30, 0x18, 0x00, #0x3c
0x00, 0x00, 0xfc, 0x00, 0x00, 0xfc, 0x00, 0x00, #0x3d
0x60, 0x30, 0x18, 0x0c, 0x18, 0x30, 0x60, 0x00, #0x3e
0x78, 0xcc, 0x0c, 0x18, 0x30, 0x00, 0x30, 0x00, #0x3f
0x7c, 0xc6, 0xde, 0xde, 0xde, 0xc0, 0x78, 0x00, #0x40
0x30, 0x78, 0xcc, 0xcc, 0xfc, 0xcc, 0xcc, 0x00, #0x41
0xfc, 0x66, 0x66, 0x7c, 0x66, 0x66, 0xfc, 0x00, #0x42
0x3c, 0x66, 0xc0, 0xc0, 0xc0, 0x66, 0x3c, 0x00, #0x43
0xf8, 0x6c, 0x66, 0x66, 0x66, 0x6c, 0xf8, 0x00, #0x44
0xfe, 0x62, 0x68, 0x78, 0x68, 0x62, 0xfe, 0x00, #0x45
0xfe, 0x62, 0x68, 0x78, 0x68, 0x60, 0xf0, 0x00, #0x46
0x3c, 0x66, 0xc0, 0xc0, 0xce, 0x66, 0x3e, 0x00, #0x47
0xcc, 0xcc, 0xcc, 0xfc, 0xcc, 0xcc, 0xcc, 0x00, #0x48
0x78, 0x30, 0x30, 0x30, 0x30, 0x30, 0x78, 0x00, #0x49
0x1e, 0x0c, 0x0c, 0x0c, 0xcc, 0xcc, 0x78, 0x00, #0x4a
0xe6, 0x66, 0x6c, 0x78, 0x6c, 0x66, 0xe6, 0x00, #0x4b
0xf0, 0x60, 0x60, 0x60, 0x62, 0x66, 0xfe, 0x00, #0x4c
0xc6, 0xee, 0xfe, 0xfe, 0xd6, 0xc6, 0xc6, 0x00, #0x4d
0xc6, 0xe6, 0xf6, 0xde, 0xce, 0xc6, 0xc6, 0x00, #0x4e
0x38, 0x6c, 0xc6, 0xc6, 0xc6, 0x6c, 0x38, 0x00, #0x4f
0xfc, 0x66, 0x66, 0x7c, 0x60, 0x60, 0xf0, 0x00, #0x50
0x78, 0xcc, 0xcc, 0xcc, 0xdc, 0x78, 0x1c, 0x00, #0x51
0xfc, 0x66, 0x66, 0x7c, 0x6c, 0x66, 0xe6, 0x00, #0x52
0x78, 0xcc, 0x60, 0x30, 0x18, 0xcc, 0x78, 0x00, #0x53
0xfc, 0xb4, 0x30, 0x30, 0x30, 0x30, 0x78, 0x00, #0x54
0xcc, 0xcc, 0xcc, 0xcc, 0xcc, 0xcc, 0xfc, 0x00, #0x55
0xcc, 0xcc, 0xcc, 0xcc, 0xcc, 0x78, 0x30, 0x00, #0x56
0xc6, 0xc6, 0xc6, 0xd6, 0xfe, 0xee, 0xc6, 0x00, #0x57
0xc6, 0xc6, 0x6c, 0x38, 0x38, 0x6c, 0xc6, 0x00, #0x58
0xcc, 0xcc, 0xcc, 0x78, 0x30, 0x30, 0x78, 0x00, #0x59
0xfe, 0xc6, 0x8c, 0x18, 0x32, 0x66, 0xfe, 0x00, #0x5a
0x78, 0x60, 0x60, 0x60, 0x60, 0x60, 0x78, 0x00, #0x5b
0xc0, 0x60, 0x30, 0x18, 0x0c, 0x06, 0x02, 0x00, #0x5c
0x78, 0x18, 0x18, 0x18, 0x18, 0x18, 0x78, 0x00, #0x5d
0x10, 0x38, 0x6c, 0xc6, 0x00, 0x00, 0x00, 0x00, #0x5e
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff, #0x5f
0x30, 0x30, 0x18, 0x00, 0x00, 0x00, 0x00, 0x00, #0x60
0x00, 0x00, 0x78, 0x0c, 0x7c, 0xcc, 0x76, 0x00, #0x61
0xe0, 0x60, 0x60, 0x7c, 0x66, 0x66, 0xdc, 0x00, #0x62
0x00, 0x00, 0x78, 0xcc, 0xc0, 0xcc, 0x78, 0x00, #0x63
0x1c, 0x0c, 0x0c, 0x7c, 0xcc, 0xcc, 0x76, 0x00, #0x64
0x00, 0x00, 0x78, 0xcc, 0xfc, 0xc0, 0x78, 0x00, #0x65
0x38, 0x6c, 0x60, 0xf0, 0x60, 0x60, 0xf0, 0x00, #0x66
0x00, 0x00, 0x76, 0xcc, 0xcc, 0x7c, 0x0c, 0xf8, #0x67
0xe0, 0x60, 0x6c, 0x76, 0x66, 0x66, 0xe6, 0x00, #0x68
0x30, 0x00, 0x70, 0x30, 0x30, 0x30, 0x78, 0x00, #0x69
0x0c, 0x00, 0x0c, 0x0c, 0x0c, 0xcc, 0xcc, 0x78, #0x6a
0xe0, 0x60, 0x66, 0x6c, 0x78, 0x6c, 0xe6, 0x00, #0x6b
0x70, 0x30, 0x30, 0x30, 0x30, 0x30, 0x78, 0x00, #0x6c
0x00, 0x00, 0xcc, 0xfe, 0xfe, 0xd6, 0xc6, 0x00, #0x6d
0x00, 0x00, 0xf8, 0xcc, 0xcc, 0xcc, 0xcc, 0x00, #0x6e
0x00, 0x00, 0x78, 0xcc, 0xcc, 0xcc, 0x78, 0x00, #0x6f
0x00, 0x00, 0xdc, 0x66, 0x66, 0x7c, 0x60, 0xf0, #0x70
0x00, 0x00, 0x76, 0xcc, 0xcc, 0x7c, 0x0c, 0x1e, #0x71
0x00, 0x00, 0xdc, 0x76, 0x66, 0x60, 0xf0, 0x00, #0x72
0x00, 0x00, 0x7c, 0xc0, 0x78, 0x0c, 0xf8, 0x00, #0x73
0x10, 0x30, 0x7c, 0x30, 0x30, 0x34, 0x18, 0x00, #0x74
0x00, 0x00, 0xcc, 0xcc, 0xcc, 0xcc, 0x76, 0x00, #0x75
0x00, 0x00, 0xcc, 0xcc, 0xcc, 0x78, 0x30, 0x00, #0x76
0x00, 0x00, 0xc6, 0xd6, 0xfe, 0xfe, 0x6c, 0x00, #0x77
0x00, 0x00, 0xc6, 0x6c, 0x38, 0x6c, 0xc6, 0x00, #0x78
0x00, 0x00, 0xcc, 0xcc, 0xcc, 0x7c, 0x0c, 0xf8, #0x79
0x00, 0x00, 0xfc, 0x98, 0x30, 0x64, 0xfc, 0x00, #0x7a
0x1c, 0x30, 0x30, 0xe0, 0x30, 0x30, 0x1c, 0x00, #0x7b
0x18, 0x18, 0x18, 0x00, 0x18, 0x18, 0x18, 0x00, #0x7c
0xe0, 0x30, 0x30, 0x1c, 0x30, 0x30, 0xe0, 0x00, #0x7d
0x76, 0xdc, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, #0x7e
0x00, 0x10, 0x38, 0x6c, 0xc6, 0xc6, 0xfe, 0x00, #0x7f
0x78, 0xcc, 0xc0, 0xcc, 0x78, 0x18, 0x0c, 0x78, #0x80
0x00, 0xcc, 0x00, 0xcc, 0xcc, 0xcc, 0x7e, 0x00, #0x81
0x1c, 0x00, 0x78, 0xcc, 0xfc, 0xc0, 0x78, 0x00, #0x82
0x7e, 0xc3, 0x3c, 0x06, 0x3e, 0x66, 0x3f, 0x00, #0x83
0xcc, 0x00, 0x78, 0x0c, 0x7c, 0xcc, 0x7e, 0x00, #0x84
0xe0, 0x00, 0x78, 0x0c, 0x7c, 0xcc, 0x7e, 0x00, #0x85
0x30, 0x30, 0x78, 0x0c, 0x7c, 0xcc, 0x7e, 0x00, #0x86
0x00, 0x00, 0x78, 0xc0, 0xc0, 0x78, 0x0c, 0x38, #0x87
0x7e, 0xc3, 0x3c, 0x66, 0x7e, 0x60, 0x3c, 0x00, #0x88
0xcc, 0x00, 0x78, 0xcc, 0xfc, 0xc0, 0x78, 0x00, #0x89
0xe0, 0x00, 0x78, 0xcc, 0xfc, 0xc0, 0x78, 0x00, #0x8a
0xcc, 0x00, 0x70, 0x30, 0x30, 0x30, 0x78, 0x00, #0x8b
0x7c, 0xc6, 0x38, 0x18, 0x18, 0x18, 0x3c, 0x00, #0x8c
0xe0, 0x00, 0x70, 0x30, 0x30, 0x30, 0x78, 0x00, #0x8d
0xc6, 0x38, 0x6c, 0xc6, 0xfe, 0xc6, 0xc6, 0x00, #0x8e
0x30, 0x30, 0x00, 0x78, 0xcc, 0xfc, 0xcc, 0x00, #0x8f
0x1c, 0x00, 0xfc, 0x60, 0x78, 0x60, 0xfc, 0x00, #0x90
0x00, 0x00, 0x7f, 0x0c, 0x7f, 0xcc, 0x7f, 0x00, #0x91
0x3e, 0x6c, 0xcc, 0xfe, 0xcc, 0xcc, 0xce, 0x00, #0x92
0x78, 0xcc, 0x00, 0x78, 0xcc, 0xcc, 0x78, 0x00, #0x93
0x00, 0xcc, 0x00, 0x78, 0xcc, 0xcc, 0x78, 0x00, #0x94
0x00, 0xe0, 0x00, 0x78, 0xcc, 0xcc, 0x78, 0x00, #0x95
0x78, 0xcc, 0x00, 0xcc, 0xcc, 0xcc, 0x7e, 0x00, #0x96
0x00, 0xe0, 0x00, 0xcc, 0xcc, 0xcc, 0x7e, 0x00, #0x97
0x00, 0xcc, 0x00, 0xcc, 0xcc, 0x7c, 0x0c, 0xf8, #0x98
0xc3, 0x18, 0x3c, 0x66, 0x66, 0x3c, 0x18, 0x00, #0x99
0xcc, 0x00, 0xcc, 0xcc, 0xcc, 0xcc, 0x78, 0x00, #0x9a
0x18, 0x18, 0x7e, 0xc0, 0xc0, 0x7e, 0x18, 0x18, #0x9b
0x38, 0x6c, 0x64, 0xf0, 0x60, 0xe6, 0xfc, 0x00, #0x9c
0xcc, 0xcc, 0x78, 0xfc, 0x30, 0xfc, 0x30, 0x30, #0x9d
0xf8, 0xcc, 0xcc, 0xfa, 0xc6, 0xcf, 0xc6, 0xc7, #0x9e
0x0e, 0x1b, 0x18, 0x3c, 0x18, 0x18, 0xd8, 0x70, #0x9f
0x1c, 0x00, 0x78, 0x0c, 0x7c, 0xcc, 0x7e, 0x00, #0xa0
0x38, 0x00, 0x70, 0x30, 0x30, 0x30, 0x78, 0x00, #0xa1
0x00, 0x1c, 0x00, 0x78, 0xcc, 0xcc, 0x78, 0x00, #0xa2
0x00, 0x1c, 0x00, 0xcc, 0xcc, 0xcc, 0x7e, 0x00, #0xa3
0x00, 0xf8, 0x00, 0xf8, 0xcc, 0xcc, 0xcc, 0x00, #0xa4
0xfc, 0x00, 0xcc, 0xec, 0xfc, 0xdc, 0xcc, 0x00, #0xa5
0x3c, 0x6c, 0x6c, 0x3e, 0x00, 0x7e, 0x00, 0x00, #0xa6
0x38, 0x6c, 0x6c, 0x38, 0x00, 0x7c, 0x00, 0x00, #0xa7
0x30, 0x00, 0x30, 0x60, 0xc0, 0xcc, 0x78, 0x00, #0xa8
0x00, 0x00, 0x00, 0xfc, 0xc0, 0xc0, 0x00, 0x00, #0xa9
0x00, 0x00, 0x00, 0xfc, 0x0c, 0x0c, 0x00, 0x00, #0xaa
0xc3, 0xc6, 0xcc, 0xde, 0x33, 0x66, 0xcc, 0x0f, #0xab
0xc3, 0xc6, 0xcc, 0xdb, 0x37, 0x6f, 0xcf, 0x03, #0xac
0x18, 0x18, 0x00, 0x18, 0x18, 0x18, 0x18, 0x00, #0xad
0x00, 0x33, 0x66, 0xcc, 0x66, 0x33, 0x00, 0x00, #0xae
0x00, 0xcc, 0x66, 0x33, 0x66, 0xcc, 0x00, 0x00, #0xaf
0x22, 0x88, 0x22, 0x88, 0x22, 0x88, 0x22, 0x88, #0xb0
0x55, 0xaa, 0x55, 0xaa, 0x55, 0xaa, 0x55, 0xaa, #0xb1
0xdb, 0x77, 0xdb, 0xee, 0xdb, 0x77, 0xdb, 0xee, #0xb2
0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18, #0xb3
0x18, 0x18, 0x18, 0x18, 0xf8, 0x18, 0x18, 0x18, #0xb4
0x18, 0x18, 0xf8, 0x18, 0xf8, 0x18, 0x18, 0x18, #0xb5
0x36, 0x36, 0x36, 0x36, 0xf6, 0x36, 0x36, 0x36, #0xb6
0x00, 0x00, 0x00, 0x00, 0xfe, 0x36, 0x36, 0x36, #0xb7
0x00, 0x00, 0xf8, 0x18, 0xf8, 0x18, 0x18, 0x18, #0xb8
0x36, 0x36, 0xf6, 0x06, 0xf6, 0x36, 0x36, 0x36, #0xb9
0x36, 0x36, 0x36, 0x36, 0x36, 0x36, 0x36, 0x36, #0xba
0x00, 0x00, 0xfe, 0x06, 0xf6, 0x36, 0x36, 0x36, #0xbb
0x36, 0x36, 0xf6, 0x06, 0xfe, 0x00, 0x00, 0x00, #0xbc
0x36, 0x36, 0x36, 0x36, 0xfe, 0x00, 0x00, 0x00, #0xbd
0x18, 0x18, 0xf8, 0x18, 0xf8, 0x00, 0x00, 0x00, #0xbe
0x00, 0x00, 0x00, 0x00, 0xf8, 0x18, 0x18, 0x18, #0xbf
0x18, 0x18, 0x18, 0x18, 0x1f, 0x00, 0x00, 0x00, #0xc0
0x18, 0x18, 0x18, 0x18, 0xff, 0x00, 0x00, 0x00, #0xc1
0x00, 0x00, 0x00, 0x00, 0xff, 0x18, 0x18, 0x18, #0xc2
0x18, 0x18, 0x18, 0x18, 0x1f, 0x18, 0x18, 0x18, #0xc3
0x00, 0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, #0xc4
0x18, 0x18, 0x18, 0x18, 0xff, 0x18, 0x18, 0x18, #0xc5
0x18, 0x18, 0x1f, 0x18, 0x1f, 0x18, 0x18, 0x18, #0xc6
0x36, 0x36, 0x36, 0x36, 0x37, 0x36, 0x36, 0x36, #0xc7
0x36, 0x36, 0x37, 0x30, 0x3f, 0x00, 0x00, 0x00, #0xc8
0x00, 0x00, 0x3f, 0x30, 0x37, 0x36, 0x36, 0x36, #0xc9
0x36, 0x36, 0xf7, 0x00, 0xff, 0x00, 0x00, 0x00, #0xca
0x00, 0x00, 0xff, 0x00, 0xf7, 0x36, 0x36, 0x36, #0xcb
0x36, 0x36, 0x37, 0x30, 0x37, 0x36, 0x36, 0x36, #0xcc
0x00, 0x00, 0xff, 0x00, 0xff, 0x00, 0x00, 0x00, #0xcd
0x36, 0x36, 0xf7, 0x00, 0xf7, 0x36, 0x36, 0x36, #0xce
0x18, 0x18, 0xff, 0x00, 0xff, 0x00, 0x00, 0x00, #0xcf
0x36, 0x36, 0x36, 0x36, 0xff, 0x00, 0x00, 0x00, #0xd0
0x00, 0x00, 0xff, 0x00, 0xff, 0x18, 0x18, 0x18, #0xd1
0x00, 0x00, 0x00, 0x00, 0xff, 0x36, 0x36, 0x36, #0xd2
0x36, 0x36, 0x36, 0x36, 0x3f, 0x00, 0x00, 0x00, #0xd3
0x18, 0x18, 0x1f, 0x18, 0x1f, 0x00, 0x00, 0x00, #0xd4
0x00, 0x00, 0x1f, 0x18, 0x1f, 0x18, 0x18, 0x18, #0xd5
0x00, 0x00, 0x00, 0x00, 0x3f, 0x36, 0x36, 0x36, #0xd6
0x36, 0x36, 0x36, 0x36, 0xff, 0x36, 0x36, 0x36, #0xd7
0x18, 0x18, 0xff, 0x18, 0xff, 0x18, 0x18, 0x18, #0xd8
0x18, 0x18, 0x18, 0x18, 0xf8, 0x00, 0x00, 0x00, #0xd9
0x00, 0x00, 0x00, 0x00, 0x1f, 0x18, 0x18, 0x18, #0xda
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, #0xdb
0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff, #0xdc
0xf0, 0xf0, 0xf0, 0xf0, 0xf0, 0xf0, 0xf0, 0xf0, #0xdd
0x0f, 0x0f, 0x0f, 0x0f, 0x0f, 0x0f, 0x0f, 0x0f, #0xde
0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00, #0xdf
0x00, 0x00, 0x76, 0xdc, 0xc8, 0xdc, 0x76, 0x00, #0xe0
0x00, 0x78, 0xcc, 0xf8, 0xcc, 0xf8, 0xc0, 0xc0, #0xe1
0x00, 0xfc, 0xcc, 0xc0, 0xc0, 0xc0, 0xc0, 0x00, #0xe2
0x00, 0xfe, 0x6c, 0x6c, 0x6c, 0x6c, 0x6c, 0x00, #0xe3
0xfc, 0xcc, 0x60, 0x30, 0x60, 0xcc, 0xfc, 0x00, #0xe4
0x00, 0x00, 0x7e, 0xd8, 0xd8, 0xd8, 0x70, 0x00, #0xe5
0x00, 0x66, 0x66, 0x66, 0x66, 0x7c, 0x60, 0xc0, #0xe6
0x00, 0x76, 0xdc, 0x18, 0x18, 0x18, 0x18, 0x00, #0xe7
0xfc, 0x30, 0x78, 0xcc, 0xcc, 0x78, 0x30, 0xfc, #0xe8
0x38, 0x6c, 0xc6, 0xfe, 0xc6, 0x6c, 0x38, 0x00, #0xe9
0x38, 0x6c, 0xc6, 0xc6, 0x6c, 0x6c, 0xee, 0x00, #0xea
0x1c, 0x30, 0x18, 0x7c, 0xcc, 0xcc, 0x78, 0x00, #0xeb
0x00, 0x00, 0x7e, 0xdb, 0xdb, 0x7e, 0x00, 0x00, #0xec
0x06, 0x0c, 0x7e, 0xdb, 0xdb, 0x7e, 0x60, 0xc0, #0xed
0x38, 0x60, 0xc0, 0xf8, 0xc0, 0x60, 0x38, 0x00, #0xee
0x78, 0xcc, 0xcc, 0xcc, 0xcc, 0xcc, 0xcc, 0x00, #0xef
0x00, 0xfc, 0x00, 0xfc, 0x00, 0xfc, 0x00, 0x00, #0xf0
0x30, 0x30, 0xfc, 0x30, 0x30, 0x00, 0xfc, 0x00, #0xf1
0x60, 0x30, 0x18, 0x30, 0x60, 0x00, 0xfc, 0x00, #0xf2
0x18, 0x30, 0x60, 0x30, 0x18, 0x00, 0xfc, 0x00, #0xf3
0x0e, 0x1b, 0x1b, 0x18, 0x18, 0x18, 0x18, 0x18, #0xf4
0x18, 0x18, 0x18, 0x18, 0x18, 0xd8, 0xd8, 0x70, #0xf5
0x30, 0x30, 0x00, 0xfc, 0x00, 0x30, 0x30, 0x00, #0xf6
0x00, 0x76, 0xdc, 0x00, 0x76, 0xdc, 0x00, 0x00, #0xf7
0x38, 0x6c, 0x6c, 0x38, 0x00, 0x00, 0x00, 0x00, #0xf8
0x00, 0x00, 0x00, 0x18, 0x18, 0x00, 0x00, 0x00, #0xf9
0x00, 0x00, 0x00, 0x00, 0x18, 0x00, 0x00, 0x00, #0xfa
0x0f, 0x0c, 0x0c, 0x0c, 0xec, 0x6c, 0x3c, 0x1c, #0xfb
0x78, 0x6c, 0x6c, 0x6c, 0x6c, 0x00, 0x00, 0x00, #0xfc
0x70, 0x18, 0x30, 0x60, 0x78, 0x00, 0x00, 0x00, #0xfd
0x00, 0x00, 0x3c, 0x3c, 0x3c, 0x3c, 0x00, 0x00, #0xfe
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])#0xff

font8x14 = array('B',[14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 24, 24, 24, 24, 24, 0, 0, 24, 0, 0, 0, 0, 102, 102, 102, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 108, 108, 254, 108, 108, 108, 254, 108, 108, 0, 0, 0, 0, 16, 124, 214, 208, 208, 124, 22, 22, 214, 124, 16, 0, 0, 0, 0, 0, 0, 194, 196, 8, 16, 32, 70, 134, 0, 0, 0, 0, 0, 56, 108, 108, 56, 118, 220, 204, 204, 118, 0, 0, 0, 0, 48, 48, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 24, 48, 48, 48, 48, 48, 24, 12, 0, 0, 0, 0, 0, 48, 24, 12, 12, 12, 12, 12, 24, 48, 0, 0, 0, 0, 0, 0, 0, 102, 60, 255, 60, 102, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 24, 126, 24, 24, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 28, 24, 48, 0, 0, 0, 0, 0, 0, 0, 0, 252, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 24, 0, 0, 0, 0, 0, 2, 6, 12, 24, 48, 96, 192, 128, 0, 0, 0, 0, 0, 0, 124, 198, 198, 198, 214, 198, 198, 198, 124, 0, 0, 0, 0, 0, 24, 56, 24, 24, 24, 24, 24, 24, 126, 0, 0, 0, 0, 0, 124, 198, 6, 12, 24, 48, 96, 192, 254, 0, 0, 0, 0, 0, 124, 198, 6, 6, 60, 6, 6, 198, 124, 0, 0, 0, 0, 0, 12, 28, 60, 108, 204, 254, 12, 12, 12, 0, 0, 0, 0, 0, 254, 192, 192, 192, 252, 6, 6, 198, 124, 0, 0, 0, 0, 0, 60, 96, 192, 192, 252, 198, 198, 198, 126, 0, 0, 0, 0, 0, 254, 6, 6, 12, 24, 48, 48, 48, 48, 0, 0, 0, 0, 0, 124, 198, 198, 198, 124, 198, 198, 198, 124, 0, 0, 0, 0, 0, 124, 198, 198, 198, 126, 6, 6, 12, 120, 0, 0, 0, 0, 0, 0, 24, 24, 0, 0, 0, 24, 24, 0, 0, 0, 0, 0, 0, 0, 24, 24, 0, 0, 0, 24, 24, 48, 0, 0, 0, 0, 0, 6, 12, 24, 48, 96, 48, 24, 12, 6, 0, 0, 0, 0, 0, 0, 0, 0, 126, 0, 0, 126, 0, 0, 0, 0, 0, 0, 0, 96, 48, 24, 12, 6, 12, 24, 48, 96, 0, 0, 0, 0, 0, 124, 198, 6, 12, 24, 24, 24, 0, 0, 24, 0, 0, 0, 0, 124, 198, 198, 198, 222, 222, 222, 192, 124, 0, 0, 0, 0, 0, 16, 56, 108, 198, 198, 254, 198, 198, 198, 0, 0, 0, 0, 0, 252, 198, 198, 198, 252, 198, 198, 198, 252, 0, 0, 0, 0, 0, 60, 102, 192, 192, 192, 192, 192, 102, 60, 0, 0, 0, 0, 0, 248, 204, 198, 198, 198, 198, 198, 204, 248, 0, 0, 0, 0, 0, 254, 192, 192, 192, 252, 192, 192, 192, 254, 0, 0, 0, 0, 0, 254, 192, 192, 192, 252, 192, 192, 192, 192, 0, 0, 0, 0, 0, 60, 102, 192, 192, 192, 206, 198, 102, 60, 0, 0, 0, 0, 0, 198, 198, 198, 198, 254, 198, 198, 198, 198, 0, 0, 0, 0, 0, 60, 24, 24, 24, 24, 24, 24, 24, 60, 0, 0, 0, 0, 0, 30, 12, 12, 12, 12, 12, 12, 12, 120, 0, 0, 0, 0, 0, 198, 204, 216, 240, 224, 240, 216, 204, 198, 0, 0, 0, 0, 0, 192, 192, 192, 192, 192, 192, 192, 192, 254, 0, 0, 0, 0, 0, 198, 238, 254, 254, 214, 198, 198, 198, 198, 0, 0, 0, 0, 0, 198, 230, 246, 254, 222, 206, 198, 198, 198, 0, 0, 0, 0, 0, 124, 198, 198, 198, 198, 198, 198, 198, 124, 0, 0, 0, 0, 0, 252, 198, 198, 198, 252, 192, 192, 192, 192, 0, 0, 0, 0, 0, 124, 198, 198, 198, 198, 198, 214, 204, 122, 0, 0, 0, 0, 0, 252, 198, 198, 198, 252, 216, 204, 198, 198, 0, 0, 0, 0, 0, 124, 198, 192, 96, 56, 12, 6, 198, 124, 0, 0, 0, 0, 0, 126, 24, 24, 24, 24, 24, 24, 24, 24, 0, 0, 0, 0, 0, 198, 198, 198, 198, 198, 198, 198, 198, 124, 0, 0, 0, 0, 0, 198, 198, 198, 198, 198, 198, 108, 56, 16, 0, 0, 0, 0, 0, 198, 198, 198, 198, 214, 214, 254, 238, 198, 0, 0, 0, 0, 0, 198, 198, 108, 56, 16, 56, 108, 198, 198, 0, 0, 0, 0, 0, 102, 102, 102, 102, 60, 24, 24, 24, 24, 0, 0, 0, 0, 0, 254, 6, 12, 24, 48, 96, 192, 192, 254, 0, 0, 0, 0, 0, 60, 48, 48, 48, 48, 48, 48, 48, 60, 0, 0, 0, 0, 0, 0, 128, 192, 96, 48, 24, 12, 6, 2, 0, 0, 0, 0, 0, 60, 12, 12, 12, 12, 12, 12, 12, 60, 0, 0, 0, 16, 56, 108, 198, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 254, 0, 48, 48, 24, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 124, 6, 126, 198, 198, 126, 0, 0, 0, 0, 0, 192, 192, 192, 252, 198, 198, 198, 198, 252, 0, 0, 0, 0, 0, 0, 0, 0, 124, 198, 192, 192, 198, 124, 0, 0, 0, 0, 0, 6, 6, 6, 126, 198, 198, 198, 198, 126, 0, 0, 0, 0, 0, 0, 0, 0, 124, 198, 254, 192, 198, 124, 0, 0, 0, 0, 0, 60, 102, 96, 96, 240, 96, 96, 96, 96, 0, 0, 0, 0, 0, 0, 0, 0, 126, 198, 198, 198, 126, 6, 6, 6, 124, 0, 0, 192, 192, 192, 252, 198, 198, 198, 198, 198, 0, 0, 0, 0, 0, 24, 24, 0, 0, 24, 24, 24, 24, 24, 0, 0, 0, 0, 0, 6, 6, 0, 0, 6, 6, 6, 6, 6, 6, 198, 124, 0, 0, 192, 192, 192, 204, 216, 240, 216, 204, 198, 0, 0, 0, 0, 0, 56, 24, 24, 24, 24, 24, 24, 24, 60, 0, 0, 0, 0, 0, 0, 0, 0, 236, 214, 214, 214, 214, 198, 0, 0, 0, 0, 0, 0, 0, 0, 252, 198, 198, 198, 198, 198, 0, 0, 0, 0, 0, 0, 0, 0, 124, 198, 198, 198, 198, 124, 0, 0, 0, 0, 0, 0, 0, 0, 252, 198, 198, 198, 198, 252, 192, 192, 192, 0, 0, 0, 0, 0, 126, 198, 198, 198, 198, 126, 6, 6, 6, 0, 0, 0, 0, 0, 252, 198, 192, 192, 192, 192, 0, 0, 0, 0, 0, 0, 0, 0, 124, 192, 112, 28, 6, 124, 0, 0, 0, 0, 0, 48, 48, 252, 48, 48, 48, 48, 48, 28, 0, 0, 0, 0, 0, 0, 0, 0, 198, 198, 198, 198, 198, 124, 0, 0, 0, 0, 0, 0, 0, 0, 198, 198, 198, 108, 56, 16, 0, 0, 0, 0, 0, 0, 0, 0, 198, 198, 214, 214, 254, 198, 0, 0, 0, 0, 0, 0, 0, 0, 198, 108, 56, 56, 108, 198, 0, 0, 0, 0, 0, 0, 0, 0, 198, 198, 198, 198, 198, 126, 6, 6, 124, 0, 0, 0, 0, 0, 254, 12, 24, 48, 96, 254, 0, 0, 0, 0, 0, 14, 24, 24, 24, 96, 24, 24, 24, 14, 0, 0, 0, 0, 0, 24, 24, 24, 24, 0, 24, 24, 24, 24, 0, 0, 0, 0, 0, 112, 24, 24, 24, 6, 24, 24, 24, 112, 0, 0, 0, 118, 220, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


def itergetcharfromfontbuf(
        charbuf: list,
        character: str) -> int:
    l = charbuf[0]
    start = ord(character) * l + 1
    end = start + l
    for i in range(start, end):
        yield charbuf[i]


def getcharfont(
        charbuf: list,
        character: str) -> list:
    return list(itergetcharfromfontbuf(charbuf, character))

# print(charbuf)
# print(getcharfont(charbuf,'A'))

dump = {}

# B next input

dump["B+"] = '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 3 FF FF FF FF FF FF FF FF FF FF 0 3 F8 0 7F E0 0 7F 0 3 FC 0 1F E0 0 FF 0 7 FC 0 F E0 0 3F FF FF FC 0 1F FF FF FF 0 F FF FF FF E0 0 3F FF FF FC 0 F FF FF FF 0 1 FF FF FF E0 0 7F FF FF FC 0 1F FF FF FF 0 1 FC 0 1F FF FF FF 0 3 FF FF FF E0 0 7F FF FF FC 0 1F E0 0 7F 0 3 FC 0 F E0 0 7F FF FF FC 0 F E0 0 3F 80 1 FC 0 7 FF FF FF 80 3 FF FF FF E0 0 1F FF FF FC 0 F FF FF FF 80 3'

# B previous input

dump["B-"] = '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 3 FF FF FF FF FF FF FF FF FF FF 0 3 FC 0 F E0 0 3F 0 3 FC 0 F E0 0 7F 0 3 FC 0 1F E0 0 7F FF FF FC 0 F FF FF FF 80 1 FF FF FF E0 0 7F FF FF FC 0 F FF FF FF 80 1 FF FF FF E0 0 7F FF FF FC 0 F FF FF FF 80 1 FF FF FF C0 0 3F 80 1 FF FF FF E0 0 7F FF FF FC 0 F E0 0 7F 80 1 FC 0 F E0 0 3F 80 0 FF FF FF F0 0 7F 80 1 FC 0 F FF FF FF 80 0 FF FF FF F0 0 3F FF FF FC 0 7 FF FF FF 80 1'

# A1

dump["A1"] = '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 FF FF FF FF FF FF FF FF FF FF 0 3 FC 0 F E0 0 7F 0 3 FC 0 1F E0 0 7F 0 1 FC 0 F E0 0 7F FF FF FC 0 1F FF FF FF 0 3 FF FF FF E0 0 7F FF FF FC 0 F FF FF FF 0 1 FF FF FF E0 0 3F FF FF FC 0 F FF FF FF 0 3 FC 0 1F E0 0 7F 80 1 FC 0 F E0 0 7F 80 1 FC 0 F E0 0 7F FF FF FC 0 F FF FF FF 80 1 FF FF FF E0 0 7F FF FF FC 0 F FF FF FF 80 1 FF FF FF E0 0 7F FF FF FC 0 F FF FF FF 80 1'

# A2

dump["A2"] = '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 3 FF FF FF FF FF FF FF FF FF FF 0 3 FC 0 1F E0 0 7F 0 3 FC 0 F E0 0 3F 0 1 FC 0 F E0 0 3F FF FF FC 0 1F FF FF FF 0 3 FF FF FF E0 0 7F FF FF FC 0 7 FF FF FF 0 1 FF FF FF E0 0 7F FF FF FC 0 F FF FF FF 80 1 FF FF FF E0 0 7F 80 1 FC 0 F E0 0 7F 80 0 FC 0 F E0 0 3F 80 1 FC 0 F FF FF FF 80 3 FF FF FF E0 0 7F FF FF FC 0 F FF FF FF 80 1'
dump["A2"] = '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 FF FF FF FF FF FF FF FF FF FF 0 1 FC 0 F E0 0 7F 80 1 FC 0 F E0 0 3F C0 1 FC 0 F E0 0 3F FF FF FC 0 F FF FF FF 80 1 FF FF FF F8 0 FF FF FF FC 0 F FF FF FF 80 3 FF FF FF F0 0 7F FF FF FC 0 F FF FF FF 80 1 FF FF FF F0 0 3F 80 1 FF 0 F F0 0 3F C0 0 FE 0 F F0 0 3F 80 1 FE 0 1F FF FF FF 80 0 FF FF FF F0 0 3F FF FF FE 0 1F FF FF FF 80 3 FF FF FF F0 0 3F FF FF FE 0 7'
dump["A2"] = '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 FF FF FF FF FF FF FF FF FF FF 0 1 FC 0 1F E0 0 FF 80 3 FC 0 1F E0 0 FF 80 3 FC 0 F E0 0 7F FF FF FC 0 F FF FF FF 80 1 FF FF FF E0 0 7F FF FF FC 0 F FF FF FF 80 1 FF FF FF F0 0 F FF FF FC 0 3 FF FF FF 80 1 FF FF FF F0 0 3F 80 1 FC 0 F F0 0 3F 80 3 FC 0 F F0 0 7F 80 1 FE 0 F FF FF FF 80 1 FF FF FF F0 0 3F FF FF FE 0 7 FF FF FF C0 1 FF FF FF F0 0 1F FF FF FF 0 7 FF FF FF C0 0'

# A3

dump["A3"] = '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 FF FF FF FF FF FF FF FF FF FF 0 3 FC 0 F E0 0 7F 0 3 FC 0 F E0 0 7F 0 3 FC 0 F E0 0 3F FF FF FC 0 F FF FF FF 80 3 FF FF FF E0 0 3F FF FF FC 0 F FF FF FF 80 3 FF FF FF E0 0 7F FF FF FC 0 F FF FF FF 80 1 FC 0 F FF FF FF 80 3 FC 0 F E0 0 7F 80 1 FC 0 7 E0 0 3F 80 3 FF FF FF E0 0 7F 80 1 FF FF FF E0 0 3F FF FF FC 0 7 FF FF FF 80 1'

dump["A3"] = '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 FF FF FF FF FF FF FF FF FF FF 0 3 FE 0 1F E0 0 7F 0 1 FC 0 F E0 0 7F 80 1 FC 0 F E0 0 7F FF FF FC 0 7 FF FF FF 80 1 FF FF FF E0 0 1F FF FF FC 0 F FF FF FF 80 1 FF FF FF F0 0 3F FF FF FC 0 F FF FF FF 80 1 FC 0 F FF FF FF 80 1 FC 0 F F0 0 7F 80 1 FE 0 F F0 0 3F 80 1 FF FF FF F0 0 7F 80 1 FF FF FF F0 0 3F FF FF FE 0 F FF FF FF 80 0 FF FF FF F0 0 3F FF FF FF 0 3 FF FF FF 80 0'

# A4

dump["A4"] = '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 3 FF FF FF FF FF FF FF FF FF FF 0 3 FC 0 F E0 0 7F 0 3 FC 0 1F E0 0 7F 0 3 FC 0 F E0 0 7F FF FF FC 0 F FF FF FF 0 3 FF FF FF E0 0 7F FF FF FC 0 F FF FF FF 0 1 FF FF FF E0 0 7F FF FF FC 0 F FF FF FF 0 1 FF FF FF E0 0 7F FF FF FC 0 1F E0 0 7F 80 1 FC 0 F E0 0 7F 80 1 FC 0 F E0 0 7F 80 1 FF FF FF E0 0 7F FF FF FC 0 F FF FF FF 80 3'

dump["A4"] = '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 7 FF FF FF FF FF FF FF FF FF FF 0 7 FC 0 3F F0 0 FF 80 3 FC 0 3F E0 0 7F 80 0 FC 0 1F E0 0 FF FF FF FC 0 0 FF FF FF 80 7 FF FF FF E0 0 7F FF FF FE 0 1F FF FF FF C0 3 FF FF FF F0 0 7F FF FF FE 0 F FF FF FF 80 0 FF FF FF E0 0 7 FF FF FC 0 F E0 0 FF 80 7 FC 0 1F E0 0 7F 80 1 FE 0 F F8 0 3F 80 1 FF FF FF F0 0 3F FF FF FE 0 3 FF FF FF C0 1 FF FF FF F0 0 3F FF FF FC 0 7'

dump["A4"] = '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 3 FF FF FF FF FF FF FF FF FF FF 0 3 FC 0 F E0 0 FF 0 3 FC 0 1F E0 0 FF 0 7 FC 0 F E0 0 7F FF FF FC 0 F FF FF FF 80 3 FF FF FF E0 0 7F FF FF FE 0 F FF FF FF 80 1 FF FF FF E0 0 7F FF FF FE 0 F FF FF FF 80 3 FF FF FF E0 0 3F FF FF FC 0 F E0 0 7F 80 3 FC 0 1F F8 0 7F 80 3 FC 0 F F0 0 7F 80 1 FF FF FF F8 0 3F FF FF FE 0 F FF FF FF 80 1 FF FF FF F0 0 3F FF FF FE 0 3 FF FF FF 80 0'

# A previous input

dump["A+"] = '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 FF FF FF FF FF FF FF FF FF FF 0 3 FC 0 1F E0 0 7F 0 3 FC 0 F E0 0 7F 0 1 FC 0 1F E0 0 7F FF FF FC 0 F FF FF FF 0 1 FF FF FF E0 0 7F FF FF FC 0 F FF FF FF 80 3 FF FF FF E0 0 7F FF FF FC 0 F FF FF FF 80 1 FC 0 F E0 0 7F FF FF FC 0 F E0 0 3F 80 3 FC 0 7 E0 0 3F 80 1 FF FF FF F0 0 3F FF FF FC 0 F F0 0 3F FF FF FC 0 3 FF FF FF 80 0 FF FF FF F0 0 3F FF FF FC 0 F FF FF FF 80 1'

# A next input

dump["A-"] = '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 3 FF FF FF FF FF FF FF FF FF FF 0 1 FC 0 1F E0 0 7F 0 3 FC 0 F E0 0 7F 0 3 FC 0 1F E0 0 7F FF FF FC 0 1F FF FF FF 0 1 FF FF FF E0 0 7F FF FF FC 0 1F FF FF FF 80 3 FF FF FF E0 0 7F FF FF FC 0 F FF FF FF 0 1 FF FF FF E0 0 3F 80 0 FF FF FF E0 0 7F 80 1 FC 0 F E0 0 7F 80 3 FC 0 F E0 0 3F FF FF FC 0 F F0 0 7F FF FF FC 0 F FF FF FF 80 1 FF FF FF F0 0 3F FF FF FC 0 F FF FF FF 80 1'

# B1

dump["B1"] = '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 FF FF FF FF FF FF FF FF FF FF 0 3 FC 0 F E0 0 7F 0 3 FC 0 F E0 0 7F 0 3 FC 0 1F E0 0 7F FF FF FC 0 F FF FF FF 0 1 FF FF FF E0 0 7F FF FF FC 0 7 FF FF FF 0 1 FF FF FF E0 0 7F FF FF FC 0 F FF FF FF 80 1 FF FF FF E0 0 7F 80 3 FC 0 F FF FF FF 80 1 FC 0 7 E0 0 3F 80 1 FC 0 F F0 0 3F FF FF FC 0 F FF FF FF 80 0 FC 0 F FF FF FF 80 1 FF FF FF F0 0 7F FF FF FC 0 7 FF FF FF 80 1'

# B2

dump["B2"] = '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 FF FF FF FF FF FF FF FF FF FF 0 3 FC 0 F E0 0 3F 0 3 FC 0 F E0 0 7F 0 3 FC 0 F E0 1 FF FF FF FC 0 F FF FF FF 0 1 FF FF FF E0 0 7F FF FF FC 0 F FF FF FF 80 1 FF FF FF E0 0 7F FF FF FC 0 F FF FF FF 80 1 FC 0 7 FF FF FF 80 3 FC 0 F FF FF FF 80 3 FC 0 F E0 0 3F 80 1 FC 0 F FF FF FF 80 3 FC 0 1F FF FF FF 80 1 FC 0 F FF FF FF 80 1 FF FF FF F0 0 7F FF FF FC 0 F FF FF FF 80 0'

# B3

dump["B3"] = '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 FF FF FF FF FF FF FF FF FF FF 0 1 FC 0 F E0 0 7F 0 3 FC 0 1F E0 0 7F 0 1 FC 0 F E0 0 7F FF FF FC 0 F FF FF FF 0 1 FF FF FF E0 0 3F FF FF FC 0 F FF FF FF 0 3 FF FF FF E0 0 7F FF FF FC 0 7 FF FF FF 80 1 FF FF FF E0 0 7F FF FF FC 0 F E0 0 7F FF FF FC 0 F E0 0 7F 80 3 FC 0 F F0 0 3F 80 0 FC 0 F FF FF FF 80 1 FC 0 F FF FF FF 80 1 FF FF FF F0 0 3F FF FF FC 0 7 FF FF FF 80 3'

# B4

dump["B4"] = '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 3 FF FF FF FF FF FF FF FF FF FF 0 3 FC 0 F E0 0 7F 0 1 FC 0 1F E0 0 7F 0 3 FC 0 1F E0 0 3F FF FF FC 0 F FF FF FF 80 3 FF FF FF E0 0 7F FF FF FC 0 F FF FF FF 80 1 FF FF FF E0 0 7F FF FF FC 0 F FF FF FF 80 1 FC 0 F E0 0 3F FF FF FC 0 F FF FF FF 80 1 FC 0 F E0 0 3F 80 1 FC 0 F FF FF FF 80 1 FF FF FF E0 0 3F 80 1 FC 0 F FF FF FF 80 1 FF FF FF F0 0 3F FF FF FC 0 7 FF FF FF 80 1'

for k, v in dump.iteritems():
    print 'const uint8_t rec' + k.replace('+', 'P').replace('-', 'M') + '[] PROGMEM = {' + ', '.join(hex(int(i, 16)) for i in v.split(' ')) + '};'

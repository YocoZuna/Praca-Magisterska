import ctypes
elo  = "4A0500D000000000041700001CD48A3FF816000040583E0FAAC3BC0C00003B0A3B0AD9003B0A3B0A0E000D00350C1F00C5FF860023000B00C3FFABFF00ACEA5D5D0428000E001000783ECAA2E9FF7F0020D6102606030500"
Ia = elo[108:112]
Ib = elo[112:116]
Ia  =int(Ia, 16)
Ib = int(Ib,16)


def ConvertToValue(Current):
    lower = (Current&0xFF00)>>8
    higher = (Current&0x00FF)<<8

    return ctypes.c_int16(higher+lower).value

#dupaa = bytearray(b'6\xe9\x80\x80\xec\x8c\x85\xe6\x80\x806\xe9\x80\x80\x1a\xe2\x80\x80\xe1\xa8\x80\x00 \x1a\xe2\x80\x80\xe1\xa8\x80\x00 \xd5\x8a\xed\x80\x80\x00\x00\xe1\xa3\xa4\x00\xe4\xba\x91\xe3\xbe\x8f\xe1\x9d\xb0\x00\xe2\xa7\xa1\xe1\x87\x94\xe2\x93\xb4\xe0\xb9\xb1\x00\xe0\xa8\xbb\xe0\xa8\xbb\xc3\x8c\xe0\xa8\xbb\xe0\xa8\xbb\x0e\r\xe0\xb0\xb5\x1f')
#print(dupaa.decode())
IPupa = ConvertToValue(Ib)


xd = "C90400E0110019005900591B9900D900190191099102D10251099101D101911451149100D1001109D108D1059105D107110851039103910451041119D118910B510BD10B110C510C910C49008900C900"
frmae = b'6\x00\x00\x90\x05\xc3\x00`6\x00\x00\x90\x1a\x00\x00 \x00\x1a\x00\x00 \x00\x1a\x00\x00 \x01\x1a\x00\x00 \x00J\x05\x00\xd0\x00\x00\x00\x00\xea\x18\x00\x00t!l?p\x17\x00\x00\xc1\x9c\xdc\x11r\x137\x0e\x00\x00;\n;\n\xca\x00;\n;\n\x0e\x00\r\x005\x0c\x1f\x00'
dupaa =bytearray()
4A0500D000000000000000001E173C407017000000000000B47F180000003B0A3B0A5E083B0A3B0A0E000D00350C1F00F6FF6B082A000B006C08D2FB00ACEA5D5D0428000E0010000000060372080700CB04FEFF04030500
int_val = int.from_bytes(frmae, "big")
print(int_val)
siusiek = []
iterator = 0
print(len(frmae))
for frame in range (0,len(frmae)):
            

    try:

       
        siusiek.append(int(frmae[iterator:iterator+2],16))
        iterator  =iterator+2
    except:

        print(f"Zjebalo się {frmae[iterator:iterator+2]}")

print(siusiek)
"""for i in siusiek:
    dupaa.append(i)"""
print(dupaa.decode("utf-8"))



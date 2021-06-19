# How to use libcdumper

```python
from libcdumper import *

dp = LibcDumper("setbuf", 0x7F6555FAD540)

print(f"[*] str_bin_sh --> {hex(dp.dump('str_bin_sh'))}")
print(f"[*] system --> {hex(dp.dump('system'))}")
```
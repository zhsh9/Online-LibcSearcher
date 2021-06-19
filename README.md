# Introduction

...

# How to install libcdumper

```bash
git clone https://github.com/ec1ipse-yes/1ibcDumper.git
cd 1ibcDumper
python3 setup.py develop
```

# How to use libcdumper

```python
from libcdumper import *

dp = LibcDumper("setbuf", 0x7F6555FAD540)

print(f"[*] str_bin_sh --> {hex(dp.dump('str_bin_sh'))}")
print(f"[*] system --> {hex(dp.dump('system'))}")
```
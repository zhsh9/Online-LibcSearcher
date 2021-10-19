# Introduction

This tool is the online version of LibcSearcher, due to the fact that the older LibcSearcher's Libc library has not been updated for a while and causes some issues. Besides, it is based on the online libcseachers website to gain the proper result.

# How to install Online-LibcSearcher

```bash
git clone https://github.com/eclipse-yes/Online-LibcSearcher.git
cd Online-LibcSearcher
python3 setup.py develop
```

# How to use Online-LibcSearcher

```python
from libcsearcher import *

ls = LibcSearcher("setbuf", 0x7F6555FAD540)
ls.add_symbol_info("puts", 0x7F6555FA5A30)

print(f"[*] str_bin_sh --> {hex(ls.dump('str_bin_sh'))}")
print(f"[*] system --> {hex(ls.dump('system'))}")
```
# Introduction

orz

# How to install Online-LibcSearcher

```bash
git clone https://github.com/ec1ipse-yes/1ibcDumper.git
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
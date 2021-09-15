#!/usr/bin/env python3

import requests
import json


class OnlineLibcSearcher:
    def __init__(self, leaked_symbol_name: str = None, leaked_symbol_addr: int = None):
        if leaked_symbol_name is None or leaked_symbol_addr is None:
            print(f"[X] Please use OnlineLibcSearcher based on information of leaked function.")
        else:
            self.leaked_symbol_name = leaked_symbol_name
            self.leaked_symbol_addr = leaked_symbol_addr
            print(
                f'[+] Symbol name: "{self.leaked_symbol_name}". Address: "{hex(self.leaked_symbol_addr)}"'
            )

        self.url = "https://libc.rip/api/find"
        self.payload = {
            "symbols": {self.leaked_symbol_name: f"{hex(self.leaked_symbol_addr)}"}
        }

        self.libcs = dict()
        self.libc_names = []
        self.selected_lic = ""

    def add_symbol_info(self, leaked_symbol_name: str, leaked_symbol_addr: int):
        self.payload["symbols"][leaked_symbol_name] = f"{hex(leaked_symbol_addr)}"
        self.get_libcs()

    def get_libcs(self):
        libcs = json.loads(
            requests.post(
                url=self.url,
                headers={"Content-Type": "application/json"},
                data=json.dumps(self.payload),
            ).content
        )

        for libc in libcs:
            self.libc_names.append(libc["id"])
            self.libcs[libc["id"]] = libc

        self.which_one()

    def which_one(self):
        print(f"[*] There are {len(self.libc_names)} potential libcs:")
        for i, libc_name in enumerate(self.libc_names):
            print(f"[*] {i}. {libc_name}")

        selected_num = int(input("[?] Which libc version you want to select: "))
        self.selected_lic = self.libc_names[selected_num]
        print("[+] The selected libc is:", self.selected_lic)

    def dump(self, wantted_symbol_name: str):
        if self.selected_lic == "":
            self.get_libcs()

        leaked_symbol_at_libc = int(
            self.libcs[self.selected_lic]["symbols"][self.leaked_symbol_name], 16
        )
        wantted_symbol_at_libc = int(
            self.libcs[self.selected_lic]["symbols"][wantted_symbol_name], 16
        )

        base = self.leaked_symbol_addr - leaked_symbol_at_libc
        wantted_symbol_addr = base + wantted_symbol_at_libc

        return wantted_symbol_addr


if __name__ == "__main__":
    # Example: how to use OnlineLibcSearcher
    setbuf_addr = 0x7F6555FAD540
    dp = OnlineLibcSearcher("setbuf", setbuf_addr)

    print(f"[*] __libc_start_main_ret --> {hex(dp.dump('__libc_start_main_ret'))}")
    print(f"[*] dup2 --> {hex(dp.dump('dup2'))}")
    print(f"[*] printf --> {hex(dp.dump('printf'))}")
    print(f"[*] puts --> {hex(dp.dump('puts'))}")
    print(f"[*] read --> {hex(dp.dump('read'))}")
    print(f"[*] setbuf --> {hex(dp.dump('setbuf'))}")
    print(f"[*] str_bin_sh --> {hex(dp.dump('str_bin_sh'))}")
    print(f"[*] system --> {hex(dp.dump('system'))}")
    print(f"[*] write --> {hex(dp.dump('write'))}")

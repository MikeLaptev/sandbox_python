class DefangingIPAddress:
    """
    Leetcode #1108
    Link: https://leetcode.com/problems/defanging-an-ip-address/
    """

    def defang_ip_addr(self, address: str) -> str:
        return "[.]".join(address.split("."))

    def defang_ip_addr_naive(self, address: str) -> str:
        st = ""
        for i in address:
            if i == ".":
                st = st + "[.]"
            else:
                st = st + i
        return st

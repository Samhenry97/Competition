import re

class Solution:
    def validIPAddress(self, ip: str) -> str:
        data = ip.split('.')
        if len(data) == 4:
            valid = True
            for part in data:
                if len(part) == 0:
                    valid = False
                    continue
                if len(part) > 3 or not part.isnumeric() or int(part) >= 256:
                    valid = False
                if len(part.lstrip('0')) == 0 and int(part) == 0 and len(part) > 1:
                    valid = False
                if len(part.lstrip('0')) != len(part) and int(part) != 0:
                    valid = False
            if valid:
                return 'IPv4'
        data = ip.split(':')
        if len(data) == 8:
            valid = True
            for part in data:
                if len(part) > 4 or not re.match(r'^[0-9a-fA-F]+$', part):
                    valid = False
            if valid:
                return 'IPv6'
        return 'Neither'
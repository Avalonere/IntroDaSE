import re

pattern = r"^[1-9]\d{5}(19|20)\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$"


def match(identification):
    valid = 0
    if re.match(pattern, identification):
        valid = 1
    return valid

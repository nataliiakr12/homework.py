import keyword
import string
def is_valid_variable(name: str) -> bool:
    if not name or name[0].isdigit():
        return False
    if any(ch.isupper() for ch in name):
        return False
    allowed_chars = set(string.ascii_lowercase + string.digits + "_")
    if any(ch not in allowed_chars for ch in name):
        return False
    if keyword.iskeyword(name):
        return False
    if set(name) == {"_"} and len(name) > 1:
        return False
    return True

tests = [ "_", "__", "--", "x", "get_value", "get value", "get:value",
    "some_super_puper_value", "Get_value", "getValue", "m3", "3m",
    "assert", "assert_exceptions"]
for t in tests:
    print(f"{t} => {is_valid_variable(t)}")

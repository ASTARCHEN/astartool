

from astartool.project._platform import is_windows, is_linux, is_32bit, is_64bit

print("windows", is_windows())
print("64bit", is_64bit())
print("linux", is_linux())
print("32bit", is_32bit())

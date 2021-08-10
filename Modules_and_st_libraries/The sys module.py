# The “sys.path” list is initialized from the PYTHONPATH environment variable. Is it possible to change it from within
# Python? If so, does it affect where Python looks for module files? Run some interactive tests to find it out.
import sys
print(sys.path[2])
a = sys.path

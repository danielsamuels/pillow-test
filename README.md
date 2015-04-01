Test case for a Django 1.8 / Pillow 2.8.0 bug.

```
$ pip install -r requirements.txt
$ ./manage.py test
```

```
======================================================================
ERROR: test_invalid_file (testing.tests.PillowTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/pillow-test/testing/tests.py", line 12, in test_invalid_file
    Image.open(test_file)
  File "/pillow-test/.venv/lib/python2.7/site-packages/PIL/Image.py", line 2279, in open
    if not accept or accept(prefix):
  File "/pillow-test/.venv/lib/python2.7/site-packages/PIL/FliImagePlugin.py", line 33, in _accept
    return i16(prefix[4:6]) in [0xAF11, 0xAF12]
  File "/pillow-test/.venv/lib/python2.7/site-packages/PIL/_binary.py", line 39, in i16le
    return unpack("<H", c[o:o+2])[0]
error: unpack requires a string argument of length 2
```

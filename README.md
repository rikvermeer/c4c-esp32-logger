# c4c-esp32-logger

###Repl
```
screen /dev/cu.usbserial-0001 115200
```

###Ampy
Use ampy to interact with the filesystem
```
ampy -p /dev/cu.usbserial-0001 ls
```

### Micropython files
```
app/boot.py
app/main.py
```

### Persistent dirs
```
app/config
app/secrets
```

### OTA replaceable
```
app/main/*
```

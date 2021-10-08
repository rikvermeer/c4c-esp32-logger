def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.config(reconnects=5)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('Stichting de Melkweg', 'melkweggast')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

def read_secrets():
    from secrets import wifi
    #SSID #PSK
    pass

# This should be done through the REPL config page
#def write_secrets():
#    pass

def is_connected():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    return wlan.isconnected()

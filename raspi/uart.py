from wltrace import wltrace

trace = wltrace.load_trace('/home/pi/')
for pkt in trace:
    print pkt

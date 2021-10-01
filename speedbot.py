import speedtest 

def speed_test_acc():
    acc = False
    speedyrit = speedtest.Speedtest()
    x=speedyrit.download()/1000000#converting to mbps
    y=speedyrit.upload()/1000000#converting to mbps
    if x>0.5 and y>0.5: acc = True
    else: pass
    return acc, x, y

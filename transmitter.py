import subprocess

SENDIQ = "/usr/bin/sendiq"
FREQ = 433.92

def sendiq(rec):
    return subprocess.run([SENDIQ,'-s','250000','-f',f'{FREQ}e6','-t','u8','-i',rec, '&'], stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)
    
def light():
    sendiq('records/light.iq')

def fan(power):
    if power == 0:
        rec = 'records/off.iq'
    elif power == 1:
        rec = 'records/low.iq'
    elif power == 2:
        rec = 'records/medium.iq'
    elif power == 3:
        rec = 'records/high.iq'
    else:
        return
    sendiq(rec)
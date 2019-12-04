from sense_hat import SenseHat
import time
import requests


sense = SenseHat()
future = 120                   #this is how long to program waits befor pushing notif
incrementer = 0
tempchange = 0
accelchange = 0
one = 1

while True:
    if (tempchange == 1):           #this pushes notif when the car has been too hot for 'future' seconds
        print("Mom its too hot")
        r = requests.post('https://maker.ifttt.com/trigger/baby_time/with/key/dYUTqII7gpo7M-bXF_6OkL2jReZiTqh-8O-IBnuoj_V', params={"value1":"none","value2":"none","value3":"none"})
        tempchange = tempchange + one
    if (accelchange == 1):
        print("Mom you forgot me")    #this pushes notif when the car has been still for 'future' seconds
        r = requests.post('https://maker.ifttt.com/trigger/baby_time/with/key/dYUTqII7gpo7M-bXF_6OkL2jReZiTqh-8O-IBnuoj_V', params={"value1":"none","value2":"none","value3":"none"})
        accelchange = accelchange + one
    
    
    p = (sense.pressure-988)
    temp = sense.get_temperature()
    accel = sense.get_accelerometer_raw()
    acc = '%s,%s,%s' % (accel['x'], accel['y'], accel['z'])
       
    while ((p>4) and (incrementer != future)):
        p= (sense.pressure-988)
        accel = sense.get_accelerometer_raw()
        temp = sense.get_temperature()
        
        
        if (temp>=3) :
           print("its too hot")
           tempchange = 1
        
        elif (accel['x'] < 1, accel['y'] < 1):
           print("we stopped somewhere")
           # if tempchange!=1:
             #   accelchange=1
                
        else:
         
            time.sleep(1)
            incrementer = incrementer + one

            
       

        


      
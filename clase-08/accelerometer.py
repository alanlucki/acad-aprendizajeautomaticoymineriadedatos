import androidhelper,time

def readAcc():
    dt=100
    endTime=30000
    timeSensed=0
    droid.startSensingTimed(2,dt)
    while timeSensed <= endTime:
        senout=droid.sensorsReadAccelerometer().result
        time.sleep(dt/1000.0)
        timeSensed+=dt
        file.write(str(timeSensed) + ',' + str(str(senout).strip('[]')+'\n'))
    file.close()

droid=androidhelper.Android()

file=open('acelerometro_samuel.csv','w')

readAcc()

droid.stopSensing()


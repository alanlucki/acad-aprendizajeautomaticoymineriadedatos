#include <Wire.h>
#define MPU 0x68
//precision de conversion datasheet mpu6050
#define A_R 16384.0
#define G_R 131.0
//radiane s a PI
#define RAD_A_DEG = 57.295779
//variables RAW
int16_t ACX,ACY,ACZ,GYX,GYY,GYZ;
//valores procesados_angulos arreglos
//[X,Y] posicion
float ACC[2];  //aceleromtero
float GY[2];  //giroscopio
float ANGLE[2];  //angulo

void setup()
{
  Wire.begin();  //start
  Wire.beginTransmission(MPU);//llamando a MPU6050
  Wire.write(0x6B);  //rellamada
  Wire.write(0);  //encendido MPU
  Wire.endTransmission(true);  //end
  Serial.begin(9600);
}

void loop()
{
  Wire.beginTransmission(MPU);
  Wire.write(0x3B);  //primer registro ACX
  Wire.endTransmission(false);
  Wire.requestFrom(MPU,6,true);//se pide 6 registros siguientes
  //solo acelerometro
  ACX=Wire.read()<<8|Wire.read();
  ACY=Wire.read()<<8|Wire.read();
  ACZ=Wire.read()<<8|Wire.read();
  //calculo de angulos formula arctg()
  ACC[1]=atan(-1*(ACX/A_R)/sqrt(pow((ACY/A_R),2)+pow((ACZ/A_R),2)))*RAD_TO_DEG;
  ACC[0]=atan(-1*(ACY/A_R)/sqrt(pow((ACX/A_R),2)+pow((ACZ/A_R),2)))*RAD_TO_DEG;
  
  //solo giroscopio
  Wire.beginTransmission(MPU);
  Wire.write(0x43);
  Wire.endTransmission(false);
  Wire.requestFrom(MPU,4,true);//4 valores del giroscopio
  GYX=Wire.read()<<8|Wire.read();
  GYY=Wire.read()<<8|Wire.read();
  // angulo giroscopio
  GY[0]=GYX/G_R;
  GY[1]=GYY/G_R;
  //filtro complementario
  ANGLE[0]=0.98*(ANGLE[0]+GY[0]*0.01)+0.02*ACC[0];
  ANGLE[1]=0.98*(ANGLE[1]+GY[1]*0.01)+0.02*ACC[1];
  //enviando resultados.
  Serial.print("Angulo X: ");Serial.print(ANGLE[0]);
  Serial.print("Angulo Y: ");Serial.println(ANGLE[1]);
  delay(100);
}



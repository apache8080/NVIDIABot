'''
Copyright (c) 2014, Rishi Desai
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''
import serial

class Arduino:
    
    ser = serial.Serial('/dev/ttyACM0')
    
    #def __init__():
        
    
    def sendData(self, data):
        dataS=""
      	for i in range(2):
      	  if(len(str(data[i]))==2):
        		s=""
        		s+=str(len(str(data[i])))
        		s+=","
            s+=",".join(str(data[i]))
            s+=","
        		dataS+=s
          elif(len(str(data[i]))==3):
            s=""
      		  s+=str(len(str(data[i])))
      		  s+=","
      		  s+=",".join(str(data[i]))
            s+=","
            dataS+=s
          else:
      		  s=""
            s+=str(len(str(data[i])))
        		s+=","
        		s+=",".join(str(data[i]))
            s+=","
      		  dataS+=s

        x=2
        while(x<len(data)):
          dataS+=str(data[x])
          dataS+=","
          x+=1
          print dataS            
        	Arduino.ser.write(dataS)
        	Arduino.ser.flushOutput()
          #print Arduino.ser.read(2)

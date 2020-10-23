import sys
sys.path.append('./remoteAPI')
import b0RemoteApi as bSim

import rospy

import time

import matplotlib.pyplot as plt
from PIL import Image
import array


theClient = bSim.RemoteApiClient('b0Api_VREP','b0Api',60)
tValue = 0
theClient.im = Image.new("RGB", (256, 256), "#000000")

def imageCallback(msg):
	#print('Received image.', msg[1])
	#plt.imshow(im)
	#plt.show()
	global tValue
	theClient.im = Image.frombuffer("RGB", (msg[1][0],msg[1][1]), 
		msg[2], "raw", "RGB", 0, 1)
	tValue += 1
	#plt.imshow(im)
	#plt.show()

if __name__ == '__main__':
	'''
	with bSim.RemoteApiClient('b0Api_VREP','b0Api',60) as theClient:
		theClient.simxAddStatusbarMessage('Hello',theClient.simxDefaultPublisher())
		theClient.simxStartSimulation(theClient.simxServiceCall())

		time.sleep(5)

		theClient.simxStopSimulation(theClient.simxServiceCall())
	'''
	#theClient = bSim.RemoteApiClient('b0Api_VREP','b0Api',60)
	theClient.simxAddStatusbarMessage('Hello',theClient.simxDefaultPublisher())

	#theClient.simxSynchronous(True)
	#theClient.simxGetSimulationStepStarted(theClient.simxDefaultSubscriber(simulationStepStarted))
	#theClient.simxGetSimulationStepDone(theClient.simxDefaultSubscriber(simulationStepDone))

	theClient.simxStartSimulation(theClient.simxDefaultPublisher())
	vHandle = theClient.simxGetObjectHandle('Vision_sensor',theClient.simxServiceCall())
	theClient.simxGetVisionSensorImage(vHandle[1], False, 
		theClient.simxDefaultSubscriber(imageCallback))

	for i in range (0,15):
		print("Index --> ",i)
		time.sleep(1)
		print(tValue)
		plt.imshow(theClient.im, origin='lower')
		plt.show()
		theClient.simxSpinOnce()		# To Update the Local data
		
	theClient.simxStopSimulation(theClient.simxDefaultPublisher())
	theClient.__exit__()
	#'''

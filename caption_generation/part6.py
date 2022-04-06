import os

for i in range(0,500):
	command='curl -X POST "localhost:8764/inception/v3/caption/image" --data-binary @generated_images/samples_8_' + str(i) + '.png >> out.out'
	os.system(command)
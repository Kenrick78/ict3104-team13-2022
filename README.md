# ICT3104 Team 13 Activity Detection Colab

Hello all! Welcome to the ICT3104 Group 13 Hub Activity Colab! This notebook will take you through the steps of running an "out-of-the-box" activity detection model on videos.


Current Working Usages:
### Feature Extraction
Fully working, use github/DanialAshidiq as there are issues on utils.py in the main v-aishin code. Steps you need to do:
- Make sure you have your video inputs and store it somewhere, you can use my own video inputs stored in MyDrive downloaded and shared by me
- The code that calls the extractI3D is meant for client showcase, you do not really need to run this code
- Main code is the running of main.py, make sure your filepath for input and output are in the arguments, or you can test using my filepaths as well.

### Validate_Train_Test.py
Fully working, 3 usages needed:
- inputfilepath (this is your extracted videos)
- comparison dataset (we have to refer using the existing smarthome_CS_51.json)
- outputfilepath (this is where you want to store)

Output of validate_train_test.py = a new json file called smarthome_CS_32.json (This is will only write the subset, testing, training, duration and list of numpy values meant for training and testing in TSU or STEP/etc).

### Training the Model:

Requirements needed:
- Pre-Trained Model requested: PDAN_TSU_RGB
- list of numpy files for training, this will be located in your feature extraction output folder
- the smarthome_CS_32.json for 80% training and 20% testing. This is where PDAN will be use as the loaded model, and it will refer to the numpy files accordingly with your json file. Afterwards it will generate a NEW model
- Create a folder called PDAN as the code will save your weights and the model's epoch accuracy into that specific directory. This will also be added as an argument in the run.sh file


Main outputs after training: (files will look somewhat like this under your PDAN) by default 140 epochs 2 batch sizes for better accuracy
- PDAN_model_epoch_0002(learning rate)_60(epoch)
- PDAN_weights_epoch_0002_60 (epoch)

*Updated Train.py: more arguments for filepath (that is all)*

### Testing, Inference, Evaluation the Model:
- Test.py script is EXACTLY the same as train.py
- Set train to False, this is to prevent training over again

Video Inferencing:
- Run the pre-trained model (PDAN_TSU_RGB) and collate its values. This values are already stored in the dataloaders. 

Dataloaders are used because torch is used. Dataloaders['val'] is where the results will display complex values (must understand):

- Ground truth
- losses
- mAP values
- etc

These values will be used to do:
- Video Captioning
- Generate a CSV File (with all the values, ground truth, etc)
- Mapping it to your annotations (0-50)

Required steps to do inside test.py (In progress not done yet):
- Method to use the dataloaders and write in a csv file
- Method to use for caption videos
- Method to map with annotations

### Visualisation using wandb.ai
- wandb.ai requires login account information and apikey (use your own)
- Use the generated visualise.csv file to visualize outputs

### GUI
- Run GUI Cell to generate TKINTER GUI in jupyter notebook
Usages:
- Specify your root filepath to the /ML_Activity_Detection in the text field inside the GUI
- Press Train button to run training
- Press Test button to run testing
- Press Inference Button to run inference

- Visualisation has no button (only output is shown currently and working code is in visualisation.py)

Do training using STEP
- Setting different Modes: [TSU, STEP] 


[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Kenrick78/ict3104-team13-2022/main?labpath=ML_Activity_Detection.ipynb)

image: https://mybinder.org/badge_logo.svg

target: https://mybinder.org/v2/gh/Kenrick78/ict3104-team13-2022/main?labpath=ML_Activity_Detection.ipynb

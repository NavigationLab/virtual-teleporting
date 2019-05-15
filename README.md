# A VR Navigation Testbed

### Summary
Teleporting is a popular interface to allow virtual reality users to explore environments that are larger than the available walking space. The research team developed the three virtual environments enclosed in this project as the basis of five experiments to evaluate the spatial cognitive consequences of teleporting, and to identify environmental cues that could mitigate those costs.

Experiment demonstration videos, data, and other materials related to these experiments may be found [here](https://osf.io/m4zfv/). The complete results of this work and implications for VR navigation design will be published in the near future.

### The Experimental Task 
Experimenters used the application to lead participants through a [triangle completion task](https://books.google.com/books?id=zN_WAgAAQBAJ&pg=PA86) by traversing two outbound path legs before pointing before to the unmarked path origin. Locomotion was performed via one of three methods:
1. Walking
2. Partially Concordant Teleporting
3. Discordant Teleporting
The latter two interfaces are distinguished by the concordance between movement of the body and movement through the virtual environment. In the partially concordant teleporting interface, participants teleported to translate(change position) but physically turned their body to rotate. In the discordant teleporting interface, participants teleported to both translate and rotate.

### Usage
This project may be used to replicate the results found in our presented work. To run the application, clone the repository and open the project in Unity. The project was developed in and is known to work with Unity v2018.2.14f1, though it should be compatible with subsequent versions at the time of this writing with only minor modifications.

Upon running the application, experiment data will be stored in ```ViveGame-master/Data/```. To process the data for analysis, copy the ```Data``` folder into ```data_collection``` and use Python 3 to run the script ```src/main.py```. Python will generate an adjacent ```Output``` folder containing the processed data. See the README file within data_collection for more details.

### Contact
This project was developed by the Iowa State University Navigation Lab located in the Department of Psychology and affiliated with the Human-Computer Interaction Program. For questions or comments regarding this project, please contact principal investigator [Dr. Jonathan Kelly](mailto:jonkelly@iastate.edu).


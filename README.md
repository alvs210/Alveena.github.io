# EDGAR - Poetry Chatbot

A simple ChatBot that provides poems based on the user's emotions and also allows users to add emotions with corresponding poetry.
You can use it here (Gmail account required): [EDGAR, The Poetry Bot](https://colab.research.google.com/drive/1tPSSPTP4n-p-GKTKaz8RkV04kJQtW5ly?usp=sharing)

## Getting Started - Personal Chatbot!

You can either run this in your Google Colab notebook (suggested) or locally as a Python file.

## Prerequisites - Google Colab

Download the EDGARPoemsChatbot.ipynb file and upload it into your Google Colab notebook. 
Save the PoetryIntents1234.json file into your own github or Google Drive.

In the first code chunk of the EDGARPoemsChatbot.ipynb file, adjust 'file_path' to be the path to your copy of the PoetryIntents1234.json file.

```
file_path = 'https://raw.githubusercontent.com/alvs210/PoetryChatter/main/PoetryIntents1234.json'
```
If you saved the file in your github, then simply replace the present URL with the URL to the file in your github.

If you saved the file in your Google Drive, this requires you to mount your Google Drive and direct a path to the file through your Google Drive.
To mount your Google Drive, add this code chunk:
```
from google.colab import drive
drive.mount('/content/drive')
```
Then replace the file_path with the path to the PoetryIntents1234.json file in your Drive. The code below should help!
```
from google.colab import files
uploaded = files.upload()

import json
with open('your_file_name.json', 'r') as f:
  data = json.load(f)
```
## Prerequisites - Local File

Download the .py file and the PoetryIntents1234.json file. You will need to adjust the code, as we did for the Google Colab file, to import and read the PoetryIntents1234.json file. Ensure both files are in the same current directory.

You'll also need the followng installations!

```
install nltk
install tensorflow as tf
install json
install numpy as np
install pandas as pd
install pickle
install random

```
## Roadmap
## Data Pre-Processing
## Chatbot Explanations
## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [Hat tip to anyone whose code was used
* Inspiration
* etc](https://github.com/vedrosuwandi/ChatBot)

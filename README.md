# COVID19_Web_Scraper

### Project Description
Scrapes COVID-19 data from the [Worldometeres website](https://www.worldometers.info/coronavirus/#countries) using BeautifulSoup and allows users to ask about country-wise live statistics of the development of COVID-19 in any country. Uses Google's Web Speech API for speech recognition to detect, understand and reply to the user.

### Utilities used
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to perform web scraping and retrieve live COVID-19 statistics
* [PyAudio](https://pypi.org/project/PyAudio/) for dealing with real-time audio input
* [Speech_recognition](https://pypi.org/project/SpeechRecognition/) library for Speech-to-Text for understanding user's spoken queries
* [Pyttsx3](https://pypi.org/project/pyttsx3/) for Text-to-Speech to return the statistic queried for by the user

### Setup
```python
pip install -r requirements.txt
```

### Usage
For using this project, simply navigate to the project directory and run ```python audio.py``` in your terminal. 
Once it is running, a conversation can be started by saying ```Hey, Buddy!``` using the computers default microphone. The user will be greeted with ```Hello User```.After this, simple queries regarding live COVID-19 statistics for any country can be asked. 

Here are a few examples of queries:
> Show me today's stats for USA <br>
> What are the number of active cases in Japan right now? <br>
> How many new deaths have occured in India today? <br>
> Total number of cases in USA. <br>
> How many total tests has Russia conducted? <br>
> What is the total number of recovered patients in China? <br>

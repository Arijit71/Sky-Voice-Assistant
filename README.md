# Sky Voice Assistant


## Video Demo: https://youtu.be/-HHHjbyfgi4


## Introduction
Welcome to Sky, a versatile voice assistant developed using Python! Sky leverages the power of ChatGPT 3.5 Turbo, chosen for its speed compared to other models like ChatGPT-4. As a voice assistant, quick responses are crucial, and ChatGPT 3.5 Turbo delivers just that. Additionally, the engine has been customized to provide responses in an easy-to-understand language, making Sky an efficient and user-friendly assistant.


## Features


### ChatGPT 3.5 Turbo Integration
Sky integrates with ChatGPT 3.5 Turbo using an API key, allowing it to perform all the tasks that ChatGPT 3.5 Turbo can handle. However, as a voice assistant, Sky is designed to handle interactions verbally and provide both text and audio outputs. It does not retain memory of previous interactions, making each session independent.

### Current News Headlines
Stay updated with the latest news! Sky can fetch and read out the current news headlines of your country using an API key. Just ask Sky for the news, and it will keep you informed with the latest happenings.

### Open Popular Websites
Need to quickly access a popular website? Simply tell Sky which site you want to visit, and it will open it for you immediately. No need to manually type URLs or search for the site.

### Play Music According to Mood
Enjoy music tailored to your mood. Just tell Sky your mood, like "play thriller," and it will find and play a suitable playlist or video for you. Whether you're in the mood for upbeat tunes or relaxing melodies, Sky has got you covered.

### Play Specific Songs
Want to listen to a particular song? Sky can search for and play any song you desire. Just tell Sky the song name, and it will find the song and give you the option to select the video to watch.

### Personalized Greetings
Sky greets the current user logged into the computer with a delightful image of an adorable cow, using the cowsay module in Python. It's a fun way to start your interaction with Sky!


## Getting Started


### Prerequisites
- Python 3.6 or higher
- API key for ChatGPT 3.5 Turbo
- API key for news service


### Installation
1. Clone the Sky repository:

        git clone https://github.com/Arijit71/Sky-Voice-Assistant.git
        cd Sky-Voice-Assistant


2. Install the required dependencies:

        pip install -r requirements.txt


### Configuration
1. Set up your API keys in the `config.py` file:

    CHATGPT_API_KEY = "your_chatgpt_api_key"
    NEWS_API_KEY = "your_news_api_key"


### Running Sky
Start the Sky voice assistant by running:

    python main.py


## Using Sky


### Interacting with Sky
Sky is designed to interact with you verbally. Speak your commands, and Sky will respond with both text and audio outputs.


#### Example Commands:
- "What's the latest news"
- "Open YouTube"
- "Play romantic music"
- "Play Sun raha hai na tu"
- "Good morning"
- "Greet me"


## Conclusion


Sky is your friendly AI powered voice assistant, ready to help with a variety of tasks. Whether you need the latest news, quick access to websites, mood-based music, or just a friendly greeting, Sky is here to assist you. Please do check out the video demo which I have created. Thank You!

Enjoy using Sky and explore its many capabilities!

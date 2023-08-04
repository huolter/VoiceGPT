# Talk to GPT

<p align="center">
  <img src="img/hal.jpg" alt="HAL Image" width="400">
</p>

## AI Assistant with Speech Interaction
### A simple script to *talk* with GPT using OpenAI and Azure Speech Services

This GitHub repository contains a Python program that implements an AI assistant capable of interactive conversations with users using both text and speech. The assistant is powered by OpenAI's GPT-3.5 model for natural language processing and Azure Cognitive Services for speech recognition and text-to-speech synthesis.

## Features

- Engaging and helpful AI assistant with natural language understanding.
- Recognizes speech input from the user and converts it into text.
- Generates contextually relevant and engaging responses using GPT-3.5. (or any model you decide)
- Converts AI responses into spoken output using text-to-speech synthesis using Azure.
- Keeps the conversation history limited to the last 8 exchanges. This can be changed.
- Funny and entertaining responses to create a positive user experience.

## Prerequisites

To run the AI assistant, you will need the following:

- Python 3.x installed on your system.
- Environment variables set up for the necessary API keys:
    - OPENAI_API_KEY: API key for OpenAI GPT-3.5 API.
    - COG_SERVICE_KEY: API key for Azure Cognitive Services.
    - COG_SERVICE_REGION: Region for Azure Cognitive Services.
    - Azure account 
    - OpenAI account

## Setup

1. Clone this repository to your local machine.
2. Install the required Python packages by running `pip install -r requirements.txt`.
3. Create a `.env` file in the root directory of the project and set the environment variables mentioned in the prerequisites.

## Usage

1. Ensure your microphone is working correctly.
2. Run the program by executing `talk_gpt.py`.
3. Speak when prompted, and the assistant will respond to your input.

## Configuration

- You can modify the conversation history limit by changing the `-8` value in the `get_response_from_gpt(prompt)` function within `main.py`.

## Notes

- The speech recognition and text-to-speech synthesis depend on Azure Cognitive Services. Please ensure you have an active subscription and the appropriate keys and region set in the environment variables.

## Acknowledgments

- This program uses OpenAI's GPT-3.5 model to generate conversational responses. Visit [OpenAI's website](https://openai.com/) to learn more about their APIs and services.
- The speech recognition and text-to-speech synthesis are powered by Azure Cognitive Services. Check out [Microsoft's Azure Cognitive Services](https://azure.microsoft.com/en-us/services/cognitive-services/) for more information.



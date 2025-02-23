# AI AIOGRAM Bot

## Description
A Telegram bot that utilizes AI to interact with users, providing information and assistance through conversation.

## Features
- Responds to user messages
- Uses OpenAI for generating responses
- Maintains conversation history

## Requirements
- Python 3.x
- [aiogram](https://github.com/aiogram/aiogram) - For Telegram bot framework
- [SQLAlchemy](https://www.sqlalchemy.org/) - For database management
- [OpenAI API](https://beta.openai.com/docs/) - For AI responses

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MARVRK/AI_AIOGRAM_BOT.git
2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv .venv
3. Activate the virtual environment:
   On Windows:
   ```
   .venv\Scripts\activate
   ```
   On Linux:
    ```bash
    python -m venv .venv
4. Install the required dependencies:
    ```bash
     pip install -r requirements.txt
5. Create a .env file in the root directory of the project and add your OpenAI API key:
    ```bash
   OPENAI_API_KEY=your_openai_api_key_here
6. Run the bot:
    ```bash
   python main.py

# Mental health assistance Chatbot

## Overview
This project is a Python-based chatbot system designed to interact with users, manage user data, and store user interactions. The chatbot is built with a focus on flexibility, allowing for easy training and customization.

## Project Structure

- **chatterbot/**: This directory contains the core chatbot engine. It is powered by the ChatterBot - an AI chatbot developed by Gunthercox (Compatible with python3.8 version).This directory is built upon the old ChatterBot version 1.0.8, which is compatible with
the latest python version.

- **UserData/**: This folder is intended for storing user-specific data. It stores conversation logs in a sqlite3 database
- **datalib.py**: A module that stores all the training data sets.

- **Main.py**: The entry point for the chatbot application. Running this script likely initializes the chatbot, sets up necessary configurations, and starts the main loop to interact with users.

- **trainer.py**: This script or module is responsible for training the chatbot. It invokes the **trainers.py** file from the **chatterbot** module and trains the model with the data provided

- **user_log.csv**: A CSV file that stores logs of user, login details and their password.

- **users.py**: This module might manage user authentication, profile creation, and other user-related functionalities. It likely interacts with `UserData/` to store and retrieve user information.

- **.gitattributes**: A Git configuration file that controls various attributes, such as handling end-of-line conversions or defining file type behaviors.

- **README.md**: The documentation file you are currently reading.

- **requirements.txt**: A list of Python dependencies required for the project. This file can be used with pip to install all necessary packages: `pip install -r requirements.txt`.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Super3_TECH-A-THON.git
   cd Super3_TECH-A-THON
   ```

2. Install the required Python packages: (Note microsoft visual C++ 14.0 or greater is required)
   Get it here- https://visualstudio.microsoft.com/visual-cpp-build-tools/
   ```bash
   
   pip install -r requirements.txt
   ```
3. Please install en_core_web_sm
   ```bash
   python -m spacy download en_core_web_sm
   ```
## Usage

1. **Run the chatbot**:
   ```bash
   python Main.py
   ```

2. **Train the chatbot**:
   ```bash
   python trainer.py
   ```
## Training
        This Chatbot is trained for Mental Health Care Assistance. It can also be trained in many other domains.Use the following code to train the model in the way you want. Provide the data on which you want to train the model.
    **Train the chatbot**:
   ```bash
   python trainer.py
   ```
## Features

- **User Authentication**: Users are prompted to provide a username and password, which are stored and managed securely. They can also use the chatbot as a general user.
- **Customizable Responses**: The chatbot's responses can be customized and trained using the `trainer.py` script.
- **User Data Management**: The system logs user interactions and maintains user-specific data for personalized experiences.

## Contributing

Feel free to submit issues, fork the repository, and send pull requests. For major changes, please open an issue first to discuss what you would like to change.

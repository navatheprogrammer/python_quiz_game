# Python Quiz Game
A simple quiz game bulit with python

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Features](#features)
- [Project Structure](#project-structure)
- [Requiermets](#requiermets)
- [Installation](#installation)
- [Enviorment Setup](#enviorment-setup)
- [Usage](#usage)
- [Example output](#example-output)
- [Roudmap](#roudmap)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Features
- Quiz System
  - Asks the player muktiaple question
  - Checks the awnsers automatoiclly
  - Calculate the final score
- Result Storage
  - Saves quiz result to a file `result.txt`
- Admin mode  
    - Ask for admin password
    - Checks if the password is correct
    - Keeps the password outside the main python file  
    - Loads the admin pass word from an envoirment file `env`

## Project Structure

``` text
python_game_quiz/
│   .env.example
│   .gitignore
│   app.log
│   main.py
│   question.py
|   requierments.txt
│   readme.md
```

 ### File Description
- `main.py` main file used to run quiz game
- `question.py` it stores questions and awnsers
- `requierments.txt` lists the python package for the project
- `.env.example` shows the enviorment variable needed by the project
- `.gitignore` it tells which files and folders should be ignored
- `redme.md` contains the project documeneation
## Requiermets
before quinning the projects make sure you have:
- `python 3`
- `python--dotenv`
## Installation
1. open terminal in project folder
2. check that python id installed
``` bash
python --vesrion 
```
3. install python packages
``` bash
pip install -r requierments.txt
```


## Enviorment Setup
1. creat e a `.env` from file `.env.example`
``` bash
cp .env.example .env
```

2. open the new `.env` file
3. replace the example value with your password

``` text
  QUIZ_ADMIN_PASSWORD = your pasword
```

4. save this file
> DO NOT COMMIT YOUR `.env` file becasue it may contain privet information
## Usage

1. open a teminal in project folder
2. run the quiz game
``` bash
python main.py
```
3. choose `yes` or `no` for admin mode
4. if you choose `yes` the password from your `.env` file
5. enter your name
6. awnser the questions
7. see your finall score and message
8. you result is saves in `result.txt`
## Example output
``` txt
do you want to open admin mode? yes/no: yes

enter admin password pls: 4321
wrong password

what is your name: nava
welcome

what language are we using?: python
correct

what command starts gitgitinit
wrong

what command shows git statusgit status
correct

your score is 2 out of 3
good job nava

## Roudmap

## Contributing

## License

## Author
# utor-assessment-task

## Installation on you local

# Requirements
Python 3.10

# Without docker
Pull the code to you local and follow these steps

1. Create an env (virtual environment) by running 
python -m venv env

2. Activate the env by running 
source env/bin/activate

2. Install the dependencies by running 
pip install -r requirements.txt

3. Apply migrations by running 
python manage.py makemigrations
python manage.py migrate

4. Run the server bu running
python manage.py runserver

# With docker
Pull the code to you local and follow these steps

1. Make sure you have docker running 
2. Apply this command to build the image
docker build -t <image_name> . e.g: utor-test

3. Run the following command to run a container
docker run -p 8000:8000 <image_name> e.g: utor-test
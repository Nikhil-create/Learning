FROM python:3.13.1

# Create a working directory if its not there and will set this directory as the default for any 
# RUN, CMD, ENTRYPOINT, COPY and ADD instructions that follow it in the Dockerfile.
WORKDIR /application

# This means that all the files will be copied to /application in the container.
COPY requirements.txt /application

# Install the required packages from requirements.txt
RUN pip install -r requirements.txt

COPY . /application

# Expose the port that the application will run on
EXPOSE 5000

VOLUME ["/application/Feedback"]

CMD ["python", "app.py"]
# This is the command that will be run when the container is started



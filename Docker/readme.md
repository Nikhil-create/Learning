### Docker
##### YourTube Video: https://www.youtube.com/watch?v=3c-iBn73dDE
##### Udemy Course: https://www.udemy.com/course/docker-kubernetes-the-practical-guide/learn/lecture/22166758#overview

##### > What are containers
1. Containers are the way to package application in an isolated environment 
   with all the necessary dependencies and configuration. 
2. Portable artifact, easily shared and move around
3. Makes development and deployment more easier.

##### > Where containers live?
Containers live under container repository, many companies have provite repositories to store their container 
and there are public repository for Docker container, where you can browse and find any application container you want

##### > Benfit of containers?
1. Own isolated environment
2. packages with all needed configuration
3. one command to install the app
4. run same app with 2 different versions

##### > What is Docker 
Docker is a container technology (A tool for creating and manage containers)

##### > Cons of using virtual machine instead of docker
1. Redundant duplications, waste of space 
2. Performance can be slow, boot time can be long
3. Reproducing on another computer server is possible may be tricky

##### > What are images
They are also called Templates or Blurprints for container.
It contains the code + required tool/ runtime for the unit of software 

##### > How to create or get images
You can use pre-exist image from Docker Hub
<b>Command</b>: docker run node

##### > How to see all the processes and containers docker created for us
###### Command: 
docker ps -a
<b>To see only running processes: </b> docker ps

##### > How to interact with the image or container
###### Command:
docker run -it node

##### > How to create your custome image
Create a file with name Dockerfile
start with 
1. Mention your runtime environment
2. Setup working directory
3. Copy all your files 
4. Install the dependencies 
5. Expose the port
6. Run your application 

<b>Now we will turn this Dockerfile into the image</b>
<b>Command:</b> docker build .

##### How to stop running container
<b>Get the running processes :</b> docker ps
<b>Stop the process: docker stop:</b> <container-id>

##### How to map the expose port to the system port
<b>Command:</b> docker run -p 80:5000 <Image>
<b>Hint:</b> local port: exposed port

##### Images are read only?
Once the image is created and you make some changes in your application then the changes 
will not get reflected to the image you need to rebuild and create a new image.

<b>Hint:</b> Install the dependencies before running your code.
COPY requirements.txt /application
RUN pip intsall -r requirements.txt
COPY . /application

##### How to get help or list of commands in docker
###### Command:
docker --help


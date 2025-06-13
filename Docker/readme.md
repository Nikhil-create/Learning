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
<b>Stop the process:</b> docker stop <container-id>

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

##### How to stop or restart container
docker ps
docker ps -a
docker ps --help

docker run will create a new container so we need to use the below
command to restart the existing container 

docker start <container-name>

##### How to run the container in detach mode so that we don't get the output
docker run -p 8000:80 -d <image-name>
Hint:
-d stands for detach mode now we don't see the logs

##### How to attach the container again 
docker ps
docker attach <container-name>

##### How to get the logs from container
docker logs <container-name>

##### How to delete the container
docker stop <container_id>
docker rm <containerName1> <containerName2> <containerName3> .. <containerNameN>

##### How to delete the images
docker rmi <imageName1> <imageName2> <imageName3> .. <imageNameN>

docker image prune (delete all unused images)

##### How to delete the container automatically when it stops
docker run -p 8000:80 -d --rm <image-name>

##### How to get image details
docker image inspect <image-name>

##### How to copy file between container and local machine
to container from local machine
docker cp dummy/. <container-name>:/test
to local machine from container
docker cp <container-name>:/test dummy

##### Naming image or container
docker run -p 8000:80 -d --rm --name <new-container-name> <image-name>

##### Rename Image with tag
docker build -t goals:latest

##### get list of images
docker images

##### how to rename existing image
docker tag <existing-image:tag> <new-name:tag>


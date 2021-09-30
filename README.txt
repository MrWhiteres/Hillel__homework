created new docker-container
1. docker build -t name-your-container .    # Create new docker container
2. docker run name-your-container           # start container
3. docker rm $(docker ps -qa)               # del all container

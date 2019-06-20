import docker

"""Please set the password sent in the email before running this script"""

username = "manasshk"
password = ""
tag = ""


client = docker.from_env()
auth_config = {
        'username': username,
        'password': password,
    }
try:
    client.images.build(path="./", tag=username+"/node-testServer-image", rm=True)
    docker_image = client.images.get(username+"/node-testServer-image")

#    Pushing the Image takes some time depending on the speed of internet Connection

    print("start pushing your docker image to docker hub")
    for line in client.images.push(username+'/node-testServer-image', tag=tag, auth_config=auth_config, stream=True):
        print(line)
    print(client.containers.run(image=username+'/node-testServer-image', name='-node-test-container',
                                ports={'8083/tcp': '9000/tcp'}, detach=True))

except docker.errors.ImageNotFound as e:
    print(e)
except docker.errors.APIError as e:
    print(e)
except docker.errors.BuildError as e:
    print(e)
except docker.errors.ContainerError as e:
    print(e)

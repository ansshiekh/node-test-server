import docker

"""Please set the password sent in the email before running this script"""

Username = "manasshk"
Password = ""
Tag = "v1"


client = docker.from_env()
Auth_config = {
        'username': Username,
        'password': Password,
    }
try:
    client.images.build(path="./", tag=Username + "/node-testServer-image", rm=True)
    Docker_image = client.images.get(Username + "/node-testServer-image")

#    Pushing the Image takes some time depending on the speed of internet Connection

    print("start pushing your docker image to docker hub")
    for line in client.images.push(Username + '/node-testServer-image', tag=Tag, auth_config=Auth_config, stream=True):
        print(line)
    print(client.containers.run(image=Username + '/node-testServer-image', name='-node-test-container',
                                ports={'8083/tcp': '9000/tcp'}, detach=True))

except docker.errors.ImageNotFound as error:
    print(error)
except docker.errors.APIError as error:
    print(error)
except docker.errors.BuildError as error:
    print(error)
except docker.errors.ContainerError as error:
    print(error)

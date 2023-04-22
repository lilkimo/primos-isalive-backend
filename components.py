import docker

def getContainers():
    client = docker.from_env()
    containers = client.containers.list(all=True)

    containers_list = []
    for container in containers:
        data = {
            'id': container.id,
            'name': container.name,
            'image': container.attrs['Config']['Image'],
            'status': container.status,
            'created_at': container.attrs['Created'],
            'ports': container.attrs['HostConfig']['PortBindings'],
            'labels': container.labels,
            'exit_code': container.attrs['State']['ExitCode'],
            'exit_time': container.attrs['State']['FinishedAt']
        }
        containers_list.append(data)

    return containers_list


def getContainerById(id: str):
    client = docker.from_env()
    container = client.containers.get(id)
    return {
        'id': container.id,
        'name': container.name,
        'image': container.attrs['Config']['Image'],
        'status': container.status,
        'created_at': container.attrs['Created'],
        'ports': container.attrs['HostConfig']['PortBindings'],
        'labels': container.labels,
        'exit_code': container.attrs['State']['ExitCode'],
        'exit_time': container.attrs['State']['FinishedAt']
    }

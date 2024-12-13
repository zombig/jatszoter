import docker
from docker import errors as docker_errors
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()
docker_client = docker.from_env()

# pylint: disable=too-few-public-methods


class CreateRequest(BaseModel):
    """
    Create Request Class.
    """
    type: str
    image: str
    token: str


@router.post('/create')
async def create_container(request: CreateRequest):

    if request.type != 'docker':
        raise HTTPException(
            status_code=400,
            detail="Only 'docker' type is supported",
        )

    try:
        container = docker_client.containers.run(
            request.image,
            detach=True,
            ports={'22/tcp': None},
        )

        container.reload()
        ssh_port = container.attrs['NetworkSettings']['Ports']['22/tcp'][0]['HostPort']

        web_ssh_url = f"http://localhost:8080/?port={ssh_port}"

        return {'message': 'Container created', 'web_ssh_url': web_ssh_url}

    except docker_errors.ImageNotFound:
        # pylint: disable=raise-missing-from
        raise HTTPException(
            status_code=404, detail='Docker image not found',
        )

    except Exception as error:
        # pylint: disable=raise-missing-from
        raise HTTPException(status_code=500, detail=str(error))

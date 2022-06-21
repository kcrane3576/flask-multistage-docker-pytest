# python-asyncio
simple flask app primer with logging and asyncio

### Docker
AWARENESS: If you want to see output from docker build, set below
```shell
export DOCKER_BUILDKIT=0
```
```shell
docker-compose down -v && \
    docker system prune -af && \
    docker-compose up --build
```
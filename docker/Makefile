.PHONY: clean docker-clean  \
        remove-image remove-container remove-volume \
		    docker-update \
        image run

CONTAINER_NAME=container-name
IMAGE_NAME=image_name

up:
	docker-compose -d up
down:
	docker-compose down

start:
	docker start $(CONTAINER_NAME)

stop:
	docker stop $(CONTAINER_NAME)

restart:
	docker restart $(CONTAINER_NAME)

inspect:
	docker inspect $(CONTAINER_NAME)

logs:
	docker logs $(CONTAINER_NAME)

clean:
	echo "clean"

remove-image:
	docker rmi $(IMAGE_NAME)

remove-container:
	docker rm $(CONTAINER_NAME)

remove-volumes:
	docker volume prune

rebuild: stop remove-container remove-image remove-volumes image


run:
	echo "Implement me in local Makefile"

docker-clean: clean
	docker-compose rm
	docker volume prune

docker-update:
	docker-compose pull

image: clean
	docker build -t $(IMAGE_NAME):latest .

master-clean-volumes:
	docker volume rm $(docker volume ls -qf dangling=true)
	docker volume ls -qf dangling=true | xargs -r docker volume rm

master-clean-networks:
	docker network ls
	docker network ls | grep "bridge"
	docker network rm $(docker network ls | grep "bridge" | awk '/ / { print $1 }')

master-clean-images:
	docker rmi $(docker images --filter "dangling=true" -q --no-trunc)
	docker images | grep "none"
	docker rmi $(docker images | grep "none" | awk '/ / { print $3 }')

master-clean-containers:
	docker ps
	docker ps -a
	docker rm $(docker ps -qa --no-trunc --filter "status=exited")

console:
	docker exec -it $(CONTAINER_NAME) /bin/bash

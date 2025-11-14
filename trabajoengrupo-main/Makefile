APP_NAME=manchas
IMAGE=your-dockerhub-user/$(APP_NAME)

build:
	docker build -t $(IMAGE) .

push:
	docker push $(IMAGE)

run:
	docker run -p 8080:8080 $(IMAGE)

stack-apply:
	docker stack deploy -c stack.yml manchas

stack-delete:
	docker stack rm manchas
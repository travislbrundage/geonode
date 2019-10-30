# Set variables to pass
DOCKER_HOST := $(DOCKER_HOST)
DOCKER_HOST_IP := `docker run --net=host codenvy/che-ip:nightly`

start:
	docker-compose -f docker-compose.async.yml -f docker-compose.development.yml up -d

start_logs:
	docker-compose -f docker-compose.async.yml -f docker-compose.development.yml up

stop:
	docker-compose -f docker-compose.async.yml -f docker-compose.development.yml down

logs:
	docker-compose logs --follow

ssh:
	docker exec -it django4geonode /bin/bash

restart: stop start

auto-up:
	# bring up the services with proper environment variables
	unset DOCKERHOST; \
	export DOCKERHOST=$(DOCKER_HOST); \
	echo Docker daemon is running at the following address $$DOCKERHOST; \
	unset GEONODE_LB_HOST_IP; \
	export GEONODE_LB_HOST_IP=$(DOCKER_HOST_IP); \
	echo GeoNode will be available at the following address http://$$GEONODE_LB_HOST_IP; \
	echo If you want to run it on localhost then remember to add this line "localhost $$GEONODE_LB_HOST_IP" to /etc/hosts; \
	docker-compose up -d --build

up:
	docker-compose up -d

build:
	docker-compose build django
	docker-compose build celery

sync: up
	# set up the database tables
	docker-compose exec django django-admin.py migrate --noinput
	docker-compose exec django django-admin.py loaddata sample_admin
	docker-compose exec django django-admin.py loaddata geonode/base/fixtures/default_oauth_apps_docker.json
	docker-compose exec django django-admin.py loaddata geonode/base/fixtures/initial_data.json

migrate:
	django-admin.py migrate --noinput

migrate_setup: migrate
	django-admin.py loaddata sample_admin

wait:
	sleep 5

down:
	docker-compose down

pull:
	docker-compose pull

reset: down up wait sync

hardreset: pull build reset

develop: pull build up sync

start_test:
	docker-compose -f docker-compose.async.yml -f docker-compose.development.yml up -d
	unset DJANGO_SETTINGS_MODULE; \
	export DJANGO_SETTINGS_MODULE='geonode.test_settings';

smoke_test: start
	coverage run --branch --source=geonode manage.py test geonode.tests.smoke --noinput --failfast

unit_test: start
	coverage run --branch --source=geonode manage.py test geonode.people.tests geonode.base.tests geonode.layers.tests geonode.maps.tests geonode.proxy.tests geonode.security.tests geonode.social.tests geonode.catalogue.tests geonode.documents.tests geonode.api.tests geonode.groups.tests geonode.services.tests geonode.geoserver.tests geonode.upload.tests --noinput --failfast

# TODO: Need proper setup for integration tests
integration_test: start
	coverage run --branch --source=geonode manage.py test geonode.monitoring.tests.integration geonode.upload.tests.integration geonode.tests.integration

test: smoke_test unit_test

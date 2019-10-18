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

build:
	docker-compose build django
	docker-compose build celery

migrate: start
	docker-compose exec django django-admin.py migrate --noinput --settings=$$DJANGO_SETTINGS_MODULE

migrate_setup: migrate
	docker-compose exec django django-admin.py loaddata sample_admin --settings=$$DJANGO_SETTINGS_MODULE

sync_setup: migrate_setup
	# TODO: setup environment variables here
	unset DATABASE_URL; \
	export DATABASE_URL=$(DATABASE_URL); \
	unset GEODATABASE_URL; \
	export GEODATABASE_URL=$(GEODATABASE_URL); \

sync: migrate_setup
	# set up the database tables
	# TODO: The default_oauth_apps_docker fixture is not working
	docker-compose exec django django-admin.py loaddata --settings=geonode.settings geonode/base/fixtures/default_oauth_apps_docker.json
	docker-compose exec django django-admin.py loaddata --settings=geonode.settings geonode/base/fixtures/initial_data.json

reset: stop start sync

pull:
	docker-compose -f docker-compose.async.yml -f docker-compose.development.yml pull

hardreset: pull build reset

develop: pull build start sync

# TODO: Separate unit and integration tests into their own commands
smoke_test: start
	coverage run --branch --source=geonode manage.py test geonode.tests.smoke --noinput --verbosity=1 --failfast

unit_test: start
	coverage run --branch --source=geonode manage.py test geonode.people.tests geonode.base.tests geonode.layers.tests geonode.maps.tests geonode.proxy.tests geonode.security.tests geonode.social.tests geonode.catalogue.tests geonode.documents.tests geonode.api.tests geonode.groups.tests geonode.services.tests geonode.geoserver.tests geonode.upload.tests --noinput --failfast

# TODO: Need proper setup for these tests
integration_test: start
	coverage run --branch --source=geonode manage.py test geonode.monitoring.tests.integration geonode.upload.tests.integration geonode.tests.integration

test: smoke_test unit_test integration_test


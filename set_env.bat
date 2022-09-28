set FSCRAWLER_VERSION=2.10-SNAPSHOT
set FSCRAWLER_PORT=8080

set ELASTIC_PASSWORD=changeme

set KIBANA_PASSWORD=changeme

set STACK_VERSION=8.4.1

set CLUSTER_NAME=docker-cluster

set LICENSE=basic

set ES_PORT=9200

set KIBANA_PORT=5601

set ENTERPRISE_SEARCH_PORT=3002
set ENCRYPTION_KEYS=BACD

set MEM_LIMIT=1073741824

set COMPOSE_PROJECT_NAME=fscrawler
set PWD=D:/Project/elasticsearch_with_kibana
wsl -d docker-desktop
@REM sysctl -w vm.max_map_count=262144
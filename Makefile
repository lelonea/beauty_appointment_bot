
help: # Show this help
	@echo "Usage: make [target]"
	@echo "Targets:"
	@echo "  build: build project"
	@echo "  run: run project"
	@echo "  clean: clean project"


clean: # Clean project
	docker compose -f docker-compose.proxy.yml -f docker-compose.yml down -v --remove-orphans

build: # Build project
	docker network create appointment-network || exit 0
	docker compose build --no-cache appointment-tg-bot appointment-db db-initializer

run_proxy: # Run proxy
	docker compose -f docker-compose.proxy.yml stop appointment-proxy || exit 0
	docker compose -f docker-compose.proxy.yml up appointment-proxy -d
	sleep 5
	sed -i '' -e "s#WEBHOOK_HOST=.*#WEBHOOK_HOST=$$(docker compose -f docker-compose.proxy.yml logs --tail 5 appointment-proxy | grep -oE 'https.*')#g" .env

run: # Run bot
	docker compose up appointment-tg-bot appointment-db db-initializer

run_with_proxy: run_proxy run # Run bot with proxy

#!/bin/bash

. ./env.sh

if [ ! -z $unix ]; then
	args="--uds $unix"
else
	args="--host $host --port $port"
fi

if [ ! -z $1 ] && [ $1 = "--dev" ]; then
	python3.11 -m uvicorn $args --reload main.asgi:app
else
	python3.11 -m uvicorn \
	--log-level $loglevel \
	--no-access-logs \
	--no-date-header \
	--no-proxy-headers \
	--no-server-header \
	--workers $workers \
	$args \
	main.asgi:app
fi

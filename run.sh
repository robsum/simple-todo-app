#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

#cd ${SCRIPT_DIR}/frontend && docker build -t todo-frontend .
cd ${SCRIPT_DIR}/backend && docker build -t todo-backend .
cd ${SCRIPT_DIR}/nginx && docker build -t todo-nginx .
cd ${SCRIPT_DIR} && docker-compose up


#!/bin/bash

URL=$(docker compose logs | grep "http://127.0.0.1:8888/lab?token=" | awk '{print $NF}' | tail -n 1)

if [[ ! -z "$URL" ]]; then
    echo "Opening Jupyter Lab URL: $URL"
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        xdg-open "$URL"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        open "$URL"
    else
        echo "Platform not supported. Please open the URL manually."
    fi
else
    echo "Jupyter Lab URL was not found."
fi

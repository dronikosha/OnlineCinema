# Django Project for Multiple People to Watch Movies Simultaneously

This Django project is designed to allow multiple people to watch movies at the same time using ASGI, Channels, Redis, Daphne, and Docker. It uses Django Channels as a WebSocket framework to enable real-time communication between the server and the client.

## Setup

```bash

docker-compose  up  --build

```

This command will download the required Docker images, build the Django project and start the Docker container.

Open your browser and navigate to http://localhost:8000/ to access the application.

## Usage

Open the application in multiple browser windows or tabs.

Play the video file in one window, and you should see the video playing in all the other windows as well.

Pause the video in one window, and you should see the video paused in all the other windows as well.

## Configuration

The Django Channels layer is configured to use Redis as a backing store for the WebSocket connections. The Redis server is configured in the docker-compose.yml file.

The Dockerfile contains the command to start the ASGI server using Daphne, as well as the command to start the Django Channels layer using daphne.

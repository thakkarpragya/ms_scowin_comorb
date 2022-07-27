## Run in local system

#### Pre-requisites

> `Rabbitmq` service should be up and running.

#### Steps to reproduce:

Clone the repository and install the required packages using below commands.

```sh
git clone git@github.com:thakkarpragya/ms_scowin_comorb.git
cd ms_scowin_comorb
```

Check if pip is installed

```sh
pip --version
```

Install all the required packages:

```sh
pip install -r requirements.txt
```

Start the server

```sh
python manage.py runserver <port>
```

In another terminal, start the consuming service.
```sh
python consumer.py
```

Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:<port>
```

## Run as docker container

Build the Dockerfile

```
DOCKER_BUILDKIT=0 docker build . -t <image-name> --no-cache
```

Run the image
```
docker run -d -p 8086:8086 <image-name>
```

Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:8086
```

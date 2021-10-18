## echo server for seldon logger cloud events

```
pip3.8 install -r requirements.txt --user
python3.8 handler.py
```

```
# test using a fake event
curl -i -d@testevent.json localhost:5000
```

Wire to `Seldon Deployment`

```
logger:
  url: http://mylogging-endpoint
  mode: all
```

## podman image

Build image
```
podman build -f Dockerfile -t quay.io/eformat/seldon-echo-server:latest
```

Run/test image locally
```
podman run --name seldon-echo-server -d -p 8080:8080 quay.io/eformat/seldon-echo-server:latest
podman logs -f seldon-echo-server
curl -i -d@testevent.json localhost:8080
```

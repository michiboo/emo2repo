RTSP relay server
===


## quickstart

To enable docker
```
sudo systemctl start docker
```

```
docker build -t rtspserver .
docker run  -i --name example -p 1234:1234 -t rtspserver
 ./build/rtsprelay -p 1234 -i `hostname -I | awk '{print $1}'`
```

After these commands you should see a RTSP server is running and its IP address is displayed.

# Emo2Repo
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
![Emo2Repo logo](https://i.imgur.com/ypC3rVf.png)

Emo2Repo is a application that match your emotion with a github repo! (Repo has emotion too!)


## Quick Start (locally)

### 1. start streaming server

Enable docker:
```
sudo systemctl start docker
```

Build docker image:
```
docker build -t rtspserver .
```
Create & run container:
```
docker run  -i --name example --network host -t rtspserver
```
Start the server:
```
./build/rtsprelay -p 1234 -i `hostname -I | awk '{print $1}'`
```
### 2. Start backend server

Install dependencies:
`pip install -r requirements.txt`
<br>
<br>
Start server:
```python app.py```

### 3. Start Android App
Before building APP in Android studio you should make sure the IP address of streaming server & backend server are correct.

## Architecture

![Arch](https://i.imgur.com/qOrh7yD.png)

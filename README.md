# Emo2Repo

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
docker run  -i --name example -p 1234:1234 -t rtspserver
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

### 3. Start Andriod App 
Before building APP in Andriod studio you should make sure the IP address of streaming server & backend server are correct.

## Architecture

![Arch](https://i.imgur.com/qOrh7yD.png)

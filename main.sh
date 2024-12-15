#!/bin/bash

mkdir tempdir
mkdir tempdir/templates
mkdir tempdir/static

cp main.py tempdir/.
cp -r templates/* tempdir/templates/.
cp -r static/* tempdir/static/.

echo "FROM python" >> tempdir/Dockerfile
echo "RUN pip install flask" >> tempdir/Dockerfile
echo "RUN pip install requests" >> tempdir/Dockerfile
echo "COPY  ./static /home/BRA9.1_Team65/static/" >> tempdir/Dockerfile
echo "COPY  ./templates /home/BRA9.1_Team65/templates/" >> tempdir/Dockerfile
echo "COPY  main.py /home/BRA9.1_Team65/" >> tempdir/Dockerfile
echo "EXPOSE 5000" >> tempdir/Dockerfile
echo "CMD python3 /home/BRA9.1_Team65/main.py" >> tempdir/Dockerfile

cd tempdir

docker build -t webapp .
docker run -t -d -p 5000:5000 --name webrun webapp
docker ps -a
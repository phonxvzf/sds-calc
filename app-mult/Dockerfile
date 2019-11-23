FROM arm32v7/python:3

WORKDIR /usr/src/app

COPY . .

RUN pip install flask requests

ENV PORT 5003

EXPOSE 5003

CMD [ "python", "app-mult.py" ]

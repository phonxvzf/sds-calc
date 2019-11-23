FROM arm32v7/python:3

WORKDIR /usr/src/app

COPY . .

RUN pip install flask

ENV PORT 5004

EXPOSE 5004

CMD [ "python", "app-div.py" ]

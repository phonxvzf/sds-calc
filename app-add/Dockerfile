FROM arm32v7/python:3

WORKDIR /usr/src/app

COPY . .

RUN pip install flask

ENV PORT 5001

EXPOSE 5001

CMD [ "python", "app-add.py" ]

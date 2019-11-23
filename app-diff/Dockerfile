FROM arm32v7/python:3

WORKDIR /usr/src/app

COPY . .

RUN pip install flask requests

ENV PORT 5002

EXPOSE 5002

CMD [ "python", "app-diff.py" ]

FROM python:3.12-slim

COPY ./ /home/app

WORKDIR /home/app

RUN pip3.12 install --upgrade pip
RUN pip3.12 install grpcio==1.62.1
RUN pip3.12 install grpcio-tools==1.62.1
RUN python -m venv dev
RUN . dev/bin/activate

EXPOSE 5000

CMD ["python3.12", "-u", "main.py"]

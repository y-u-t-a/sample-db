# コンテナを起動したままにするために ubuntu イメージを使用する
FROM ubuntu:20.10
RUN apt-get update && apt-get install -y python3.9 python3-distutils curl
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" \
    && python3 get-pip.py
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
# コンテナを起動したままにするために ubuntu イメージを使用する
FROM ubuntu:20.10
RUN apt-get update \
    && apt-get install -y \
        python3.9 \
        python3-distutils \
        curl \
        less
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" \
    && python3 get-pip.py
# less の charset を UTF-8 にする
ENV LESSCHARSET utf-8
WORKDIR /script/python
COPY . .
RUN pip install -r requirements.txt
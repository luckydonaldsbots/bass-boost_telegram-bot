FROM luckydonald/telegram-bot:python3.6-stretch

RUN apt-get update -y \
    # omitting libavcodec-extra-53
    && apt-get install  -y libav-tools \
    && rm -rfv /var/lib/apt/lists/*


COPY $FOLDER/requirements.txt   /config/
RUN pip install --no-cache-dir -r /config/requirements.txt

COPY $FOLDER/code /app
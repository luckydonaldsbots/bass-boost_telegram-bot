FROM luckydonald/telegram-bot:python3.6-stretch-onbuild

RUN apt-get update -y \
    # omitting libavcodec-extra-53
    && apt-get install  -y libav-tools \
    && rm -rfv /var/lib/apt/lists/*

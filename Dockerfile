FROM python:3.9

WORKDIR /tmp/islands_counter
COPY src ./src
COPY tests ./tests
COPY setup.py ./
COPY count_islands.sh ./
COPY requirements.txt ./

RUN pip3 install -r requirements.txt
RUN pip3 install .

RUN apt-get update
RUN apt-get install -y zsh
RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true

CMD [ "sh" ]

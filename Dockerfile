FROM python:3.7.9

RUN apt-get update
RUN apt-get install -y supervisor

RUN mkdir -p /FIC_Algo_task

WORKDIR /FIC_Algo_task

ADD . /FIC_Algo_task
ADD supervisor.conf /etc/supervisor/conf.d/

RUN pip install -r /FIC_Algo_task/requirements.txt

ENV PYTHONPATH /FIC_Algo_task
RUN mkdir -p /FIC_Algo_task/logs

CMD /usr/bin/supervisord -n -c /etc/supervisor/supervisord.conf

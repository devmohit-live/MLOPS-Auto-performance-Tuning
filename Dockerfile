FROM centos
RUN yum update -y
RUN yum install python36 -y
RUN yum install python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install tensorflow==2.0.0
RUN pip3 install keras
COPY train.py /root/project
COPY iter /root/project
COPY accuracy /root/project
CMD python3 /root/train.py

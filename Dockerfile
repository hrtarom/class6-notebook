
FROM ubuntu:latest
RUN apt-get update \
    && apt-get install -y python3-pip \
    && pip3 install --upgrade pip

RUN pip3 install numpy pandas matplotlib seaborn plotly sklearn
COPY class6.py .
COPY 3D+pie.py .
COPY multifigplot.py .

ADD . /plots/

CMD ["python3","-u","3D+pie.py"]
CMD ["python3","-u","multifigplot.py"]






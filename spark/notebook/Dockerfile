FROM datamechanics/spark:3.2.1-latest

USER root

WORKDIR /opt/spark

RUN pip install --upgrade pip

COPY  requirements.txt .
RUN pip3 install -r requirements.txt

CMD ["jupyter-lab", "--allow-root", "--no-browser", "--ip=0.0.0.0"]

FROM python
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
RUN chmod +x time-call.sh
RUN ./time-call.sh

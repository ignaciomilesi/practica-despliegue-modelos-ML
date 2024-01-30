FROM python:3.11.3

WORKDIR /app

COPY api/ ./api

COPY model/model.pkl ./model/model.pkl

COPY initializer.sh .

RUN pip install -U pip && pip install -r ./api/requirements.txt

RUN chmod +x initializer.sh

EXPOSE 8000

ENTRYPOINT ["./initializer.sh"]
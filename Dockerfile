FROM python:3
EXPOSE 5000
COPY . .
ENTRYPOINT ["/docker-entrypoint.sh"]

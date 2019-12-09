FROM mysql
ENV MYSQL_DATABASE mysql
ENV MYSQL_ROOT_PASSWORD gpsc9926

COPY data /docker-entrypoint-initdb.d/
COPY config/my.cnf /etc/mysql

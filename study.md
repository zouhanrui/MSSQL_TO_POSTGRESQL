# MySQL server in Docker

* Instead of installing mysql server locally, use docker image to spin up mysql db
> MySQL docker image:
> 
> https://hub.docker.com/_/mysql
> 
> docker run --name mydbtest-mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password -d mysql
> 

* Connect via DataGrip, use query console for sql language: create db and table

* Download sample database from mysql tutorial: https://www.mysqltutorial.org/mysql-sample-database.aspx

* Python users mysql.connector to connect the mysql db

# PostgreSQL server in Docker
* PostgreSQL docker image: https://hub.docker.com/_/postgres
> $ docker run --name my-postgres -p 5432:5432 -e POSTGRES_PASSWORD=password -d postgres
> 
> create user in postgres 
> 
> 
> 
# Microsoft SQL Server in Docker
* Microsoft SQL Server docker image: https://hub.docker.com/_/microsoft-mssql-server
* Start a mssql-server instance for SQL Server 2022, which is currently in public preview.
> docker run --name MicroSoft-msSQL -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=Password0" -p 1433:1433 -d mcr.microsoft.com/mssql/server:2022-latest


USE [master]
GO
CREATE LOGIN [hanrui] WITH PASSWORD=N'password', DEFAULT_DATABASE=[AdventureWorksDW2019], CHECK_EXPIRATION=OFF, CHECK_POLICY=OFF
GO
USE [AdventureWorksDW2019]
GO
CREATE USER [hanrui] FOR LOGIN [hanrui]
GO
USE [AdventureWorksDW2019]
GO
ALTER ROLE [db_datareader] ADD MEMBER [hanrui]
GO
use [master]
GO
GRANT CONNECT SQL TO [hanrui]
GO
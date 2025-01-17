USE [storehouse]
GO
/****** Object:  StoredProcedure [dbo].[init1]    Script Date: 2019/11/20 15:39:55 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
ALTER PROCEDURE [dbo].[init1]

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	exec clear1

	--init user

	declare @username nchar(100)
	set @username='user'

	DECLARE @T INT
	SET @T = 1
	WHILE @T<4
		BEGIN
			declare @name nchar(100)
			set @name = trim(rtrim(@username)+ltrim(@T))
			insert into [user] values (@name, @name);
			set @T+=1
		END

	--init cargo

	insert into [cargo] 
	values('苹果', 5, 'kg', 'A'),
	('梨', 50, 'kg', 'B'),
	('西瓜', 50, 'kg', 'C'),
	('桃子', 59, 'kg', 'D'),
	('哈密瓜', 56, 'kg', 'E'),
	('香蕉', 51, 'kg', 'F'),
	('葡萄', 52, 'kg', 'G');
	
	--init input

END

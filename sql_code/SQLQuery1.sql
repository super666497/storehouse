USE [storehouse]
GO
/****** Object:  StoredProcedure [dbo].[init1]    Script Date: 2019/11/20 14:21:30 ******/
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

	--init user
	declare @username nchar(100)
	set @username='user'

	DECLARE @T INT
	SET @T = 1
	WHILE @T<4
		BEGIN
			declare @name nchar(100)
			set @name = trim(rtrim(@username)+ltrim(@T))
			print @name
			set @T+=1
		END
  
END

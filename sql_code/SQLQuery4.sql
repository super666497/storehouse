-- ================================================
-- Template generated from Template Explorer using:
-- Create Procedure (New Menu).SQL
--
-- Use the Specify Values for Template Parameters 
-- command (Ctrl-Shift-M) to fill in the parameter 
-- values below.
--
-- This block of comments will not be included in
-- the definition of the procedure.
-- ================================================
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE clear

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    --init user
	delete [user]
	DBCC CHECKIDENT ("user", RESEED, 0)
	--init cargo
	delete [cargo]
	DBCC CHECKIDENT ("cargo", RESEED, 0)
	--init input
	delete [input]
	DBCC CHECKIDENT ("input", RESEED, 0)
	--init output
	delete [output]
	DBCC CHECKIDENT ("output", RESEED, 0)
END
GO

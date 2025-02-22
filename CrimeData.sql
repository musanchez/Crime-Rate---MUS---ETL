USE Crime;

-- Verificar si la tabla CrimeData existe
IF OBJECT_ID('CrimeData', 'U') IS NOT NULL
BEGIN
    -- Si existe, dropear la tabla
    DROP TABLE CrimeData;
END

CREATE TABLE CrimeData (
	[DR_NO] [nvarchar](100) NOT NULL,
	[Date_Rptd] [date] NULL,
	[DATE_OCC] [date] NULL,
	[TIME_OCC] INT NULL,
	[AREA] [tinyint] NULL,
	[AREA_NAME] [nvarchar](50) NULL,
	[Rpt_Dist_No] [smallint] NULL,
	[Part_1_2] [tinyint] NULL,
	[Crm_Cd] [smallint] NULL,
	[Crm_Cd_Desc] [nvarchar](100) NULL,
	[Mocodes] [nvarchar](50) NULL,
	[Vict_Age] [smallint] NULL,
	[Vict_Sex] [nvarchar](50) NULL,
	[Vict_Descent] [nvarchar](50) NULL,
	[Premis_Cd] [smallint] NULL,
	[Premis_Desc] [nvarchar](100) NULL,
	[Weapon_Used_Cd] [smallint] NULL,
	[Weapon_Desc] [nvarchar](100) NULL,
	[Status] [nvarchar](100) NULL,
	[LOCATION] [nvarchar](max) NULL,
	[Status_Desc] [nvarchar](max) NULL,
	[Cross_Street] [nvarchar](max) NULL,
	[LAT] decimal(8,4) NULL,
	[LON] decimal(8, 4) NULL
)
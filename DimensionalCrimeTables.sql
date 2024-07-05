CREATE TABLE DimVictSex (
    Vict_Sex_Id SMALLINT PRIMARY KEY,
    Vict_Sex NVARCHAR(50)
);


CREATE TABLE DimVictDescent (
    Vict_Descent_Id SMALLINT PRIMARY KEY,
    Vict_Descent NVARCHAR(50)
);


CREATE TABLE DimDateRptd (
    Date_Rptd_Id INT PRIMARY KEY,
    Date_Rptd DATE
);


CREATE TABLE DimArea (
    AREA TINYINT PRIMARY KEY,
    AREA_NAME NVARCHAR(50)
);

CREATE TABLE DimWeapon (
    Weapon_Used_Cd SMALLINT PRIMARY KEY,
    Weapon_Desc NVARCHAR(100)
);

CREATE TABLE DimStatus (
    Status NVARCHAR(100) PRIMARY KEY,
    Status_Desc NVARCHAR(MAX)
);

CREATE TABLE DimPremis (
    Premis_Cd SMALLINT PRIMARY KEY,
    Premis_Desc NVARCHAR(100)
);

CREATE TABLE FactCrime (
    DR_NO VARCHAR(100) PRIMARY KEY,
    Date_Rptd_Id INT,
    DATE_OCC DATE,
    TIME_OCC INT,
    AREA TINYINT,
    Rpt_Dist_No SMALLINT,
    Part_1_2 TINYINT,
    Crm_Cd SMALLINT,
    Mocodes VARCHAR(50),
    Vict_Age SMALLINT,
    Vict_Sex_Id SMALLINT,
    Vict_Descent_Id SMALLINT,
    Premis_Cd SMALLINT,
    Weapon_Used_Cd SMALLINT,
    Status NVARCHAR(100),
    LOCATION NVARCHAR(MAX),
    Cross_Street NVARCHAR(MAX),
    LAT DECIMAL(8,4),
    LON DECIMAL(8,4),
    CONSTRAINT FK_FactCrime_DimDateRptd FOREIGN KEY (Date_Rptd_Id) REFERENCES DimDateRptd(Date_Rptd_Id),
    CONSTRAINT FK_FactCrime_DimArea FOREIGN KEY (AREA) REFERENCES DimArea(AREA),
    CONSTRAINT FK_FactCrime_DimVictSex FOREIGN KEY (Vict_Sex_Id) REFERENCES DimVictSex(Vict_Sex_Id),
    CONSTRAINT FK_FactCrime_DimVictDescent FOREIGN KEY (Vict_Descent_Id) REFERENCES DimVictDescent(Vict_Descent_Id),
    CONSTRAINT FK_FactCrime_DimWeapon FOREIGN KEY (Weapon_Used_Cd) REFERENCES DimWeapon(Weapon_Used_Cd),
    CONSTRAINT FK_FactCrime_DimStatus FOREIGN KEY (Status) REFERENCES DimStatus(Status),
    CONSTRAINT FK_FactCrime_DimPremis FOREIGN KEY (Premis_Cd) REFERENCES DimPremis(Premis_Cd)
);

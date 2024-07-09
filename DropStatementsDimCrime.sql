IF OBJECT_ID('FactCrime', 'U') IS NOT NULL
    DROP TABLE FactCrime;

IF OBJECT_ID('DimDateRptd', 'U') IS NOT NULL
    DROP TABLE DimDateRptd;

IF OBJECT_ID('DimArea', 'U') IS NOT NULL
    DROP TABLE DimArea;

IF OBJECT_ID('DimVictSex', 'U') IS NOT NULL
    DROP TABLE DimVictSex;

IF OBJECT_ID('DimVictDescent', 'U') IS NOT NULL
    DROP TABLE DimVictDescent;

IF OBJECT_ID('DimWeapon', 'U') IS NOT NULL
    DROP TABLE DimWeapon;

IF OBJECT_ID('DimStatus', 'U') IS NOT NULL
    DROP TABLE DimStatus;

IF OBJECT_ID('DimPremis', 'U') IS NOT NULL
    DROP TABLE DimPremis;

IF OBJECT_ID('DimCrime', 'U') IS NOT NULL
    DROP TABLE DimCrime;
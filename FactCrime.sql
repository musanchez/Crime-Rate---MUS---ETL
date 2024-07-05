SELECT 
    cd.DR_NO,
    dr.Date_Rptd_Id,
    cd.DATE_OCC,
    cd.TIME_OCC,
    cd.AREA,
    cd.Rpt_Dist_No,
    cd.Part_1_2,
    cd.Crm_Cd,
    cd.Mocodes,
    cd.Vict_Age,
    vs.Vict_Sex_Id,
    vd.Vict_Descent_Id,
    cd.Premis_Cd,
    cd.Weapon_Used_Cd,
    cd.Status,
    cd.LOCATION,
    cd.Cross_Street,
    cd.LAT,
    cd.LON
FROM Crime.dbo.CrimeData cd
LEFT JOIN DimensionalCrime.dbo.DimDateRptd dr ON cd.Date_Rptd = dr.Date_Rptd
LEFT JOIN DimensionalCrime.dbo.DimVictSex vs ON cd.Vict_Sex = vs.Vict_Sex
LEFT JOIN DimensionalCrime.dbo.DimVictDescent vd ON cd.Vict_Descent = vd.Vict_Descent;
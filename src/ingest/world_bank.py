import wbgapi as wb
import pandas as pd
from pathlib import Path
from datetime import datetime as dt

# folder for all raw source files
RAW_DIR = Path("data/raw")

# World Bank indicator codes for Cameroon 
INDICATORS = {
    # --- Macroeconomic ---
    "gdp_current_usd":       "NY.GDP.MKTP.CD",        # total size of the economy in current US dollars
    "gdp_per_capita":        "NY.GDP.PCAP.CD",        # GDP divided by population
    "inflation_cpi":         "FP.CPI.TOTL.ZG",        # annual % change in consumer prices
    "exports_pct_gdp":       "NE.EXP.GNFS.ZS",        # exports of goods and services as % of GDP
    "fdi_inflows_pct_gdp":   "BX.KLT.DINV.WD.GD.ZS",  # foreign direct investment net inflows as % of GDP
    "external_debt_pct_gni": "DT.DOD.DECT.GN.ZS",     # total external debt stock as % of GNI
    "gni_per_capita":        "NY.GNP.PCAP.CD",        # World Bank's income classification metric; GNI vs GDP gap reveals remittance flows

    # --- Demographics ---
    "population_total":      "SP.POP.TOTL",        # total population count
    "population_urban_pct":  "SP.URB.TOTL.IN.ZS",  # urban population as % of total
    "population_rural":      "SP.RUR.TOTL",        # rural population absolute count

    # --- Health ---
    "life_expectancy":       "SP.DYN.LE00.IN",   # life expectancy at birth in years
    "mortality_under5":      "SH.DYN.MORT",      # deaths per 1,000 live births before age 5
    "maternal_mortality":    "SH.STA.MMRT",      # maternal deaths per 100,000 live births
    "hiv_prevalence":        "SH.DYN.AIDS.ZS",   # % of population ages 15–49 living with HIV
    "tb_incidence":          "SH.TBS.INCD",      # TB cases per 100,000 people
    "water_access_pct":      "SH.H2O.BASW.ZS",   # % using at least basic drinking water services
    "sanitation_access_pct": "SH.STA.BASS.ZS",   # % using at least basic sanitation services

    # --- Education ---
    "enrollment_primary_net":   "SE.PRM.NENR",      # net enrollment rate to primary school (% of school-age children)
    "enrollment_secondary_net": "SE.SEC.NENR",      # net enrollment rate to secondary school
    "literacy_adult":           "SE.ADT.LITR.ZS",   # adult literacy rate (% ages 15+)
    "literacy_youth":           "SE.ADT.1524.LT.ZS",# youth literacy rate (% ages 15–24)
    "gender_parity_school":     "SE.ENR.PRSC.FM.ZS",# ratio of female to male enrollment

    # --- Infrastructure & Energy ---
    "electricity_access_pct":       "EG.ELC.ACCS.ZS",    # % of population with access to electricity
    "electricity_access_rural_pct": "EG.ELC.ACCS.RU.ZS", # rural electricity access
    "renewable_energy_pct":         "EG.FEC.RNEW.ZS",    # renewables as % of total final energy consumption

    # --- Agriculture & Environment ---
    "cereal_yield_kg_per_ha": "AG.YLD.CREL.KG",       # kg of cereal produced per hectare
    "forest_area_pct":        "AG.LND.FRST.ZS",       # forest as % of land area
    "co2_per_capita":         "EN.GHG.CO2.PC.CE.AR5", # CO2 emissions per person in tonnes
    "air_pollution_pm25":     "EN.ATM.PM25.MC.M3",    # mean annual PM2.5 concentration in urban areas

    # --- Gender ---
    "female_labor_participation": "SL.TLF.CACT.FE.ZS", # female labor force participation rate (% of female ages 15+)
    "women_in_parliament_pct":    "SG.GEN.PARL.ZS",    # % of parliamentary seats held by women
}


def pull_world_bank(country="CMR", start_year=1990, end_year=None):  # CMR is the World Bank's ISO code for Cameroon; end_year resolves to current year at runtime
    if end_year is None:
        end_year = dt.now().year
    for name, code in INDICATORS.items():
        df = wb.data.DataFrame(
            code,
            country,
            time=range(start_year, end_year + 1)
        )
        df = df.reset_index()
        filepath = RAW_DIR / f"wb_{name}.csv"
        df.to_csv(filepath, index=False)
        print(f"Saved {len(df)} rows → {filepath}")

if __name__ == "__main__":
    pull_world_bank()

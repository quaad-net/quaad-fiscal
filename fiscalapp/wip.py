import pandas as pd
import sqlalchemy as db

engine = db.create_engine(f"mssql+pymssql://eukoh:1Cartoon!@uqnt.database.windows.net:1433/uqnt")
cnxn = engine.connect()

expend = 'select year, total_expenditures from expenditures_and_receipts where year between 2013 and 2023'
expend_df = pd.read_sql(expend, cnxn)
real_gdp = 'select date, real_gdp from cbo_annual_cy where date between 2013 and 2023'
real_gdp_df = pd.read_sql(real_gdp, cnxn)
cnxn.close()

for i in range(len(expend_df)):
    expend_df.loc[i, 'expend_as_prct_rgdp'] = (expend_df['total_expenditures'][i] / real_gdp_df['real_gdp'][i]) * 100
    expend_df.loc[i, 'expend_as_prct_receipts'] = (expend_df['total_expenditures'][i] / real_gdp_df['real_gdp'][i]) * 100
    
# Copyright (c) 2026 Matthew Shirazi

import pandas as pd
import geopandas as gpd
from sqlalchemy import create_engine, select
from geoalchemy2 import Geometry
from sqlalchemy import insert, text, update
from backend.app.models import Election, Party, Candidate, District


### DUMMY USERNAMES AND PASSWORDS
# DB_NAME = 'mydatabase'
# USER = 'myuser'
# PASSWORD = 'mypassword'
# HOST = 'localhost'
# PORT = '5050'


def sort_csv_and_save_new_file(csv_file_path: str, ELECTION_YEAR: str):
    voting_data = pd.read_csv(csv_file_path)


    ### FIX VICTORIA DISTRICT NAMES TO MATCH SHAPEFILE
    if int(ELECTION_YEAR) < 1968:
        voting_data.loc[(voting_data["Province or Territory"] == "British Columbia") 
                        & (voting_data["Constituency"] == "Victoria"),"Constituency"] = "Victoria (B.C.)"
    
    voting_data.loc[(voting_data["Province or Territory"] == "New Brunswick") 
                    & (voting_data["Constituency"] == "Victoria"),"Constituency"] = "Victoria (N.B.)"
    
    voting_data.loc[(voting_data["Province or Territory"] == "Nova Scotia") 
                    & (voting_data["Constituency"] == "Victoria"),"Constituency"] = "Victoria (N.S.)"
    
    voting_data.loc[(voting_data["Province or Territory"] == "Ontario") 
                    & (voting_data["Constituency"] == "Victoria"),"Constituency"] = "Victoria (Ont.)"
    
    voting_data.loc[(voting_data["Province or Territory"] == "Alberta") 
                    & (voting_data["Constituency"] == "Victoria"),"Constituency"] = "Victoria (Alta.)"
    

    ### FIX KINGS DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Province or Territory"] == "New Brunswick") 
                    & (voting_data["Constituency"] == "King's"),"Constituency"] = "King's (N.B.)"
    
    voting_data.loc[(voting_data["Province or Territory"] == "Nova Scotia") 
                    & (voting_data["Constituency"] == "Kings"),"Constituency"] = "King's (N.S.)"
    

    ### FIX CARLETON DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Province or Territory"] == "New Brunswick") 
                    & (voting_data["Constituency"] == "Carleton"),"Constituency"] = "Carleton (N.B.)"
    
    if int(ELECTION_YEAR) < 1917:
        voting_data.loc[(voting_data["Province or Territory"] == "Ontario") 
                        & (voting_data["Constituency"] == "Carleton"),"Constituency"] = "Carleton (Ont.)"
    

    ### FIX QUEENS DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Province or Territory"] == "New Brunswick") 
                    & (voting_data["Constituency"] == "Queen's"),"Constituency"] = "Queen's (N.B.)"
    
    voting_data.loc[(voting_data["Province or Territory"] == "Nova Scotia") 
                    & (voting_data["Constituency"] == "Queens"),"Constituency"] = "Queen's (N.S.)"
    
    
    ### FIX KENT DISTRICT NAMES TO MATCH SHAPEFILE
    if int(ELECTION_YEAR) < 1979:
        voting_data.loc[(voting_data["Province or Territory"] == "Ontario") 
                        & (voting_data["Constituency"] == "Kent"),"Constituency"] = "Kent (Ont.)"
    
    voting_data.loc[(voting_data["Province or Territory"] == "New Brunswick") 
                    & (voting_data["Constituency"] == "Kent"),"Constituency"] = "Kent (N.B.)"
    
    
    ### FIX Jacques Cartier DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Province or Territory"] == "Quebec") 
                    & (voting_data["Constituency"] == "Jacques Cartier"),"Constituency"] = "Jacques-Cartier"
    

    ### FIX MONTREAL DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Province or Territory"] == "Quebec") 
                    & (voting_data["Constituency"] == "Montreal East"),"Constituency"] = "Montreal Est"
    
    voting_data.loc[(voting_data["Province or Territory"] == "Quebec") 
                    & (voting_data["Constituency"] == "Montreal West"),"Constituency"] = "Montreal Ouest"
    

    ### FIX VILLE DU QUEBEC DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "Quebec County"),"Constituency"] = "Québec (Comté)"
    
    voting_data.loc[(voting_data["Constituency"] == "Quebec East"),"Constituency"] = "Québec-Est"

    voting_data.loc[(voting_data["Constituency"] == "Quebec West"),"Constituency"] = "Québec-Ouest"

    voting_data.loc[(voting_data["Constituency"] == "Quebec-Centre"),"Constituency"] = "Québec-Centre"


    ### FIX Three Rivers (TROIS RIVIERES) DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "Three Rivers"),"Constituency"] = "Trois-Rivières"

    voting_data.loc[(voting_data["Constituency"] == "Three Rivers and St. Maurice"),"Constituency"] = "Trois-Rivières et Saint-Maurice"


    ### FIX Two Mountains (DEUX MONTAGNES) DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "Two Mountains"),"Constituency"] = "Deux-Montagnes"


    ### FIX St. John's (Saint-Jean) DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Province or Territory"] == "Quebec") 
                    & (voting_data["Constituency"] == "St. John's"),"Constituency"] = "Saint-Jean"
    

    ### FIX NEW BRUNSWICK St. John DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "St. John (City and County of)"),"Constituency"] = "City and County of St. John"

    voting_data.loc[(voting_data["Constituency"] == "St. John (City of )"),"Constituency"] = "City of St. John"

    
    ### FIX St. Hyacinthe DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Province or Territory"] == "Quebec") 
                    & (voting_data["Constituency"] == "St. Hyacinthe"),"Constituency"] = "Saint-Hyacinthe"
    

    ### FIX Saint Maurice DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Province or Territory"] == "Quebec") 
                    & (voting_data["Constituency"] == "Saint Maurice"),"Constituency"] = "Saint-Maurice"
    

    ### FIX Sherbrooke (Town of) DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Province or Territory"] == "Quebec") 
                    & (voting_data["Constituency"] == "Sherbrooke (Town of)"),"Constituency"] = "Sherbrooke"
    

    ### FIX Saskatchewan (Provisional District) DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Province or Territory"] == "Northwest Territories") 
                    & (voting_data["Constituency"] == "Saskatchewan (Provisional District)"),"Constituency"] = "Saskatchewan"
    

    ### FIX Alberta (Provisional District) DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Province or Territory"] == "Northwest Territories") 
                    & (voting_data["Constituency"] == "Alberta (Provisional District)"),"Constituency"] = "Alberta"
    
    ### FIX Ottawa (County of) DISTRICT NAMES TO MATCH SHAPEFILE
    if int(ELECTION_YEAR) > 1887:
        voting_data.loc[(voting_data["Province or Territory"] == "Quebec") 
                        & (voting_data["Constituency"] == "Ottawa (County of)"),"Constituency"] = "Labelle"
        
        voting_data.loc[(voting_data["Province or Territory"] == "Ontario") 
                        & (voting_data["Constituency"] == "Ottawa (City of)"),"Constituency"] = "Ottawa"


    ### FIX St. Mary DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "St. Mary"),"Constituency"] = "Sainte-Marie"


    ### FIX St. Lawrence DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "St. Lawrence"),"Constituency"] = "Saint-Laurent"


    ### FIX St. Johns--Iberville DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "St. Johns--Iberville"),"Constituency"] = "Saint-Jean--Iberville"


    ### FIX St. James DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "St. James"),"Constituency"] = "Saint-Jacques"


    ### FIX St. Antoine DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "St. Antoine"),"Constituency"] = "Saint-Antoine"


    ### FIX St. Anne DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "St. Anne"),"Constituency"] = "Sainte-Anne"


    ### FIX King's (P.E.I.) DISTRICT NAMES TO MATCH SHAPEFILE
    if int(ELECTION_YEAR) < 1896:
        voting_data.loc[(voting_data["Province or Territory"] == "Prince Edward Island") 
                            & (voting_data["Constituency"] == "King's"),"Constituency"] = "King's County"

    ### FIX North Cape Breton and Victoria DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "North Cape Breton and Victoria"),"Constituency"] = "Cape Breton North and Victoria"


    ### FIX East Calgary DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "East Calgary"),"Constituency"] = "Calgary East"


    ### FIX Laval--Two Mountains DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "Laval--Two Mountains"),"Constituency"] = "Laval--Deux-Montagnes"

    ### FIX Quebec South DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "Quebec South"),"Constituency"] = "Québec-Sud"

    ### FIX St. Ann DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "St. Ann"),"Constituency"] = "Sainte-Anne"

    ### FIX St. Denis DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "St. Denis"),"Constituency"] = "Saint-Denis"

    ### FIX St. Hyacinthe--Rouville DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "St. Hyacinthe--Rouville"),"Constituency"] = "Saint-Hyacinthe--Rouville"

    ### FIX St. John--Albert DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "St. John--Albert"),"Constituency"] = "Saint John--Albert"

    ### FIX St. Lawrence--St. George DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "St. Lawrence--St. George"),"Constituency"] = "Saint-Laurent--Saint-Georges"

    ### FIX Fraser Valley DISTRICT NAMES TO MATCH SHAPEFILE
    if ELECTION_YEAR == '1917':
        voting_data.loc[(voting_data["Constituency"] == "Fraser Valley"),"Constituency"] = "Westminster District"

    ### FIX Westmount--St. Henri DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "Westmount--St. Henri"),"Constituency"] = "Westmount--Saint-Henri"

    ### FIX Northumberland DISTRICT NAMES TO MATCH SHAPEFILE
    if int(ELECTION_YEAR) >= 1917 and int(ELECTION_YEAR) < 1957:
        voting_data.loc[(voting_data["Province or Territory"] == "New Brunswick") 
                        & (voting_data["Constituency"] == "Northumberland"),"Constituency"] = "Northumberland (N.B.)"
        
        voting_data.loc[(voting_data["Province or Territory"] == "Ontario") 
                                & (voting_data["Constituency"] == "Northumberland"),"Constituency"] = "Northumberland (Ont.)"
        
    ### FIX Lake St. John DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "Lake St. John"),"Constituency"] = "Lac-Saint-Jean"

    ### FIX St. Henri DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "St. Henri"),"Constituency"] = "Saint-Henri"

    ### FIX Three Rivers--St. Maurice DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "Three Rivers--St. Maurice"),"Constituency"] = "Trois-Rivières--Saint-Maurice"

    ### FIX Joliette--l'Assomption--Montcalm DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "Joliette--l'Assomption--Montcalm"),"Constituency"] = "Joliette--L'Assomption--Montcalm"

    ### FIX Lake St-John--Roberval DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "Lake St-John--Roberval"),"Constituency"] = "Lac-Saint-Jean--Roberval"

    ### FIX Montmagny--l'Islet DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "Montmagny--l'Islet"),"Constituency"] = "Montmagny--L'Islet"

    ### FIX Quebec West and South DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "Quebec West and South"),"Constituency"] = "Québec-Ouest-et-Sud"

    ### FIX St. Antoine--Westmount DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "St. Antoine--Westmount"),"Constituency"] = "Saint-Antoine--Westmount"

    ### FIX St. Henry DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "St. Henry"),"Constituency"] = "Saint-Henri"

    ### FIX St. Hyacinthe--Bagot DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "St. Hyacinthe--Bagot"),"Constituency"] = "Saint-Hyacinthe--Bagot"

    ### FIX  St. Johns--Iberville--Napierville DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "St. Johns--Iberville--Napierville"),"Constituency"] = "Saint-Jean--Iberville--Napierville"

    ### FIX St-Maurice--Laflèche DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "St-Maurice--Laflèche"),"Constituency"] = "Saint-Maurice--Laflèche"

    ### FIX Outremont--St-Jean DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "Outremont--St-Jean"),"Constituency"] = "Outremont--Saint-Jean"

    ### FIX St-Denis DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "St-Denis"),"Constituency"] = "Saint-Denis"

    ### FIX St-Henri DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "St-Henri"),"Constituency"] = "Saint-Henri"

    ### FIX Berthier--Maskinongé--de Lanaudière DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "Berthier--Maskinongé--de Lanaudière"),"Constituency"] = "Berthier--Maskinongé--Delanaudière"

    ### FIX Okanagan Boundary DISTRICT NAMES TO MATCH SHAPEFILE
    if int(ELECTION_YEAR) < 1968:
        voting_data.loc[(voting_data["Constituency"] == "Okanagan Boundary"),"Constituency"] = "Okanagan--Boundary"

    ### FIX Coast-Capilano DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "Coast-Capilano"),"Constituency"] = "Coast--Capilano"

    ### FIX Leeds--Grenville--Thousand Islands--Rideau Lakes DISTRICT NAMES TO MATCH SHAPEFILE
    if int(ELECTION_YEAR) >= 2015 and int(ELECTION_YEAR) < 2025:
        voting_data.loc[(voting_data["Constituency"] == "Leeds--Grenville--Thousand Islands--Rideau Lakes"),"Constituency"] = "Leeds--Grenville--Thousand Islands and Rideau Lakes"

    ### FIX St. Boniface--St. Vital DISTRICT NAMES TO MATCH SHAPEFILE
    voting_data.loc[(voting_data["Constituency"] == "St. Boniface--St. Vital"),"Constituency"] = "Saint Boniface--Saint Vital"


    voting_data = voting_data.sort_values('Constituency', ascending=True)
    voting_data.reset_index(drop=True, inplace=True)

    voting_data.drop(['Gender'], axis=1, inplace=True)


    voting_data.to_csv('voting_data/electionsCandidates' + ELECTION_YEAR + '_sorted.csv', index=False)



def upload_parties_to_postgres(csv_file_path: str, ELECTION_YEAR: str):

    voting_data = pd.read_csv(csv_file_path)
    
    engine_string = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
    engine = create_engine(engine_string)

    unimported_parties = []

    with engine.connect() as conn:

        with conn.begin():

            ### SAVE UNIQUE PARTIES
            unique_parties = voting_data["Political Affiliation"].dropna().unique()

            for party_name in unique_parties:
                existing_party_id = conn.execute(
                    select(Party).where(Party.name == party_name)
                ).scalar_one_or_none()

                if not existing_party_id:
                    unimported_parties.append({"name": party_name})
                    print(f"{party_name} not found!")

            if len(unimported_parties) != 0:
                conn.execute(insert(Party), unimported_parties)
                conn.commit()
                print(f"Political parties in {ELECTION_YEAR} imported successfully into Postgres!")
            else: 
                print(f"All political parties are already imported for the {ELECTION_YEAR} election!")

    engine.dispose()

def upload_candidates_to_postgres(election_id: int, boundary_version_id: int, ELECTION_YEAR: str):
    
    engine_string = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
    engine = create_engine(engine_string)

    with engine.connect() as conn:

        with conn.begin():

            existing_candidates = conn.execute(
                        select(Candidate).where(Candidate.election_id == election_id)
                    ).scalars().all()
            
            if existing_candidates:
                print(f"Candidates in the {ELECTION_YEAR} election already exist! Backing out...")
                return
            else:
    
                conn.execute(text("""
                INSERT INTO candidates (name, occupation, election_id, district_id)
                SELECT DISTINCT
                    s."Candidate",
                    s."Occupation",
                    :election_id,
                    d.id
                FROM staging_table s
                JOIN district_aliases da
                    ON da.alias_name = s."Constituency"
                JOIN districts d
                    ON d.id = da.district_id
                    AND d.boundary_version_id = :boundary_version_id
                    AND d.election_id = :election_id;
                """),
                {
                    "election_id": election_id,
                    "boundary_version_id": boundary_version_id
                })
                
                print(f"Candidates in {ELECTION_YEAR} imported successfully into Postgres!")

    engine.dispose()


def upload_csv_to_staging_table(csv_file_path: str, ELECTION_YEAR: int):

    staging_voting_data = pd.read_csv(csv_file_path)
    
    engine_string = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
    engine = create_engine(engine_string)

    staging_voting_data.to_sql('staging_table', con=engine, index=False, if_exists='append')

    engine.dispose()

    print(f"Results for {ELECTION_YEAR} imported successfully into staging_table!")


def populate_district_aliases_table(ELECTION_YEAR: str):

    engine_string = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
    engine = create_engine(engine_string)

    with engine.begin() as conn:

        conn.execute(text("TRUNCATE district_aliases RESTART IDENTITY"))

        conn.execute(text("""
            INSERT INTO district_aliases (alias_name, district_id)
            SELECT fedname, id
            FROM districts;
         """))

        print(f"district_aliases table was populated for the {ELECTION_YEAR} election!")
    
    engine.dispose()


def upload_results_to_postgres(election_id: int, boundary_version_id: int, ELECTION_YEAR: str):
        
    engine_string = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
    engine = create_engine(engine_string)

    with engine.begin() as conn:

        conn.execute(text("""
        INSERT INTO results (
            election_id,
            district_id,
            candidate_id,
            party_id,
            votes,
            result
        )
        SELECT
            :election_id,
            d.id,
            c.id,
            p.id,
            s."Votes",
            s."Result"
        FROM staging_table s

        JOIN district_aliases da
            ON da.alias_name = s."Constituency"

        JOIN districts d
            ON d.id = da.district_id
            AND d.election_id = :election_id

        JOIN candidates c
            ON c.name = s."Candidate"
            AND c.election_id = :election_id
            AND c.district_id = d.id

        JOIN parties p
            ON p.name = s."Political Affiliation"
        """),
        {
            "election_id": election_id,
            "boundary_version_id": boundary_version_id
        })

        print(f"Results table was populated with voting data from the {ELECTION_YEAR} election!")

        ### CLEAR STAGING TABLE
        conn.execute(text("TRUNCATE staging_table RESTART IDENTITY"))
    
    engine.dispose()


def remove_incorrect_districts(shapefile_path: str, rows_to_keep, fedid_of_incorrect_districts, ELECTION_YEAR):
    ### REMOVES DISTRICTS THAT ARE PRESENT IN THE SHAPEFILE, BUT WERE NOT IN AN ELECTION
    if rows_to_keep is not None and fedid_of_incorrect_districts is not None and fedid_of_incorrect_districts >= 12000:
        districts = gpd.read_file(shapefile_path, rows=rows_to_keep, encoding="UTF-8")
        districts['id'] = districts['id'].astype(int)
        districts = districts[districts['id'] < fedid_of_incorrect_districts]
    
    elif ELECTION_YEAR == '1896' or ELECTION_YEAR == '1900':
        districts = gpd.read_file(shapefile_path, encoding="UTF-8")
        districts['id'] = districts['id'].astype(int)
        districts = districts[districts['id'] != 60001] ### REMOVE YUKON DISTRICT
    
    elif rows_to_keep is None and fedid_of_incorrect_districts is not None and fedid_of_incorrect_districts >= 12000:
        districts = gpd.read_file(shapefile_path, encoding="UTF-8")
        districts['id'] = districts['id'].astype(int)
        districts = districts[districts['id'] < fedid_of_incorrect_districts]
    
    elif rows_to_keep is None and fedid_of_incorrect_districts is not None and fedid_of_incorrect_districts < 12000:
        districts = gpd.read_file(shapefile_path, encoding="UTF-8")
        districts['id'] = districts['id'].astype(int)
        districts = districts[districts['id'] > fedid_of_incorrect_districts]

    return districts


def simplify_nunavut(districts: pd.DataFrame, ELECTION_YEAR: str):
    ### SIMPLIFY NUNATSIAQ SHAPE SIZE BY 100, MERGE INTO districts DATAFRAME WHERE ALL OTHER DISTRICTS ARE SIMPLIFIED BY 20
    if int(ELECTION_YEAR) < 2019: 
        nunavut_district = districts[districts['id'] == 61002]
    elif int(ELECTION_YEAR) >= 2019: 
        nunavut_district = districts[districts['id'] == 62001]

    nunavut_district["geometry"] = nunavut_district.to_crs(
        nunavut_district.estimate_utm_crs()).simplify(500).to_crs(nunavut_district.crs)

    new_attributes = nunavut_district.iloc[0].drop('geometry')

    merged_geometry = nunavut_district.geometry.union_all()
    new_row = gpd.GeoSeries([merged_geometry], crs=districts.crs, name='geometry')
    new_row_gdf = gpd.GeoDataFrame(new_attributes.to_frame().T, geometry=new_row)

    new_row_gdf['geometry'] = merged_geometry

    gdf_updated = districts.drop(nunavut_district.index)

    districts_new = pd.concat([gdf_updated, new_row_gdf], ignore_index=True)

    return districts_new


def simplify_mackenzie_river(districts: pd.DataFrame, ELECTION_YEAR: str):
    ### SIMPLIFY Mackenzie River SHAPE SIZE BY 100, MERGE INTO districts DATAFRAME WHERE ALL OTHER DISTRICTS ARE SIMPLIFIED BY 20
    if ELECTION_YEAR == '1949':
        mackenzie_district = districts[districts['id'] == 60001]
        mackenzie_district["geometry"] = mackenzie_district.to_crs(
        mackenzie_district.estimate_utm_crs()).simplify(500).to_crs(mackenzie_district.crs)

    elif int(ELECTION_YEAR) >= 1953 and int(ELECTION_YEAR) < 1979:
        mackenzie_district = districts[districts['id'] == 61001]
        mackenzie_district["geometry"] = mackenzie_district.to_crs(
        mackenzie_district.estimate_utm_crs()).simplify(500).to_crs(mackenzie_district.crs)

    elif int(ELECTION_YEAR) >= 1979 and int(ELECTION_YEAR) < 2019:
        mackenzie_district = districts[districts['id'] == 62002]
        mackenzie_district["geometry"] = mackenzie_district.to_crs(
        mackenzie_district.estimate_utm_crs()).simplify(100).to_crs(mackenzie_district.crs)

    elif int(ELECTION_YEAR) >= 2019:
        mackenzie_district = districts[districts['id'] == 61001]
        mackenzie_district["geometry"] = mackenzie_district.to_crs(
        mackenzie_district.estimate_utm_crs()).simplify(100).to_crs(mackenzie_district.crs)

    new_attributes = mackenzie_district.iloc[0].drop('geometry')

    merged_geometry = mackenzie_district.geometry.union_all()
    new_row = gpd.GeoSeries([merged_geometry], crs=districts.crs, name='geometry')
    new_row_gdf = gpd.GeoDataFrame(new_attributes.to_frame().T, geometry=new_row)

    new_row_gdf['geometry'] = merged_geometry

    gdf_updated = districts.drop(mackenzie_district.index)

    districts_new = pd.concat([gdf_updated, new_row_gdf], ignore_index=True)

    return districts_new


def merge_disputed_territories(districts: pd.DataFrame):
    ####### MERGE THE TERRITORIES CLAIMED BY ONTARIO FOR 1891 ELECTION (GIVEN TO ONTARIO IN 1889) - PRE WORK ######
    rows_to_merge = districts[districts['fedname'].isin(['Algoma', 'Claimed by Ontario (awarded 1889)', 'Disputed Territories (Awarded to Ontario 1889)'])]

    new_attributes = rows_to_merge.iloc[0].drop('geometry')
    new_attributes['fedname'] = "Algoma"

    merged_geometry = rows_to_merge.geometry.union_all()
    new_row = gpd.GeoSeries([merged_geometry], crs=districts.crs, name='geometry')
    new_row_gdf = gpd.GeoDataFrame(new_attributes.to_frame().T, geometry=new_row)

    new_row_gdf['geometry'] = merged_geometry

    gdf_updated = districts.drop(rows_to_merge.index)

    districts_new = pd.concat([gdf_updated, new_row_gdf], ignore_index=True)

    return districts_new


def fix_middlesex_and_london_districts(districts: pd.DataFrame):
    ## GET CORRECT WENTWORTH DISTRICT FROM 1903 election, 1905 wentworth is incorrect (overlaps Hamilton East and West)
    correct_wentworth = gpd.read_file("districts2/CBF_RO1903_CSRS.shp")
    correct_wentworth = correct_wentworth[correct_wentworth['fedname'].isin(['Wentworth'])]

    gdf_updated = districts.drop(districts[districts['fedname'] == 'Wentworth'].index)

    districts = pd.concat([gdf_updated, correct_wentworth], ignore_index=True)
    # ************************************************************************************ #
    ## GET CORRECT MIDDLESEX-EAST DISTRICT FROM 1903 election, 1905 MIDDLESEX-EAST is incorrect (overlaps London)
    correct_districts= gpd.read_file("districts2/CBF_RO1903_CSRS.shp")
    correct_middlesex_east = correct_districts[correct_districts['fedname'].isin(['Middlesex East'])]

    gdf_updated_mideast = districts.drop(districts[districts['fedname'] == 'Middlesex East'].index)

    districts = pd.concat([gdf_updated_mideast, correct_middlesex_east], ignore_index=True)
    # ************************************************************************************ #
    ## ALSO GET BETTER FITTING LONDON DISTRICT
    better_london = correct_districts[correct_districts['fedname'].isin(['London'])]

    gdf_updated_london = districts.drop(districts[districts['fedname'] == 'London'].index)

    districts = pd.concat([gdf_updated_london, better_london], ignore_index=True)

    return districts


def simplify_and_save_shp_file(
        shapefile_path: str, ELECTION_YEAR: str, 
        ELECTION_ID: int, rows_to_keep, fedid_of_incorrect_districts,
        BOUNDARY_VERSION_ID: int):

    if rows_to_keep is not None or fedid_of_incorrect_districts is not None:
        districtsDataframe = remove_incorrect_districts(shapefile_path, rows_to_keep, fedid_of_incorrect_districts, ELECTION_YEAR)
    else:
        districtsDataframe = gpd.read_file(shapefile_path, encoding="UTF-8")
        districtsDataframe['id'] = districtsDataframe['id'].astype(int)

    if ELECTION_YEAR == '1882' or ELECTION_YEAR == '1887':
        ## Remove Claimed and Disputed territories ##
        districtsDataframe = districtsDataframe[districtsDataframe['fedname'] != "Claimed by Ontario (awarded 1889)"]
        districtsDataframe = districtsDataframe[districtsDataframe['fedname'] != "Disputed Territories (Awarded to Ontario 1889)"]

    if ELECTION_YEAR == '1891':
        districtsDataframe = merge_disputed_territories(districtsDataframe)

    if ELECTION_YEAR == '1908' or ELECTION_YEAR == '1911':
        districtsDataframe = fix_middlesex_and_london_districts(districtsDataframe)

    ## Simplifiy district shapes to increase loading speed
    districtsDataframe["geometry"] = (districtsDataframe.to_crs(districtsDataframe.estimate_utm_crs()).simplify(20).to_crs(districtsDataframe.crs))


    if int(ELECTION_YEAR) >= 1949:
        districtsDataframe = simplify_mackenzie_river(districtsDataframe, ELECTION_YEAR)
    if int(ELECTION_YEAR) >= 1979:
        districtsDataframe = simplify_nunavut(districtsDataframe, ELECTION_YEAR)


    ## SET SRID TO 4326 TO BE COMPATIBILE WITH LEAFLET
    districtsDataframe = districtsDataframe.to_crs("EPSG:4326")

    districtsDataframe = districtsDataframe.sort_values('fedname', ascending=True)
    districtsDataframe.reset_index(drop=True, inplace=True)


    ### REMOVE UNNECESSARY COLUMNS
    if 'OBJECTID' in districtsDataframe.columns:
        districtsDataframe = districtsDataframe.drop(columns=['OBJECTID'])
    if 'fedid' in districtsDataframe.columns:
        districtsDataframe = districtsDataframe.drop(columns=['fedid'])
    if 'Notes' in districtsDataframe.columns:
        districtsDataframe = districtsDataframe.drop(columns=['Notes'])
    if 'id' in districtsDataframe.columns:
        districtsDataframe = districtsDataframe.drop(columns=['id'])
    if 'arealand' in districtsDataframe.columns:
        districtsDataframe = districtsDataframe.drop(columns=['arealand'])
    if 'areawater' in districtsDataframe.columns:
        districtsDataframe = districtsDataframe.drop(columns=['areawater'])

    if 'areatotal' in districtsDataframe.columns:
        districtsDataframe['shape_area'] = districtsDataframe['areatotal']
        districtsDataframe = districtsDataframe.drop(columns=['areatotal'])

    ### RENAME COLUMNS TO MATCH POSTGRES DATABASE
    districtsDataframe = districtsDataframe.rename(columns={'Shape_Area': 'shape_area', 'geometry': 'geom'})

    ### SET ELECTION_ID
    districtsDataframe['election_id'] = ELECTION_ID

    ### SET BOUNDARY_VERSION_ID
    districtsDataframe['boundary_version_id'] = BOUNDARY_VERSION_ID

    ### FOR DEBUGGING
    # pd.set_option('display.max_rows', None)
    # pd.set_option('display.max_columns', None)
    # print(districtsDataframe)

    ### SAVES DATAFRAME TO .gpkg
    districtsDataframe.to_file("./simplified_district_data/Canada"+ ELECTION_YEAR + ".gpkg", driver="GPKG")


def create_election_in_database(election_id: int, ELECTION_YEAR: int, BOUNDARY_VERSION_ID: int):

    engine = create_engine(
        f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
    )

    with engine.connect() as conn:

        with conn.begin():
            ### CHECK IF ELECTION ALREADY EXISTS
            election_query = select(Election).where(Election.id == election_id)
            result = conn.execute(election_query).fetchone()

            if result is None:
                result = conn.execute(
                    insert(Election).values(id=election_id, year=ELECTION_YEAR, boundary_version_id=BOUNDARY_VERSION_ID)
                )
                conn.commit()
                print(str(ELECTION_YEAR) + " election was created successfully!\n")
            else:
                print(str(ELECTION_YEAR) + " election already exists, SKIPPING\n")

    engine.dispose()


def upload_shapefile_to_postgres(shapefile_path: str, ELECTION_ID: int, ELECTION_YEAR: str):

    engine = create_engine(
        f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
    )
    with engine.connect() as conn:

        with conn.begin():

            existing_districts = conn.execute(
                        select(District).where(District.election_id == ELECTION_ID)
                    ).scalar()
            
            if existing_districts:
                print(f"Districts in the {ELECTION_YEAR} election already exist! Backing out...")
                return
            else:

                gdf = gpd.read_file(shapefile_path)

                gdf = gdf.rename(columns={"geometry": "geom"})
                gdf = gdf.set_geometry("geom")

                # Ensure CRS is correct
                gdf = gdf.set_crs(4326, allow_override=True)

                # pd.set_option('display.max_rows', None)
                # pd.set_option('display.max_columns', None)
                # print(gdf)

                gdf.to_postgis(
                    "districts",
                    engine,
                    if_exists="append",
                    index=False,
                    dtype={
                        "geom": Geometry("MULTIPOLYGON", srid=4326)
                    }
                )

                print("Uploaded " + shapefile_path + " successfully!\n")

    engine.dispose()


def fix_district_names_in_postgres(ELECTION_ID: int):

    engine = create_engine(
        f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
    )
    with engine.connect() as conn:

        with conn.begin():

            existing_districts = conn.execute(
                        select(District).where(District.election_id == ELECTION_ID)
                    ).columns("id","fedname","shape_area").all()


            for row in existing_districts:

                if row[1] == "Prince" and ELECTION_ID < 9:
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Prince County"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Prince County'")

                elif row[1] == "Queens" and row[2] == '2831092401.233065' or row[1] == "Queens" and row[2] == '2831.092':
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Queen's (N.S.)"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Queen's (N.S.)'")

                elif row[1] == "Queens" and row[2] == '2120913186.2305257' or row[1] == "Queens" and row[2] == '2127.34':
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Queen's County"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Queen's County'")

                elif row[1] == "Queens" and row[2] == '3971994987.6643124' or row[1] == "Queens" and row[2] == '3971.995':
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Queen's (N.B.)"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Queen's (N.B.)'")

                elif row[1] == "Kings (N.B.)":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="King's (N.B.)"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'King's (N.B.)'")

                elif row[1] == "Kings (N.S.)":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="King's (N.S.)"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'King's (N.S.)'")

                elif row[1] == "Kings (P.E.I.)" and ELECTION_ID < 8:
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="King's County"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'King's County'")

                elif row[1] == "Kings (P.E.I.)" and ELECTION_ID > 8:
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="King's (P.E.I)"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'King's (P.E.I)'")

                elif row[1] == "Kings" and ELECTION_ID > 8:
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="King's"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'King's'")

                elif row[1] == "Ottawa" and row[2] == '16552813087.962992':
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Ottawa (County of)"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Ottawa (County of)'")

                elif row[1] == "Ottawa" and row[2] == '8686273.208374564':
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Ottawa (City of)"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Ottawa (City of)'")

                elif row[1] == "Cornwall" and row[2] == '271322422.01872677' and ELECTION_ID == 5:
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Cornwall and Stormont"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Cornwall and Stormont'")

                elif row[1] == "East Queens" and row[2] == '1523314590.36':
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="East Queen's"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'East Queen's'")

                elif row[1] == "West Queens" and row[2] == '653707985.484':
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="West Queen's"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'West Queen's'")

                elif row[1] == "Shelburne and Queens":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Shelburne and Queen's"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Shelburne and Queen's'")

                elif row[1] == "Sunbury--Queens":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Sunbury--Queen's"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Sunbury--Queen's'")

                elif row[1] == "Kings and Albert":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="King's and Albert"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'King's and Albert'")

                elif row[1] == "Victoria and Cape Breton North":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Cape Breton North and Victoria"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Cape Breton North and Victoria'")

                elif row[1] == "Queens" and ELECTION_ID < 28:
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Queen's"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Queen's'")

                elif row[1] == "Kent" and (row[2] == '4625827166.674165' or row[2] == '4625736995.0'):
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Kent (N.B.)"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Kent (N.B.)'")

                elif row[1] == "Québec (comte)":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Québec (Comté)"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Québec (Comté)'")

                elif row[1] == "George-Étienne-Cartier":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="George-Étienne Cartier"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'George-Étienne Cartier'")

                elif ELECTION_ID == 13 and row[1] == "Fraser Valley":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Westminster District"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Westminster District'")

                elif row[1] == "Verdun--LaSalle":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Verdun--La Salle"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Verdun--La Salle'")

                elif row[1] == "Vancouver--Kingsway":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Vancouver Kingsway"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Vancouver Kingsway'")

                elif row[1] == "Vancouver--Quadra":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Vancouver Quadra"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Vancouver Quadra'")

                elif row[1] == "Notre-Dame-De-Grâce":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Notre-Dame-de-Grâce"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Notre-Dame-de-Grâce'")

                elif row[1] == "Cape Breton North And Victoria":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Cape Breton North and Victoria"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Cape Breton North and Victoria'")

                elif row[1] == "Îles-De-La-Madeleine":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Îles-de-la-Madeleine"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Îles-de-la-Madeleine'")

                elif ELECTION_ID >= 23 and row[1] == "Northumberland (N.B.)":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Northumberland--Miramichi"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Northumberland--Miramichi'")

                elif ELECTION_ID >= 23 and row[1] == "Northumberland (Ont.)":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Northumberland"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Northumberland'")

                elif ELECTION_ID >= 25 and row[1] == "Humboldt--Melfort":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Humboldt--Melfort--Tisdale"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Humboldt--Melfort--Tisdale'")

                elif ELECTION_ID >= 25 and ELECTION_ID < 31 and row[1] == "Nanaimo":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Humboldt--Melfort--Tisdale"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Humboldt--Melfort--Tisdale'")

                elif ELECTION_ID >= 25 and row[1] == "Mackenzie River":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Northwest Territories"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Northwest Territories'")

                elif ELECTION_ID >= 25 and ELECTION_ID < 28 and row[1] == "Témiscouata":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Rivière-du-Loup--Témiscouata"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Rivière-du-Loup--Témiscouata'")
                
                elif row[1] == "Frontenac--Lennox And Addington":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Frontenac--Lennox and Addington"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Frontenac--Lennox and Addington'")

                elif ELECTION_ID < 29 and row[1] == "Lanark And Renfrew":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Lanark and Renfrew"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Lanark and Renfrew'")

                elif row[1] == "Kingston And The Islands":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Kingston and the Islands"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Kingston and the Islands'")

                elif ELECTION_ID >= 29 and row[1] == "Burnaby--Richmond":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Burnaby--Richmond--Delta"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Burnaby--Richmond--Delta'")

                elif ELECTION_ID >= 29 and row[1] == "High Park":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="High Park--Humber Valley"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'High Park--Humber Valley'")

                elif ELECTION_ID >= 29 and ELECTION_ID < 31 and row[1] == "Bourassa":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Montreal--Bourassa"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Montreal--Bourassa'")

                elif ELECTION_ID >= 29 and ELECTION_ID <= 30 and row[1] == "Perth":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Perth--Wilmot"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Perth--Wilmot'")

                elif ELECTION_ID >= 29 and row[1] == "Renfrew North":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Renfrew North--Nipissing East"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Renfrew North--Nipissing East'")

                elif ELECTION_ID >= 29 and ELECTION_ID <= 30 and row[1] == "Sarnia":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Sarnia--Lambton"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Sarnia--Lambton'")

                elif ELECTION_ID >= 29 and ELECTION_ID <= 30 and row[1] == "Surrey":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Surrey--White Rock"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Surrey--White Rock'")

                elif ELECTION_ID >= 29 and ELECTION_ID <= 30 and row[1] == "Lakeshore":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Toronto--Lakeshore"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Toronto--Lakeshore'")

                elif ELECTION_ID >= 29 and ELECTION_ID <= 30 and row[1] == "Trois-Rivières":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Trois-Rivières Métropolitain"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Trois-Rivières Métropolitain'")

                elif ELECTION_ID >= 29 and ELECTION_ID <= 30 and row[1] == "Wellington--Grey":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Wellington--Grey--Dufferin--Waterloo"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Wellington--Grey--Dufferin--Waterloo'")

                elif ELECTION_ID >= 29 and row[1] == "Bonaventure":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Bonaventure--Îles-de-la-Madeleine"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Bonaventure--Îles-de-la-Madeleine'")

                elif ELECTION_ID >= 29 and row[1] == "Glengarry--Prescott":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Glengarry--Prescott--Russell"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Glengarry--Prescott--Russell'")

                elif ELECTION_ID >= 29 and ELECTION_ID <= 31 and row[1] == "Maisonneuve":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Maisonneuve--Rosemont"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Maisonneuve--Rosemont'")

                elif ELECTION_ID >= 29 and ELECTION_ID <= 30 and row[1] == "Argenteuil":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Argenteuil--Deux-Montagnes"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Argenteuil--Deux-Montagnes'")

                elif ELECTION_ID >= 29 and ELECTION_ID <= 30 and row[1] == "Témiscouata":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Rivière-du-Loup--Témiscouata"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Rivière-du-Loup--Témiscouata'")

                elif ELECTION_ID >= 29 and row[1] == "Beauharnois":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Beauharnois--Salaberry"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Beauharnois--Salaberry'")

                elif ELECTION_ID >= 29 and ELECTION_ID <= 30 and row[1] == "Missisquoi":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Brome--Missisquoi"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Brome--Missisquoi'")

                elif ELECTION_ID >= 29 and row[1] == "Lanark And Renfrew":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Lanark--Renfrew--Carleton"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Lanark--Renfrew--Carleton'")

                elif ELECTION_ID >= 29 and ELECTION_ID < 36 and row[1] == "Essex":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Essex--Windsor"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Essex--Windsor'")

                elif ELECTION_ID == 30 and row[1] == "Huron":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Huron--Middlesex"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Huron--Middlesex'")

                elif ELECTION_ID == 30 and row[1] == "Middlesex":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Middlesex--London--Lambton"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Middlesex--London--Lambton'")

                elif ELECTION_ID == 30 and row[1] == "Lachine":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Lachine--Lakeshore"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Lachine--Lakeshore'")

                elif ELECTION_ID == 30 and row[1] == "Lasalle":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Lasalle--Émard--Côte Saint-Paul"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Lasalle--Émard--Côte Saint-Paul'")

                elif ELECTION_ID == 30 and row[1] == "Peel South":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Mississauga"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Mississauga'")

                elif ELECTION_ID == 30 and row[1] == "Waterloo":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Waterloo--Cambridge"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Waterloo--Cambridge'")

                elif ELECTION_ID >= 30 and row[1] == "Ottawa East":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Ottawa--Vanier"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Ottawa--Vanier'")

                elif row[1] == "Humber--Port Au Port--St. Barbe":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Humber--Port au Port--St. Barbe"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Humber--Port au Port--St. Barbe'")

                elif row[1] == "Kamouraska--Rivière-Du-Loup":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Kamouraska--Rivière-du-Loup"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Kamouraska--Rivière-du-Loup'")

                elif row[1] == "Laval-Des-Rapides":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Laval-des-Rapides"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Laval-des-Rapides'")

                elif row[1] == "Prince George--Bulkley Valley" and row[2] == "108680840810.82312":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Prince George--Peace River"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Prince George--Peace River'")

                elif row[1] == "Bonaventure--Îles-De-La-Madeleine":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Bonaventure--Îles-de-la-Madeleine"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Bonaventure--Îles-de-la-Madeleine'")

                elif ELECTION_ID == 31 and row[1] == "La Prairie":
                    conn.execute(update(District).where(District.id == row[0]).values(fedname="Laprairie"))
                    print(f"[{row[0]}:{row[1]}] was updated to 'Laprairie'")

                if ELECTION_ID >= 43:
                    if row[1] == "Abitibi--T�miscamingue":
                        conn.execute(update(District).where(District.id == row[0]).values(fedname="Abitibi--Témiscamingue"))
                        print(f"[{row[0]}:{row[1]}] was updated to 'Abitibi--Témiscamingue'")
                    elif row[1] == "Avignon--La Mitis--Matane--Matap�dia":
                        conn.execute(update(District).where(District.id == row[0]).values(fedname="Avignon--La Mitis--Matane--Matapédia"))
                        print(f"[{row[0]}:{row[1]}] was updated to 'Avignon--La Mitis--Matane--Matapédia'")
                    elif row[1] == "Beauport--C�te-de-Beaupr�--�le d�Orl�ans--Charlevoix":
                        conn.execute(update(District).where(District.id == row[0]).values(fedname="Beauport--Côte-de-Beaupré--Île D’Orléans--Charlevoix"))
                        print(f"[{row[0]}:{row[1]}] was updated to 'Avignon--La Mitis--Matane--Matapédia'")
                    elif row[1] == "Beaus�jour":
                        conn.execute(update(District).where(District.id == row[0]).values(fedname="Beauséjour"))
                        print(f"[{row[0]}:{row[1]}] was updated to 'Beauséjour'")
                    elif row[1] == "B�cancour--Nicolet--Saurel":
                        conn.execute(update(District).where(District.id == row[0]).values(fedname="Bécancour--Nicolet--Saurel"))
                        print(f"[{row[0]}:{row[1]}] was updated to 'Bécancour--Nicolet--Saurel'")
                    elif row[1] == "Bellechasse--Les Etchemins--L�vis":
                        conn.execute(update(District).where(District.id == row[0]).values(fedname="Bellechasse--Les Etchemins--Lévis"))
                        print(f"[{row[0]}:{row[1]}] was updated to 'Bellechasse--Les Etchemins--Lévis'")
                    elif row[1] == "Ch�teauguay--Lacolle":
                        conn.execute(update(District).where(District.id == row[0]).values(fedname="Châteauguay--Lacolle"))
                        print(f"[{row[0]}:{row[1]}] was updated to 'Châteauguay--Lacolle'")
                    elif row[1] == "Desneth�--Missinippi--Churchill River":
                        conn.execute(update(District).where(District.id == row[0]).values(fedname="Desnethé--Missinippi--Churchill River"))
                        print(f"[{row[0]}:{row[1]}] was updated to 'Desnethé--Missinippi--Churchill River'")
                    elif row[1] == "Gasp�sie--Les �les-de-la-Madeleine":
                        conn.execute(update(District).where(District.id == row[0]).values(fedname="Gaspésie--Les Îles-de-la-Madeleine"))
                        print(f"[{row[0]}:{row[1]}] was updated to 'Gaspésie--Les Îles-de-la-Madeleine'")
                    elif row[1] == "Honor�-Mercier":
                        conn.execute(update(District).where(District.id == row[0]).values(fedname="Honoré-Mercier"))
                        print(f"[{row[0]}:{row[1]}] was updated to 'Honoré-Mercier'")
                    elif row[1] == "La Pointe-de-l'�le":
                        conn.execute(update(District).where(District.id == row[0]).values(fedname="La Pointe-de-l'Île"))
                        print(f"[{row[0]}:{row[1]}] was updated to 'La Pointe-de-l'Île'")
                    elif row[1] == "LaSalle--�mard--Verdun":
                        conn.execute(update(District).where(District.id == row[0]).values(fedname="LaSalle--Émard--Verdun"))
                        print(f"[{row[0]}:{row[1]}] was updated to 'LaSalle--Émard--Verdun'")
                    elif row[1] == "Laval--Les �les":
                        conn.execute(update(District).where(District.id == row[0]).values(fedname="Laval--Les Îles"))
                        print(f"[{row[0]}:{row[1]}] was updated to 'Laval--Les Îles'")
                    elif row[1] == "L�vis--Lotbini�re":
                        conn.execute(update(District).where(District.id == row[0]).values(fedname="Lévis--Lotbinière"))
                        print(f"[{row[0]}:{row[1]}] was updated to 'Lévis--Lotbinière'")
                    elif row[1] == "Marc-Aur�le-Fortin":
                        conn.execute(update(District).where(District.id == row[0]).values(fedname="Marc-Aurèle-Fortin"))
                        print(f"[{row[0]}:{row[1]}] was updated to 'Marc-Aurèle-Fortin'")
                    elif row[1] == "M�gantic--L'�rable":
                        conn.execute(update(District).where(District.id == row[0]).values(fedname="Mégantic--L'Érable"))
                        print(f"[{row[0]}:{row[1]}] was updated to 'Mégantic--L'Érable'")
                    elif row[1] == "Montmagny--L'Islet--Kamouraska--Rivi�re-du-Loup":
                        conn.execute(update(District).where(District.id == row[0]).values(fedname="Montmagny--L’Islet--Kamouraska--Rivière-du-Loup"))
                        print(f"[{row[0]}:{row[1]}] was updated to 'Montmagny--L’Islet--Kamouraska--Rivière-du-Loup'")
                    elif row[1] == "Notre-Dame-de-Gr�ce--Westmount":
                        conn.execute(update(District).where(District.id == row[0]).values(fedname="Notre-Dame-de-Grâce--Westmount"))
                        print(f"[{row[0]}:{row[1]}] was updated to 'Notre-Dame-de-Grâce--Westmount'")
                    elif row[1] == "Orl�ans":
                        conn.execute(update(District).where(District.id == row[0]).values(fedname="Orléans"))
                        print(f"[{row[0]}:{row[1]}] was updated to 'Orléans'")
                    elif row[1] == "Pierre-Boucher--Les Patriotes--Verch�res":
                        conn.execute(update(District).where(District.id == row[0]).values(fedname="Pierre-Boucher--Les Patriotes--Verchères"))
                        print(f"[{row[0]}:{row[1]}] was updated to 'Pierre-Boucher--Les Patriotes--Verchères'")
                    elif row[1] == "Qu�bec":
                        conn.execute(update(District).where(District.id == row[0]).values(fedname="Québec"))
                        print(f"[{row[0]}:{row[1]}] was updated to 'Québec'")
                    elif row[1] == "Rimouski-Neigette--T�miscouata--Les Basques":
                        conn.execute(update(District).where(District.id == row[0]).values(fedname="Rimouski-Neigette--Témiscouata--Les Basques"))
                        print(f"[{row[0]}:{row[1]}] was updated to 'Rimouski-Neigette--Témiscouata--Les Basques'")
                    elif row[1] == "Rivi�re-des-Mille-�les":
                        conn.execute(update(District).where(District.id == row[0]).values(fedname="Rivière-des-Mille-Îles"))
                        print(f"[{row[0]}:{row[1]}] was updated to 'Rivière-des-Mille-Îles'")
                    elif row[1] == "Rivi�re-du-Nord":
                        conn.execute(update(District).where(District.id == row[0]).values(fedname="Rivière-du-Nord"))
                        print(f"[{row[0]}:{row[1]}] was updated to 'Rivière-du-Nord'")
                    elif row[1] == "Saint-L�onard--Saint-Michel":
                        conn.execute(update(District).where(District.id == row[0]).values(fedname="Saint-Léonard--Saint-Michel"))
                        print(f"[{row[0]}:{row[1]}] was updated to 'Saint-Léonard--Saint-Michel'")
                    elif row[1] == "Salaberry--Suro�t":
                        conn.execute(update(District).where(District.id == row[0]).values(fedname="Salaberry--Suroît"))
                        print(f"[{row[0]}:{row[1]}] was updated to 'Salaberry--Suroît'")
                    elif row[1] == "Th�r�se-De Blainville":
                        conn.execute(update(District).where(District.id == row[0]).values(fedname="Thérèse-De Blainville"))
                        print(f"[{row[0]}:{row[1]}] was updated to 'Thérèse-De Blainville'")
                    elif row[1] == "Ville-Marie--Le Sud-Ouest--�le-des-Soeurs":
                        conn.execute(update(District).where(District.id == row[0]).values(fedname="Ville-Marie--Le Sud-Ouest--Île-des-Soeurs"))
                        print(f"[{row[0]}:{row[1]}] was updated to 'Ville-Marie--Le Sud-Ouest--Île-des-Soeurs'")
                    elif row[1] == "Trois-Rivi�res":
                        conn.execute(update(District).where(District.id == row[0]).values(fedname="Trois-Rivières"))
                        print(f"[{row[0]}:{row[1]}] was updated to 'Trois-Rivières'")
                    elif row[1] == "Berthier--Maskinong�":
                        conn.execute(update(District).where(District.id == row[0]).values(fedname="Berthier--Maskinongé"))
                        print(f"[{row[0]}:{row[1]}] was updated to 'Berthier--Maskinongé'")
                    elif row[1] == "Jonqui�re":
                        conn.execute(update(District).where(District.id == row[0]).values(fedname="Jonquière"))
                        print(f"[{row[0]}:{row[1]}] was updated to 'Jonquière'")
                    elif row[1] == "Louis-H�bert":
                        conn.execute(update(District).where(District.id == row[0]).values(fedname="Louis-Hébert"))
                        print(f"[{row[0]}:{row[1]}] was updated to 'Louis-Hébert'")

            

    engine.dispose()


# def print_fedname_and_constituencies(shapefile_path: str, csv_file_path: str):

#     shp_file = gpd.read_file(shapefile_path, encoding="UTF-8")
#     csv_file = pd.read_csv(csv_file_path)

#     combined_dataframe = pd.DataFrame()

#     combined_dataframe['Constituency'] = csv_file['Constituency']
#     combined_dataframe['fedname'] = shp_file['fedname']


#     pd.set_option('display.max_rows', None)
#     pd.set_option('display.max_columns', None)
#     print(combined_dataframe)


############################# UPLOAD ELECTION SHAPEFILES STARTING HERE #############################

def upload_1867_districts():
    ELECTION_YEAR = "1867"
    ELECTION_ID = 1
    BOUNDARY_VERSION_ID = 1
    NEW_SHAPEFILE_PATH = "./simplified_district_data/Canada" + ELECTION_YEAR + ".gpkg"
    starting_id_column_number = 283
    rows_to_keep = 186                     ## CAN BE SET TO None
    fedid_of_incorrect_districts = 59000   ## CAN BE SET TO None

    ### CREATE ELECTION IN DATABASE
    create_election_in_database(ELECTION_ID, int(ELECTION_YEAR), BOUNDARY_VERSION_ID)

    #### TO UPLOAD JUST PROVINCE AND NAME OF DISTRICTS
    shapefile_path = "districts2/CBF_RO" + ELECTION_YEAR + "_CSRS.shp"

    simplify_and_save_shp_file(shapefile_path, ELECTION_YEAR, ELECTION_ID, rows_to_keep, fedid_of_incorrect_districts, BOUNDARY_VERSION_ID)

    ### UPLOADS SHAPEFILE TO LOCAL POSTGRES
    upload_shapefile_to_postgres(NEW_SHAPEFILE_PATH, ELECTION_ID, ELECTION_YEAR)

    fix_district_names_in_postgres(ELECTION_ID)


def upload_1872_districts():
    ELECTION_YEAR = "1872"
    ELECTION_ID = 2
    BOUNDARY_VERSION_ID = 2
    NEW_SHAPEFILE_PATH = "./simplified_district_data/Canada" + ELECTION_YEAR + ".gpkg"
    starting_id_column_number = 464
    rows_to_keep = None                     ## CAN BE SET TO None
    fedid_of_incorrect_districts = 11999   ## CAN BE SET TO None

    ### CREATE ELECTION IN DATABASE
    create_election_in_database(ELECTION_ID, int(ELECTION_YEAR), BOUNDARY_VERSION_ID)

    #### TO UPLOAD JUST PROVINCE AND NAME OF DISTRICTS
    shapefile_path = "districts2/CBF_RO" + ELECTION_YEAR + "_CSRS.shp"

    simplify_and_save_shp_file(shapefile_path, ELECTION_YEAR, ELECTION_ID, rows_to_keep, fedid_of_incorrect_districts, BOUNDARY_VERSION_ID)

    ### UPLOADS SHAPEFILE TO LOCAL POSTGRES
    upload_shapefile_to_postgres(NEW_SHAPEFILE_PATH, ELECTION_ID, ELECTION_YEAR)

    fix_district_names_in_postgres(ELECTION_ID)


def upload_1874_districts():
    ELECTION_YEAR = "1874"
    ELECTION_ID = 3
    BOUNDARY_VERSION_ID = 2
    NEW_SHAPEFILE_PATH = "./simplified_district_data/Canada" + ELECTION_YEAR + ".gpkg"
    starting_id_column_number = 657
    rows_to_keep = None                     ## CAN BE SET TO None
    fedid_of_incorrect_districts = None   ## CAN BE SET TO None

    ### CREATE ELECTION IN DATABASE
    create_election_in_database(ELECTION_ID, int(ELECTION_YEAR), BOUNDARY_VERSION_ID)

    #### TO UPLOAD JUST PROVINCE AND NAME OF DISTRICTS
    shapefile_path = "districts2/CBF_RO1872_CSRS.shp"

    simplify_and_save_shp_file(shapefile_path, ELECTION_YEAR, ELECTION_ID, rows_to_keep, fedid_of_incorrect_districts, BOUNDARY_VERSION_ID)

    ### UPLOADS SHAPEFILE TO LOCAL POSTGRES
    upload_shapefile_to_postgres(NEW_SHAPEFILE_PATH, ELECTION_ID, ELECTION_YEAR)

    fix_district_names_in_postgres(ELECTION_ID)


def upload_1878_districts():
    ELECTION_YEAR = "1878"
    ELECTION_ID = 4
    BOUNDARY_VERSION_ID = 2
    NEW_SHAPEFILE_PATH = "./simplified_district_data/Canada" + ELECTION_YEAR + ".gpkg"
    rows_to_keep = None                     ## CAN BE SET TO None
    fedid_of_incorrect_districts = None   ## CAN BE SET TO None

    ### CREATE ELECTION IN DATABASE
    create_election_in_database(ELECTION_ID, int(ELECTION_YEAR), BOUNDARY_VERSION_ID)

    #### TO UPLOAD JUST PROVINCE AND NAME OF DISTRICTS
    shapefile_path = "districts2/CBF_RO1872_CSRS.shp"

    simplify_and_save_shp_file(shapefile_path, ELECTION_YEAR, ELECTION_ID, rows_to_keep, fedid_of_incorrect_districts, BOUNDARY_VERSION_ID)

    ### UPLOADS SHAPEFILE TO LOCAL POSTGRES
    upload_shapefile_to_postgres(NEW_SHAPEFILE_PATH, ELECTION_ID, ELECTION_YEAR)

    fix_district_names_in_postgres(ELECTION_ID)


def upload_1882_districts():
    ELECTION_YEAR = "1882"
    ELECTION_ID = 5
    BOUNDARY_VERSION_ID = 3
    NEW_SHAPEFILE_PATH = "./simplified_district_data/Canada" + ELECTION_YEAR + ".gpkg"
    rows_to_keep = None                     ## CAN BE SET TO None
    fedid_of_incorrect_districts = 60999   ## CAN BE SET TO None

    ### CREATE ELECTION IN DATABASE
    create_election_in_database(ELECTION_ID, int(ELECTION_YEAR), BOUNDARY_VERSION_ID)

    #### TO UPLOAD JUST PROVINCE AND NAME OF DISTRICTS
    shapefile_path = "districts2/CBF_RO1882_CSRS.shp"

    simplify_and_save_shp_file(shapefile_path, ELECTION_YEAR, ELECTION_ID, rows_to_keep, fedid_of_incorrect_districts, BOUNDARY_VERSION_ID)

    ### UPLOADS SHAPEFILE TO LOCAL POSTGRES
    upload_shapefile_to_postgres(NEW_SHAPEFILE_PATH, ELECTION_ID, ELECTION_YEAR)

    fix_district_names_in_postgres(ELECTION_ID)


def upload_1887_districts():
    ELECTION_YEAR = "1887"
    ELECTION_ID = 6
    BOUNDARY_VERSION_ID = 3
    NEW_SHAPEFILE_PATH = "./simplified_district_data/Canada" + ELECTION_YEAR + ".gpkg"
    rows_to_keep = None                     ## CAN BE SET TO None
    fedid_of_incorrect_districts = None   ## CAN BE SET TO None

    ### CREATE ELECTION IN DATABASE
    create_election_in_database(ELECTION_ID, int(ELECTION_YEAR), BOUNDARY_VERSION_ID)

    #### TO UPLOAD JUST PROVINCE AND NAME OF DISTRICTS
    shapefile_path = "districts2/CBF_RO1882_CSRS.shp"

    simplify_and_save_shp_file(shapefile_path, ELECTION_YEAR, ELECTION_ID, rows_to_keep, fedid_of_incorrect_districts, BOUNDARY_VERSION_ID)

    ### UPLOADS SHAPEFILE TO LOCAL POSTGRES
    upload_shapefile_to_postgres(NEW_SHAPEFILE_PATH, ELECTION_ID, ELECTION_YEAR)

    fix_district_names_in_postgres(ELECTION_ID)


def upload_1891_districts():
    ELECTION_YEAR = "1891"
    ELECTION_ID = 7
    BOUNDARY_VERSION_ID = 3
    NEW_SHAPEFILE_PATH = "./simplified_district_data/Canada" + ELECTION_YEAR + ".gpkg"
    rows_to_keep = None                     ## CAN BE SET TO None
    fedid_of_incorrect_districts = None   ## CAN BE SET TO None

    ### CREATE ELECTION IN DATABASE
    create_election_in_database(ELECTION_ID, int(ELECTION_YEAR), BOUNDARY_VERSION_ID)

    #### TO UPLOAD JUST PROVINCE AND NAME OF DISTRICTS
    shapefile_path = "districts2/CBF_RO1882_CSRS.shp"

    simplify_and_save_shp_file(shapefile_path, ELECTION_YEAR, ELECTION_ID, rows_to_keep, fedid_of_incorrect_districts, BOUNDARY_VERSION_ID)

    ### UPLOADS SHAPEFILE TO LOCAL POSTGRES
    upload_shapefile_to_postgres(NEW_SHAPEFILE_PATH, ELECTION_ID, ELECTION_YEAR)

    fix_district_names_in_postgres(ELECTION_ID)


def upload_1896_districts():
    ELECTION_YEAR = "1896"
    ELECTION_ID = 8
    BOUNDARY_VERSION_ID = 4
    NEW_SHAPEFILE_PATH = "./simplified_district_data/Canada" + ELECTION_YEAR + ".gpkg"
    rows_to_keep = None                     ## CAN BE SET TO None
    fedid_of_incorrect_districts = 60001   ## CAN BE SET TO None

    ### CREATE ELECTION IN DATABASE
    create_election_in_database(ELECTION_ID, int(ELECTION_YEAR), BOUNDARY_VERSION_ID)

    #### TO UPLOAD JUST PROVINCE AND NAME OF DISTRICTS
    shapefile_path = "districts2/CBF_RO1892_CSRS.shp"

    simplify_and_save_shp_file(shapefile_path, ELECTION_YEAR, ELECTION_ID, rows_to_keep, fedid_of_incorrect_districts, BOUNDARY_VERSION_ID)

    ### UPLOADS SHAPEFILE TO LOCAL POSTGRES
    upload_shapefile_to_postgres(NEW_SHAPEFILE_PATH, ELECTION_ID, ELECTION_YEAR)

    fix_district_names_in_postgres(ELECTION_ID)


def upload_1900_districts():
    ELECTION_YEAR = "1900"
    ELECTION_ID = 9
    BOUNDARY_VERSION_ID = 4
    NEW_SHAPEFILE_PATH = "./simplified_district_data/Canada" + ELECTION_YEAR + ".gpkg"
    rows_to_keep = None                     ## CAN BE SET TO None
    fedid_of_incorrect_districts = 60001   ## CAN BE SET TO None

    ### CREATE ELECTION IN DATABASE
    create_election_in_database(ELECTION_ID, int(ELECTION_YEAR), BOUNDARY_VERSION_ID)

    #### TO UPLOAD JUST PROVINCE AND NAME OF DISTRICTS
    shapefile_path = "districts2/CBF_RO1892_CSRS.shp"

    simplify_and_save_shp_file(shapefile_path, ELECTION_YEAR, ELECTION_ID, rows_to_keep, fedid_of_incorrect_districts, BOUNDARY_VERSION_ID)

    ### UPLOADS SHAPEFILE TO LOCAL POSTGRES
    upload_shapefile_to_postgres(NEW_SHAPEFILE_PATH, ELECTION_ID, ELECTION_YEAR)

    fix_district_names_in_postgres(ELECTION_ID)


def upload_1904_districts():
    ELECTION_YEAR = "1904"
    ELECTION_ID = 10
    BOUNDARY_VERSION_ID = 6
    NEW_SHAPEFILE_PATH = "./simplified_district_data/Canada" + ELECTION_YEAR + ".gpkg"
    rows_to_keep = None                     ## CAN BE SET TO None
    fedid_of_incorrect_districts = None   ## CAN BE SET TO None

    ### CREATE ELECTION IN DATABASE
    create_election_in_database(ELECTION_ID, int(ELECTION_YEAR), BOUNDARY_VERSION_ID)

    #### TO UPLOAD JUST PROVINCE AND NAME OF DISTRICTS
    shapefile_path = "districts2/CBF_RO1903_CSRS.shp"

    simplify_and_save_shp_file(shapefile_path, ELECTION_YEAR, ELECTION_ID, rows_to_keep, fedid_of_incorrect_districts, BOUNDARY_VERSION_ID)

    ### UPLOADS SHAPEFILE TO LOCAL POSTGRES
    upload_shapefile_to_postgres(NEW_SHAPEFILE_PATH, ELECTION_ID, ELECTION_YEAR)

    fix_district_names_in_postgres(ELECTION_ID)


def upload_1908_districts():
    ELECTION_YEAR = "1908"
    ELECTION_ID = 11
    BOUNDARY_VERSION_ID = 6
    NEW_SHAPEFILE_PATH = "./simplified_district_data/Canada" + ELECTION_YEAR + ".gpkg"
    rows_to_keep = None                     ## CAN BE SET TO None
    fedid_of_incorrect_districts = None   ## CAN BE SET TO None

    ### CREATE ELECTION IN DATABASE
    create_election_in_database(ELECTION_ID, int(ELECTION_YEAR), BOUNDARY_VERSION_ID)

    #### TO UPLOAD JUST PROVINCE AND NAME OF DISTRICTS
    shapefile_path = "districts2/CBF_RO1905_CSRS.shp"

    simplify_and_save_shp_file(shapefile_path, ELECTION_YEAR, ELECTION_ID, rows_to_keep, fedid_of_incorrect_districts, BOUNDARY_VERSION_ID)

    ### UPLOADS SHAPEFILE TO LOCAL POSTGRES
    upload_shapefile_to_postgres(NEW_SHAPEFILE_PATH, ELECTION_ID, ELECTION_YEAR)

    fix_district_names_in_postgres(ELECTION_ID)


def upload_1911_districts():
    ELECTION_YEAR = "1911"
    ELECTION_ID = 12
    BOUNDARY_VERSION_ID = 6
    NEW_SHAPEFILE_PATH = "./simplified_district_data/Canada" + ELECTION_YEAR + ".gpkg"
    rows_to_keep = None                     ## CAN BE SET TO None
    fedid_of_incorrect_districts = None   ## CAN BE SET TO None

    ### CREATE ELECTION IN DATABASE
    create_election_in_database(ELECTION_ID, int(ELECTION_YEAR), BOUNDARY_VERSION_ID)

    #### TO UPLOAD JUST PROVINCE AND NAME OF DISTRICTS
    shapefile_path = "districts2/CBF_RO1905_CSRS.shp"

    simplify_and_save_shp_file(shapefile_path, ELECTION_YEAR, ELECTION_ID, rows_to_keep, fedid_of_incorrect_districts, BOUNDARY_VERSION_ID)

    ### UPLOADS SHAPEFILE TO LOCAL POSTGRES
    upload_shapefile_to_postgres(NEW_SHAPEFILE_PATH, ELECTION_ID, ELECTION_YEAR)

    fix_district_names_in_postgres(ELECTION_ID)


def upload_1917_districts():
    ELECTION_YEAR = "1917"
    ELECTION_ID = 13
    BOUNDARY_VERSION_ID = 7
    NEW_SHAPEFILE_PATH = "./simplified_district_data/Canada" + ELECTION_YEAR + ".gpkg"
    rows_to_keep = None                     ## CAN BE SET TO None
    fedid_of_incorrect_districts = None   ## CAN BE SET TO None

    ### CREATE ELECTION IN DATABASE
    create_election_in_database(ELECTION_ID, int(ELECTION_YEAR), BOUNDARY_VERSION_ID)

    #### TO UPLOAD JUST PROVINCE AND NAME OF DISTRICTS
    shapefile_path = "districts2/CBF_RO1914_CSRS.shp"

    simplify_and_save_shp_file(shapefile_path, ELECTION_YEAR, ELECTION_ID, rows_to_keep, fedid_of_incorrect_districts, BOUNDARY_VERSION_ID)

    ### UPLOADS SHAPEFILE TO LOCAL POSTGRES
    upload_shapefile_to_postgres(NEW_SHAPEFILE_PATH, ELECTION_ID, ELECTION_YEAR)

    fix_district_names_in_postgres(ELECTION_ID)


def upload_1921_districts():
    ELECTION_YEAR = "1921"
    ELECTION_ID = 14
    BOUNDARY_VERSION_ID = 7
    NEW_SHAPEFILE_PATH = "./simplified_district_data/Canada" + ELECTION_YEAR + ".gpkg"
    rows_to_keep = None                     ## CAN BE SET TO None
    fedid_of_incorrect_districts = None   ## CAN BE SET TO None

    ### CREATE ELECTION IN DATABASE
    create_election_in_database(ELECTION_ID, int(ELECTION_YEAR), BOUNDARY_VERSION_ID)

    #### TO UPLOAD JUST PROVINCE AND NAME OF DISTRICTS
    shapefile_path = "districts2/CBF_RO1914_CSRS.shp"

    simplify_and_save_shp_file(shapefile_path, ELECTION_YEAR, ELECTION_ID, rows_to_keep, fedid_of_incorrect_districts, BOUNDARY_VERSION_ID)

    ### UPLOADS SHAPEFILE TO LOCAL POSTGRES
    upload_shapefile_to_postgres(NEW_SHAPEFILE_PATH, ELECTION_ID, ELECTION_YEAR)

    fix_district_names_in_postgres(ELECTION_ID)


def upload_1925_districts():
    ELECTION_YEAR = "1925"
    ELECTION_ID = 15
    BOUNDARY_VERSION_ID = 8
    NEW_SHAPEFILE_PATH = "./simplified_district_data/Canada" + ELECTION_YEAR + ".gpkg"
    rows_to_keep = None                     ## CAN BE SET TO None
    fedid_of_incorrect_districts = None   ## CAN BE SET TO None

    ### CREATE ELECTION IN DATABASE
    create_election_in_database(ELECTION_ID, int(ELECTION_YEAR), BOUNDARY_VERSION_ID)

    #### TO UPLOAD JUST PROVINCE AND NAME OF DISTRICTS
    shapefile_path = "districts2/CBF_RO1924_CSRS.shp"

    simplify_and_save_shp_file(shapefile_path, ELECTION_YEAR, ELECTION_ID, rows_to_keep, fedid_of_incorrect_districts, BOUNDARY_VERSION_ID)

    ### UPLOADS SHAPEFILE TO LOCAL POSTGRES
    upload_shapefile_to_postgres(NEW_SHAPEFILE_PATH, ELECTION_ID, ELECTION_YEAR)

    fix_district_names_in_postgres(ELECTION_ID)

def upload_1926_districts():
    ELECTION_YEAR = "1926"
    ELECTION_ID = 16
    BOUNDARY_VERSION_ID = 8
    NEW_SHAPEFILE_PATH = "./simplified_district_data/Canada" + ELECTION_YEAR + ".gpkg"
    rows_to_keep = None                     ## CAN BE SET TO None
    fedid_of_incorrect_districts = None   ## CAN BE SET TO None

    ### CREATE ELECTION IN DATABASE
    create_election_in_database(ELECTION_ID, int(ELECTION_YEAR), BOUNDARY_VERSION_ID)

    #### TO UPLOAD JUST PROVINCE AND NAME OF DISTRICTS
    shapefile_path = "districts2/CBF_RO1924_CSRS.shp"

    simplify_and_save_shp_file(shapefile_path, ELECTION_YEAR, ELECTION_ID, rows_to_keep, fedid_of_incorrect_districts, BOUNDARY_VERSION_ID)

    ### UPLOADS SHAPEFILE TO LOCAL POSTGRES
    upload_shapefile_to_postgres(NEW_SHAPEFILE_PATH, ELECTION_ID, ELECTION_YEAR)

    fix_district_names_in_postgres(ELECTION_ID)


def upload_1930_districts():
    ELECTION_YEAR = "1930"
    ELECTION_ID = 17
    BOUNDARY_VERSION_ID = 8
    NEW_SHAPEFILE_PATH = "./simplified_district_data/Canada" + ELECTION_YEAR + ".gpkg"
    rows_to_keep = None                     ## CAN BE SET TO None
    fedid_of_incorrect_districts = None   ## CAN BE SET TO None

    ### CREATE ELECTION IN DATABASE
    create_election_in_database(ELECTION_ID, int(ELECTION_YEAR), BOUNDARY_VERSION_ID)

    #### TO UPLOAD JUST PROVINCE AND NAME OF DISTRICTS
    shapefile_path = "districts2/CBF_RO1924_CSRS.shp"

    simplify_and_save_shp_file(shapefile_path, ELECTION_YEAR, ELECTION_ID, rows_to_keep, fedid_of_incorrect_districts, BOUNDARY_VERSION_ID)

    ### UPLOADS SHAPEFILE TO LOCAL POSTGRES
    upload_shapefile_to_postgres(NEW_SHAPEFILE_PATH, ELECTION_ID, ELECTION_YEAR)

    fix_district_names_in_postgres(ELECTION_ID)


def upload_1935_districts():
    ELECTION_YEAR = "1935"
    ELECTION_ID = 18
    BOUNDARY_VERSION_ID = 9
    NEW_SHAPEFILE_PATH = "./simplified_district_data/Canada" + ELECTION_YEAR + ".gpkg"
    rows_to_keep = None                     ## CAN BE SET TO None
    fedid_of_incorrect_districts = None   ## CAN BE SET TO None

    ### CREATE ELECTION IN DATABASE
    create_election_in_database(ELECTION_ID, int(ELECTION_YEAR), BOUNDARY_VERSION_ID)

    #### TO UPLOAD JUST PROVINCE AND NAME OF DISTRICTS
    shapefile_path = "districts2/CBF_RO1933_CSRS.shp"

    simplify_and_save_shp_file(shapefile_path, ELECTION_YEAR, ELECTION_ID, rows_to_keep, fedid_of_incorrect_districts, BOUNDARY_VERSION_ID)

    ### UPLOADS SHAPEFILE TO LOCAL POSTGRES
    upload_shapefile_to_postgres(NEW_SHAPEFILE_PATH, ELECTION_ID, ELECTION_YEAR)

    fix_district_names_in_postgres(ELECTION_ID)


def upload_1940_districts():
    ELECTION_YEAR = "1940"
    ELECTION_ID = 19
    BOUNDARY_VERSION_ID = 9
    NEW_SHAPEFILE_PATH = "./simplified_district_data/Canada" + ELECTION_YEAR + ".gpkg"
    rows_to_keep = None                     ## CAN BE SET TO None
    fedid_of_incorrect_districts = None   ## CAN BE SET TO None

    ### CREATE ELECTION IN DATABASE
    create_election_in_database(ELECTION_ID, int(ELECTION_YEAR), BOUNDARY_VERSION_ID)

    #### TO UPLOAD JUST PROVINCE AND NAME OF DISTRICTS
    shapefile_path = "districts2/CBF_RO1933_CSRS.shp"

    simplify_and_save_shp_file(shapefile_path, ELECTION_YEAR, ELECTION_ID, rows_to_keep, fedid_of_incorrect_districts, BOUNDARY_VERSION_ID)

    ### UPLOADS SHAPEFILE TO LOCAL POSTGRES
    upload_shapefile_to_postgres(NEW_SHAPEFILE_PATH, ELECTION_ID, ELECTION_YEAR)

    fix_district_names_in_postgres(ELECTION_ID)


def upload_1945_districts():
    ELECTION_YEAR = "1945"
    ELECTION_ID = 20
    BOUNDARY_VERSION_ID = 9
    NEW_SHAPEFILE_PATH = "./simplified_district_data/Canada" + ELECTION_YEAR + ".gpkg"
    rows_to_keep = None                     ## CAN BE SET TO None
    fedid_of_incorrect_districts = None   ## CAN BE SET TO None

    ### CREATE ELECTION IN DATABASE
    create_election_in_database(ELECTION_ID, int(ELECTION_YEAR), BOUNDARY_VERSION_ID)

    #### TO UPLOAD JUST PROVINCE AND NAME OF DISTRICTS
    shapefile_path = "districts2/CBF_RO1933_CSRS.shp"

    simplify_and_save_shp_file(shapefile_path, ELECTION_YEAR, ELECTION_ID, rows_to_keep, fedid_of_incorrect_districts, BOUNDARY_VERSION_ID)

    ### UPLOADS SHAPEFILE TO LOCAL POSTGRES
    upload_shapefile_to_postgres(NEW_SHAPEFILE_PATH, ELECTION_ID, ELECTION_YEAR)

    fix_district_names_in_postgres(ELECTION_ID)


def upload_1949_districts():
    ELECTION_YEAR = "1949"
    ELECTION_ID = 21
    BOUNDARY_VERSION_ID = 10
    NEW_SHAPEFILE_PATH = "./simplified_district_data/Canada" + ELECTION_YEAR + ".gpkg"
    rows_to_keep = None                     ## CAN BE SET TO None
    fedid_of_incorrect_districts = None   ## CAN BE SET TO None

    ### CREATE ELECTION IN DATABASE
    create_election_in_database(ELECTION_ID, int(ELECTION_YEAR), BOUNDARY_VERSION_ID)

    #### TO UPLOAD JUST PROVINCE AND NAME OF DISTRICTS
    shapefile_path = "districts2/CBF_RO1947_CSRS.shp"

    simplify_and_save_shp_file(shapefile_path, ELECTION_YEAR, ELECTION_ID, rows_to_keep, fedid_of_incorrect_districts, BOUNDARY_VERSION_ID)

    ### UPLOADS SHAPEFILE TO LOCAL POSTGRES
    upload_shapefile_to_postgres(NEW_SHAPEFILE_PATH, ELECTION_ID, ELECTION_YEAR)

    fix_district_names_in_postgres(ELECTION_ID)


def upload_1953_districts():
    ELECTION_YEAR = "1953"
    ELECTION_ID = 22
    BOUNDARY_VERSION_ID = 11
    NEW_SHAPEFILE_PATH = "./simplified_district_data/Canada" + ELECTION_YEAR + ".gpkg"
    rows_to_keep = None                     ## CAN BE SET TO None
    fedid_of_incorrect_districts = None   ## CAN BE SET TO None

    ### CREATE ELECTION IN DATABASE
    create_election_in_database(ELECTION_ID, int(ELECTION_YEAR), BOUNDARY_VERSION_ID)

    #### TO UPLOAD JUST PROVINCE AND NAME OF DISTRICTS
    shapefile_path = "districts2/CBF_RO1952_CSRS.shp"

    simplify_and_save_shp_file(shapefile_path, ELECTION_YEAR, ELECTION_ID, rows_to_keep, fedid_of_incorrect_districts, BOUNDARY_VERSION_ID)

    ### UPLOADS SHAPEFILE TO LOCAL POSTGRES
    upload_shapefile_to_postgres(NEW_SHAPEFILE_PATH, ELECTION_ID, ELECTION_YEAR)

    fix_district_names_in_postgres(ELECTION_ID)


def upload_1957_districts():
    ELECTION_YEAR = "1957"
    ELECTION_ID = 23
    BOUNDARY_VERSION_ID = 11
    NEW_SHAPEFILE_PATH = "./simplified_district_data/Canada" + ELECTION_YEAR + ".gpkg"
    rows_to_keep = None                     ## CAN BE SET TO None
    fedid_of_incorrect_districts = None   ## CAN BE SET TO None

    ### CREATE ELECTION IN DATABASE
    create_election_in_database(ELECTION_ID, int(ELECTION_YEAR), BOUNDARY_VERSION_ID)

    #### TO UPLOAD JUST PROVINCE AND NAME OF DISTRICTS
    shapefile_path = "districts2/CBF_RO1952_CSRS.shp"

    simplify_and_save_shp_file(shapefile_path, ELECTION_YEAR, ELECTION_ID, rows_to_keep, fedid_of_incorrect_districts, BOUNDARY_VERSION_ID)

    ### UPLOADS SHAPEFILE TO LOCAL POSTGRES
    upload_shapefile_to_postgres(NEW_SHAPEFILE_PATH, ELECTION_ID, ELECTION_YEAR)

    fix_district_names_in_postgres(ELECTION_ID)


def upload_1958_districts():
    ELECTION_YEAR = "1958"
    ELECTION_ID = 24
    BOUNDARY_VERSION_ID = 11
    NEW_SHAPEFILE_PATH = "./simplified_district_data/Canada" + ELECTION_YEAR + ".gpkg"
    rows_to_keep = None                     ## CAN BE SET TO None
    fedid_of_incorrect_districts = None   ## CAN BE SET TO None

    ### CREATE ELECTION IN DATABASE
    create_election_in_database(ELECTION_ID, int(ELECTION_YEAR), BOUNDARY_VERSION_ID)

    #### TO UPLOAD JUST PROVINCE AND NAME OF DISTRICTS
    shapefile_path = "districts2/CBF_RO1952_CSRS.shp"

    simplify_and_save_shp_file(shapefile_path, ELECTION_YEAR, ELECTION_ID, rows_to_keep, fedid_of_incorrect_districts, BOUNDARY_VERSION_ID)

    ### UPLOADS SHAPEFILE TO LOCAL POSTGRES
    upload_shapefile_to_postgres(NEW_SHAPEFILE_PATH, ELECTION_ID, ELECTION_YEAR)

    fix_district_names_in_postgres(ELECTION_ID)


def upload_1962_districts():
    ELECTION_YEAR = "1962"
    ELECTION_ID = 25
    BOUNDARY_VERSION_ID = 11
    NEW_SHAPEFILE_PATH = "./simplified_district_data/Canada" + ELECTION_YEAR + ".gpkg"
    rows_to_keep = None                     ## CAN BE SET TO None
    fedid_of_incorrect_districts = None   ## CAN BE SET TO None

    ### CREATE ELECTION IN DATABASE
    create_election_in_database(ELECTION_ID, int(ELECTION_YEAR), BOUNDARY_VERSION_ID)

    #### TO UPLOAD JUST PROVINCE AND NAME OF DISTRICTS
    shapefile_path = "districts2/CBF_RO1952_CSRS.shp"

    simplify_and_save_shp_file(shapefile_path, ELECTION_YEAR, ELECTION_ID, rows_to_keep, fedid_of_incorrect_districts, BOUNDARY_VERSION_ID)

    ### UPLOADS SHAPEFILE TO LOCAL POSTGRES
    upload_shapefile_to_postgres(NEW_SHAPEFILE_PATH, ELECTION_ID, ELECTION_YEAR)

    fix_district_names_in_postgres(ELECTION_ID)


def upload_1963_districts():
    ELECTION_YEAR = "1963"
    ELECTION_ID = 26
    BOUNDARY_VERSION_ID = 11
    NEW_SHAPEFILE_PATH = "./simplified_district_data/Canada" + ELECTION_YEAR + ".gpkg"
    rows_to_keep = None                     ## CAN BE SET TO None
    fedid_of_incorrect_districts = None   ## CAN BE SET TO None

    ### CREATE ELECTION IN DATABASE
    create_election_in_database(ELECTION_ID, int(ELECTION_YEAR), BOUNDARY_VERSION_ID)

    #### TO UPLOAD JUST PROVINCE AND NAME OF DISTRICTS
    shapefile_path = "districts2/CBF_RO1952_CSRS.shp"

    simplify_and_save_shp_file(shapefile_path, ELECTION_YEAR, ELECTION_ID, rows_to_keep, fedid_of_incorrect_districts, BOUNDARY_VERSION_ID)

    ### UPLOADS SHAPEFILE TO LOCAL POSTGRES
    upload_shapefile_to_postgres(NEW_SHAPEFILE_PATH, ELECTION_ID, ELECTION_YEAR)

    fix_district_names_in_postgres(ELECTION_ID)


def upload_1965_districts():
    ELECTION_YEAR = "1965"
    ELECTION_ID = 27
    BOUNDARY_VERSION_ID = 11
    NEW_SHAPEFILE_PATH = "./simplified_district_data/Canada" + ELECTION_YEAR + ".gpkg"
    rows_to_keep = None                     ## CAN BE SET TO None
    fedid_of_incorrect_districts = None   ## CAN BE SET TO None

    ### CREATE ELECTION IN DATABASE
    create_election_in_database(ELECTION_ID, int(ELECTION_YEAR), BOUNDARY_VERSION_ID)

    #### TO UPLOAD JUST PROVINCE AND NAME OF DISTRICTS
    shapefile_path = "districts2/CBF_RO1952_CSRS.shp"

    simplify_and_save_shp_file(shapefile_path, ELECTION_YEAR, ELECTION_ID, rows_to_keep, fedid_of_incorrect_districts, BOUNDARY_VERSION_ID)

    ### UPLOADS SHAPEFILE TO LOCAL POSTGRES
    upload_shapefile_to_postgres(NEW_SHAPEFILE_PATH, ELECTION_ID, ELECTION_YEAR)

    fix_district_names_in_postgres(ELECTION_ID)


def upload_1968_districts():
    ELECTION_YEAR = "1968"
    ELECTION_ID = 28
    BOUNDARY_VERSION_ID = 12
    NEW_SHAPEFILE_PATH = "./simplified_district_data/Canada" + ELECTION_YEAR + ".gpkg"
    rows_to_keep = None                     ## CAN BE SET TO None
    fedid_of_incorrect_districts = None   ## CAN BE SET TO None

    ### CREATE ELECTION IN DATABASE
    create_election_in_database(ELECTION_ID, int(ELECTION_YEAR), BOUNDARY_VERSION_ID)

    #### TO UPLOAD JUST PROVINCE AND NAME OF DISTRICTS
    shapefile_path = "districts2/CBF_RO1966_CSRS.shp"

    simplify_and_save_shp_file(shapefile_path, ELECTION_YEAR, ELECTION_ID, rows_to_keep, fedid_of_incorrect_districts, BOUNDARY_VERSION_ID)

    ### UPLOADS SHAPEFILE TO LOCAL POSTGRES
    upload_shapefile_to_postgres(NEW_SHAPEFILE_PATH, ELECTION_ID, ELECTION_YEAR)

    fix_district_names_in_postgres(ELECTION_ID)


def upload_1972_districts():
    ELECTION_YEAR = "1972"
    ELECTION_ID = 29
    BOUNDARY_VERSION_ID = 12
    NEW_SHAPEFILE_PATH = "./simplified_district_data/Canada" + ELECTION_YEAR + ".gpkg"
    rows_to_keep = None                     ## CAN BE SET TO None
    fedid_of_incorrect_districts = None   ## CAN BE SET TO None

    ### CREATE ELECTION IN DATABASE
    create_election_in_database(ELECTION_ID, int(ELECTION_YEAR), BOUNDARY_VERSION_ID)

    #### TO UPLOAD JUST PROVINCE AND NAME OF DISTRICTS
    shapefile_path = "districts2/CBF_RO1966_CSRS.shp"

    simplify_and_save_shp_file(shapefile_path, ELECTION_YEAR, ELECTION_ID, rows_to_keep, fedid_of_incorrect_districts, BOUNDARY_VERSION_ID)

    ### UPLOADS SHAPEFILE TO LOCAL POSTGRES
    upload_shapefile_to_postgres(NEW_SHAPEFILE_PATH, ELECTION_ID, ELECTION_YEAR)

    fix_district_names_in_postgres(ELECTION_ID)


def upload_1974_districts():
    ELECTION_YEAR = "1974"
    ELECTION_ID = 30
    BOUNDARY_VERSION_ID = 12
    NEW_SHAPEFILE_PATH = "./simplified_district_data/Canada" + ELECTION_YEAR + ".gpkg"
    rows_to_keep = None                     ## CAN BE SET TO None
    fedid_of_incorrect_districts = None   ## CAN BE SET TO None

    ### CREATE ELECTION IN DATABASE
    create_election_in_database(ELECTION_ID, int(ELECTION_YEAR), BOUNDARY_VERSION_ID)

    #### TO UPLOAD JUST PROVINCE AND NAME OF DISTRICTS
    shapefile_path = "districts2/CBF_RO1966_CSRS.shp"

    simplify_and_save_shp_file(shapefile_path, ELECTION_YEAR, ELECTION_ID, rows_to_keep, fedid_of_incorrect_districts, BOUNDARY_VERSION_ID)

    ### UPLOADS SHAPEFILE TO LOCAL POSTGRES
    upload_shapefile_to_postgres(NEW_SHAPEFILE_PATH, ELECTION_ID, ELECTION_YEAR)

    fix_district_names_in_postgres(ELECTION_ID)


def upload_1979_districts():
    ELECTION_YEAR = "1979"
    ELECTION_ID = 31
    BOUNDARY_VERSION_ID = 13
    NEW_SHAPEFILE_PATH = "./simplified_district_data/Canada" + ELECTION_YEAR + ".gpkg"
    rows_to_keep = None                     ## CAN BE SET TO None
    fedid_of_incorrect_districts = None   ## CAN BE SET TO None

    ### CREATE ELECTION IN DATABASE
    create_election_in_database(ELECTION_ID, int(ELECTION_YEAR), BOUNDARY_VERSION_ID)

    #### TO UPLOAD JUST PROVINCE AND NAME OF DISTRICTS
    shapefile_path = "districts2/CBF_RO1976_CSRS.shp"

    simplify_and_save_shp_file(shapefile_path, ELECTION_YEAR, ELECTION_ID, rows_to_keep, fedid_of_incorrect_districts, BOUNDARY_VERSION_ID)

    ### UPLOADS SHAPEFILE TO LOCAL POSTGRES
    upload_shapefile_to_postgres(NEW_SHAPEFILE_PATH, ELECTION_ID, ELECTION_YEAR)

    fix_district_names_in_postgres(ELECTION_ID)


def upload_2019_districts():
    ELECTION_YEAR = "2019"
    ELECTION_ID = 43
    BOUNDARY_VERSION_ID = 18
    NEW_SHAPEFILE_PATH = "./simplified_district_data/Canada" + ELECTION_YEAR + ".gpkg"
    rows_to_keep = None                     ## CAN BE SET TO None
    fedid_of_incorrect_districts = None   ## CAN BE SET TO None

    ### CREATE ELECTION IN DATABASE
    create_election_in_database(ELECTION_ID, int(ELECTION_YEAR), BOUNDARY_VERSION_ID)

    #### TO UPLOAD JUST PROVINCE AND NAME OF DISTRICTS
    shapefile_path = "districts2/CBF_RO2013_CSRS.shp"

    simplify_and_save_shp_file(shapefile_path, ELECTION_YEAR, ELECTION_ID, rows_to_keep, fedid_of_incorrect_districts, BOUNDARY_VERSION_ID)

    ### UPLOADS SHAPEFILE TO LOCAL POSTGRES
    upload_shapefile_to_postgres(NEW_SHAPEFILE_PATH, ELECTION_ID, ELECTION_YEAR)

    fix_district_names_in_postgres(ELECTION_ID)


def upload_2021_districts():
    ELECTION_YEAR = "2021"
    ELECTION_ID = 44
    BOUNDARY_VERSION_ID = 18
    NEW_SHAPEFILE_PATH = "./simplified_district_data/Canada" + ELECTION_YEAR + ".gpkg"
    rows_to_keep = None                     ## CAN BE SET TO None
    fedid_of_incorrect_districts = None   ## CAN BE SET TO None

    ### CREATE ELECTION IN DATABASE
    create_election_in_database(ELECTION_ID, int(ELECTION_YEAR), BOUNDARY_VERSION_ID)

    #### TO UPLOAD JUST PROVINCE AND NAME OF DISTRICTS
    shapefile_path = "districts2/CBF_RO2013_CSRS.shp"

    simplify_and_save_shp_file(shapefile_path, ELECTION_YEAR, ELECTION_ID, rows_to_keep, fedid_of_incorrect_districts, BOUNDARY_VERSION_ID)

    ### UPLOADS SHAPEFILE TO LOCAL POSTGRES
    upload_shapefile_to_postgres(NEW_SHAPEFILE_PATH, ELECTION_ID, ELECTION_YEAR)

    fix_district_names_in_postgres(ELECTION_ID)


def main():

    ELECTION_YEAR = "2021"
    ELECTION_ID = 44
    BOUNDARY_VERSION_ID = 18
    csv_file_path_original = 'voting_data/electionsCandidates' + ELECTION_YEAR + '.csv'
    csv_file_path_sorted = 'voting_data/electionsCandidates' + ELECTION_YEAR + '_sorted.csv'

    ## STEP 1: UPLOAD AND FIX DISTRICTS
    ### MAKE SURE THE DISTRICTS DO NOT EXIST ALREADY!
    upload_2021_districts()

    ### NEED TO SAVE electionsCandidates file to voting_data folder BEFORE proceeding!

    ## STEP 2: SORT AND CREATE NEW CSV FILE. Make sure to remove _sorted from the path!!!!!!!
    sort_csv_and_save_new_file(csv_file_path_original, ELECTION_YEAR)

    ## STEP 3: UPLOAD ANY NEW PARTIES
    upload_parties_to_postgres(csv_file_path_sorted, ELECTION_YEAR)

    ## STEP 4: POPULATE district_aliases TABLE
    populate_district_aliases_table(ELECTION_YEAR)

    ## STEP 5: UPLOAD CSV TO staging_table
    upload_csv_to_staging_table(csv_file_path_sorted, ELECTION_YEAR)
    
    ## STEP 6: UPLOAD CANDIDATES (uses staging_table)
    upload_candidates_to_postgres(ELECTION_ID, BOUNDARY_VERSION_ID, ELECTION_YEAR)

    ## STEP 7: INSERT VOTING DATA INTO RESULTS TABLE
    upload_results_to_postgres(ELECTION_ID, BOUNDARY_VERSION_ID, ELECTION_YEAR)


if __name__ == "__main__":
    main()

import pandas as pd

def load_and_process(url_or_path_to_csv_file):
    # Method Chain 1
    # Load Data
    # remove Player ID column
    # remove LS (long snappers) are typicaly never drafted as the team
    # there are 20 Long Snappers
    # remove 2018 data from dataset
    # there is no draft information
    # set all undrafted players pick 300
    # set all undrafted players round 10
    
    df1 = (
        pd.read_csv(url_or_path_to_csv_file)
        .drop(columns = ['Pfr_ID'])
        .query('Pos != "LS"')
        .query('Year != 2018')
        .assign(Pick=lambda x: x.Pick.fillna(300))
        .assign(Round=lambda x: x.Round.fillna(10))
    )
    
    # Method Chain 2
    # Replace position names
    # MLB (middle line backer) and ILB (inside line backer) are the same thing
    # LB (line backer) with ILB
    # EDGE is the same as DE (Defense End)
    # combine P (punter) and K (kicker) into a single position PK (Punter Kicker)
    # G (guard) with OG (offensive guard)
    # OL (offensive line) with OG (offensive guard)
    # FS(free safety) with S (satefy)
    # SS(strong safety) with S (satefy)
    # DB (defensive back) with CB (corner back)
    # NT (nose tackle with DT (defensive tackle)
    
    df1['Pos'] = (df1['Pos']
        .replace({'MLB': 'ILB'})
        .replace('LB', 'ILB')
        .replace('EDGE', 'DE')
        .replace('P', 'PK')
        .replace('K', 'PK')
        .replace('G', 'OG')
        .replace('OL', 'OG')
        .replace('FS', 'S')
        .replace('SS', 'S')
        .replace('DB', 'CB')
        .replace('NT', 'DT')
    )
        
    return df1
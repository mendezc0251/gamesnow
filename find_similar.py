import pandas as pd
import random

def load_games():
    return pd.read_csv("data/steam.csv")

def find_similar_games(user_favorites, all_games):
    results=[]
    for fav in user_favorites:
        game_row = all_games[all_games['name'].str.contains(fav, case=False, na=False)]

        if not game_row.empty:
            fav_genres = str(game_row.iloc[0]['genres'])
            fav_tags=str(game_row.iloc[0]['steamspy_tags'])

            keywords = [g.strip().lower() for g in (fav_genres + "," + fav_tags).split(",") if g.strip()]

            matches = all_games[all_games['steamspy_tags'].apply(
                lambda x: any(k in str(x).lower() for k in keywords)
            )]

            if len(matches) > 0:
                sampled = matches.sample(min(5, len(matches)), random_state=random.randint(1,9999))
                results.extend(sampled.to_dict(orient='records'))
            
    results_df = pd.DataFrame(results).drop_duplicates(subset=["name"])
    results_df = results_df[~results_df['name'].isin(user_favorites)]

    return results_df.to_dict(orient='records')

games = load_games()

user_favorites = ["The Binding of Isaac", "Team Fortress 2", "Slay the Spire"]

recs = find_similar_games(user_favorites, games)

for game in recs[:5]:
    print(f"{game['name']} ({game['genres']}) - by {game['developer']}")
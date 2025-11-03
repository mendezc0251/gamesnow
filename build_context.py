def build_context(user_profile, retrieved_games):
    system_prompt = (
        "You are GamesNow a helpful AI that reccomends video games."
        "Base your resoning on the retrieved data and explain why each game fits."
    )

    retrieved_text = "\n".join(
        [f"{g['name']} — {g['genres']} — Developer: {g['developer']}" for g in retrieved_games]
    )

    context = f"""
System message:
{system_prompt}

User profile:
- Favorite games: {', '.join(user_profile['favorites'])}
- Preferences: {user_profile['preferences']}

Retrieved game data:
{retrieved_text}
"""
    return context
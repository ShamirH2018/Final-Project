"""
AI Music Mood Selector
-----------------------------------------
This program recommends a music genre based on:
1. User mood
2. Time of day
3. Current activity

The system uses a scoring-based approach:
- Each input adds points to certain genres
- The genre with the highest score is selected
"""

# Function to collect user input
def get_user_input():
    print("=== AI Music Mood Selector ===\n")

    # Ask the user for their current mood
    mood = input("Enter your mood (happy, sad, stressed, relaxed): ").lower()

    # Ask for the time of day
    time_of_day = input("Enter time of day (morning, afternoon, night): ").lower()

    # Ask for current activity
    activity = input("Enter activity (studying, workout, relaxing, driving): ").lower()

    # Return all inputs
    return mood, time_of_day, activity


# Function to initialize all genre scores to 0
def initialize_scores():
    # Dictionary to store scores for each music genre
    scores = {
        "Pop": 0,
        "EDM": 0,
        "Hip-Hop": 0,
        "Classical": 0,
        "Lo-fi": 0,
        "Rock": 0,
        "Jazz": 0
    }
    return scores


# Function to apply scoring based on mood
def apply_mood_scores(scores, mood):
    # Increase scores depending on mood
    if mood == "happy":
        scores["Pop"] += 3
        scores["EDM"] += 2

    elif mood == "sad":
        scores["Classical"] += 3
        scores["Lo-fi"] += 2

    elif mood == "stressed":
        scores["Lo-fi"] += 3
        scores["Jazz"] += 2

    elif mood == "relaxed":
        scores["Jazz"] += 3
        scores["Classical"] += 2

    else:
        # If input doesn't match expected values
        print("⚠ Unknown mood entered. No score applied.")


# Function to apply scoring based on time of day
def apply_time_scores(scores, time_of_day):
    if time_of_day == "morning":
        scores["Pop"] += 2
        scores["Jazz"] += 1

    elif time_of_day == "afternoon":
        scores["Rock"] += 2
        scores["Hip-Hop"] += 1

    elif time_of_day == "night":
        scores["Lo-fi"] += 2
        scores["Classical"] += 1

    else:
        print("⚠ Unknown time entered. No score applied.")


# Function to apply scoring based on activity
def apply_activity_scores(scores, activity):
    if activity == "studying":
        scores["Lo-fi"] += 3
        scores["Classical"] += 2

    elif activity == "workout":
        scores["EDM"] += 3
        scores["Hip-Hop"] += 2

    elif activity == "relaxing":
        scores["Jazz"] += 3
        scores["Classical"] += 2

    elif activity == "driving":
        scores["Rock"] += 3
        scores["Hip-Hop"] += 2

    else:
        print("⚠ Unknown activity entered. No score applied.")


# Function to determine the best genre based on highest score
def get_recommendation(scores):
    # max() finds the key (genre) with the highest value (score)
    best_genre = max(scores, key=scores.get)
    return best_genre


# Function to display the final recommendation
def display_result(genre):
    print("\n🎵 Recommended Music Genre:", genre)

    # Dictionary of suggestions for each genre
    suggestions = {
        "Pop": "Try artists like Taylor Swift or Dua Lipa",
        "EDM": "Try artists like Calvin Harris or Avicii",
        "Hip-Hop": "Try artists like Drake or Travis Scott",
        "Classical": "Try composers like Mozart or Beethoven",
        "Lo-fi": "Try Lo-fi beats playlists on YouTube or Spotify",
        "Rock": "Try bands like Imagine Dragons or Linkin Park",
        "Jazz": "Try artists like Miles Davis or John Coltrane"
    }

    # Print suggestion if available
    if genre in suggestions:
        print("👉", suggestions[genre])


# Main function to run the program
def main():
    # Step 1: Get user input
    mood, time_of_day, activity = get_user_input()

    # Step 2: Initialize scores
    scores = initialize_scores()

    # Step 3: Apply scoring rules
    apply_mood_scores(scores, mood)
    apply_time_scores(scores, time_of_day)
    apply_activity_scores(scores, activity)

    # Step 4: Determine best genre
    best_genre = get_recommendation(scores)

    # Step 5: Display result
    display_result(best_genre)

    # Optional: Print all scores (useful for debugging or report screenshots)
    print("\n--- Debug: Genre Scores ---")
    for genre, score in scores.items():
        print(f"{genre}: {score}")


# Run the program
if __name__ == "__main__":
    main()
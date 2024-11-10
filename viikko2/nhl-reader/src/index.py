from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    nat = "FIN"
    players = stats.top_scorers_by_nationality(nat)

    print(f"Players from {nat}\n")
    for player1 in players:
        print(player1)


if __name__ == "__main__":
    main()

import random


class Team:
    def __init__(self, name, strength):
        self.name = name
        self.base_strength = strength
        self.points = 0
        self.goals_scored = 0
        self.goals_conceded = 0

    def goal_diff(self):
        return self.goals_scored - self.goals_conceded


class Match:
    def __init__(self, home, away):
        self.home = home
        self.away = away

    def play(self, show=False):

        home_power = self.home.base_strength + 10
        away_power = self.away.base_strength - 10

        total = home_power + away_power
        home_chance = home_power / total
        away_chance = away_power / total

        home_goals = 0
        away_goals = 0

        for _ in range(5):
            r = random.random()
            if r < home_chance * 0.3:
                home_goals += 1
            elif r > 1 - (away_chance * 0.3):
                away_goals += 1

        self.home.goals_scored += home_goals
        self.home.goals_conceded += away_goals
        self.away.goals_scored += away_goals
        self.away.goals_conceded += home_goals

        if home_goals > away_goals:
            self.home.points += 3
        elif away_goals > home_goals:
            self.away.points += 3
        else:
            self.home.points += 1
            self.away.points += 1

        if show:
            print(f"\n⚽ {self.home.name} {home_goals} : {away_goals} {self.away.name}")

class League:
    def __init__(self, teams):
        self.teams = teams
        self.schedule = []
        self.current_round = 0
        self.generate_schedule()

    def generate_schedule(self):
        teams = self.teams[:]
        if len(teams) % 2:
            teams.append(None)

        n = len(teams)
        rounds = n - 1

        for r in range(rounds):
            round_matches = []
            for i in range(n // 2):
                t1 = teams[i]
                t2 = teams[n - 1 - i]
                if t1 and t2:
                    round_matches.append(Match(t1, t2))
            self.schedule.append(round_matches)

            teams.insert(1, teams.pop())

    def play_round(self, manager_team):
        if self.current_round >= len(self.schedule):
            print("Сезон завершено!")
            return False

        print(f"\n===== ТУР {self.current_round + 1} =====")

        for match in self.schedule[self.current_round]:
            if match.home == manager_team or match.away == manager_team:
                match.play(show=True)
            else:
                match.play()

        self.current_round += 1
        return True

    def show_table(self):
        table = sorted(self.teams, key=lambda x: (x.points, x.goal_diff()), reverse=True)

        print("\n=== ТУРНІРНА ТАБЛИЦЯ ===")
        for i, team in enumerate(table, 1):
            print(f"{i}. {team.name} | {team.points} pts | GD {team.goal_diff()}")

team_data = [
    ("Manchester City", 400),
    ("Arsenal", 380),
    ("Liverpool", 360),
    ("Chelsea", 340),
    ("Tottenham", 320),
    ("Manchester United", 300),
    ("West Ham", 280),
    ("Leicester", 260),
    ("Crystal Palace", 240),
    ("Newcastle", 220),
    ("Aston Villa", 200),
    ("Everton", 180),
    ("Wolves", 160),
    ("Southampton", 140),
    ("Burnley", 120),
    ("Norwich", 100),
    ("Bournemouth", 80),
    ("Brighton", 60),
    ("Brentford", 40),
    ("Sheffield Utd", 20),
]

teams = [Team(name, strength) for name, strength in team_data]

league = League(teams)

print("Обери команду:")
for i, team in enumerate(teams, 1):
    print(f"{i}. {team.name}")

choice = int(input("Введи номер команди: "))
manager_team = teams[choice - 1]

print(f"\nТи менеджер команди {manager_team.name} 🔥")


while True:
    command = input("\nНапиши 'далі' щоб зіграти тур або 'вихід': ")

    if command.lower() == "далі":
        if not league.play_round(manager_team):
            break
        league.show_table()
    elif command.lower() == "вихід":
        break
    else:
        print("Невірна команда!")
import random

class MarkovChain:
    def __init__(self):
        self.states = ["easy", "normal", "hard"]
        self.current_state = random.choice(self.states)
        self.transition_probs = {
            "easy": {"easy": 0.7, "normal": 0.2, "hard": 0.1},
            "normal": {"easy": 0.3, "normal": 0.6, "hard": 0.1},
            "hard": {"easy": 0.1, "normal": 0.2, "hard": 0.7}
        }

    def next_state(self):
        next_state_probs = self.transition_probs[self.current_state]
        rand = random.random()
        cumulative_prob = 0.0
        for state, prob in next_state_probs.items():
            cumulative_prob += prob
            if rand < cumulative_prob:
                self.current_state = state
                break

    def set_difficulty(self, difficulty):
        if difficulty in self.states:
            self.current_state = difficulty
        else:
            raise ValueError("Invalid difficulty level.")

    def get_difficulty(self):
        return self.current_state

def get_computer_choice(difficulty, player_choice_history):
    choices = ["Rock", "Paper", "Scissors"]
    if difficulty == "easy":
        return random.choice(choices)
    elif difficulty == "normal":
        return random.choice(choices)
    elif difficulty == "hard":
        if player_choice_history:
            last_player_choice = player_choice_history[-1]
            if last_player_choice == "Rock":
                return "Paper"
            elif last_player_choice == "Paper":
                return "Scissors"
            elif last_player_choice == "Scissors":
                return "Rock"
        return random.choice(choices)

def determine_winner(player, computer):
    if player == computer:
        return "Tie"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        return "Player"
    else:
        return "Computer"

def print_results(player, computer, result):
    if result == "Tie":
        print(f"It's a tie! Both chose {player}.")
    elif result == "Player":
        print(f"You win! {player} beats {computer}.")
    else:
        print(f"You lose! {computer} beats {player}.")

def print_score(player_wins, computer_wins, ties):
    print(f"Score - Player: {player_wins}, Computer: {computer_wins}, Ties: {ties}")

def play_game():
    player_wins = 0
    computer_wins = 0
    ties = 0
    player_choice_history = []

    markov_chain = MarkovChain()

    while True:
        difficulty = input("Choose difficulty level for the first game ('easy', 'normal', 'hard'): ").strip().lower()
        try:
            markov_chain.set_difficulty(difficulty)
            break
        except ValueError as e:
            print(e)
            continue

    while True:
        difficulty = markov_chain.get_difficulty()

        while True:
            player_input = input(f"Current difficulty: {difficulty}\n"
                                 "Enter 'R' for Rock, 'P' for Paper, 'S' for Scissors, 'D' to change difficulty, 'E' to exit: ").strip().upper()

            if player_input == "E":
                print("Exiting the game.")
                return
            elif player_input == "D":
                new_difficulty = input("Choose new difficulty level ('easy', 'normal', 'hard'): ").strip().lower()
                try:
                    markov_chain.set_difficulty(new_difficulty)
                    break
                except ValueError as e:
                    print(e)
                    continue

            if player_input not in ["R", "P", "S"]:
                print("That's not a valid play. Please try again.")
                continue

            choices = {"R": "Rock", "P": "Paper", "S": "Scissors"}
            player_choice = choices[player_input]

            if difficulty == "hard":
                player_choice_history.append(player_choice)

            computer_choice = get_computer_choice(difficulty, player_choice_history)
            print(f"Computer chooses: {computer_choice}")

            result = determine_winner(player_choice, computer_choice)
            print_results(player_choice, computer_choice, result)

            if result == "Player":
                player_wins += 1
            elif result == "Computer":
                computer_wins += 1
            else:
                ties += 1

            print_score(player_wins, computer_wins, ties)
            print()

            markov_chain.next_state()

play_game()

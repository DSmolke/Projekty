from typing import Final
import re


def word_of_choice(message: str) -> str:
    """
    Takes first player input
    :param message: Provide information that should user do
    :return: word that second player will try to match
    """
    while not re.match(r'^[A-Z]{2,}$', word := input(f'{message}:\n')):
        print(f'Incorrect input: {word}')
    return word


def init_template_of(word: str) -> list[str]:
    """
    Creates list that will be hub for second player characters bets
    :param word: First player word choice
    :return: list of underscores
    """
    return ["_" for _ in range(len(word))]


def get_user_bet(message: str) -> str:
    """
    Takes input that must be single capital letter
    :param message: Provide information that should user do
    :return: Second player char of choice
    """
    while not re.match(r'^[A-Z]$', char := input(f'{message}:\n')):
        print(f'Incorrect input: {char}')
    return char


def play_round(word: str, template: list[str], counter: list[int]) -> True or None:
    """

    :param word: Player one word choice
    :param template: Player two bets hub
    :param counter: amount of Player 2 chances left
    :return: True if counter equals 0 or templates elements equal words elements, None if game continue
    """
    def update_template(char: str) -> None:
        """
        Function does not return any value, only updates list objects of template, choice
        :param char: Player 2 word of choice
        :return: None
        """
        def check_user_bet() -> bool:
            return True if char in word else False

        if check_user_bet():
            if char not in template:
                for i in range(len(word)):
                    if char == word[i]:
                        template[i] = char
        else:
            counter[0] -= 1

    if counter[0] > 1 and '_' in template:
        print("".join(template))
        bet = get_user_bet("Input your bet")
        update_template(bet)
    else:
        return True


def main() -> None:
    GALLOWS_NUM: Final = 6
    counter = [GALLOWS_NUM]
    word = word_of_choice("Player 1, input your word of choice")
    template = init_template_of(word)
    while not play_round(word, template, counter):
        print(f"Player 2 has {counter[0]} chances left.")
    print(f"Player 1 {'lose' if '_' in template or counter == 0 else 'wins'}")


if __name__ == '__main__':
    main()

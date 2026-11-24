
"""Quote generator: prints a random inspirational quote each time it runs."""

import random

QUOTES = [
    ("The only way to do great work is to love what you do.", "Steve Jobs"),
    ("Well done is better than well said.", "Benjamin Franklin"),
    ("It does not matter how slowly you go as long as you do not stop.", "Confucius"),
    ("Do what you can, with what you have, where you are.", "Theodore Roosevelt"),
    ("The unexamined life is not worth living.", "Socrates"),
    ("I think, therefore I am.", "René Descartes"),
    ("Fall seven times, stand up eight.", "Japanese Proverb"),
    ("The journey of a thousand miles begins with a single step.", "Lao Tzu"),
    ("Act as if what you do makes a difference. It does.", "William James"),
    ("Imagination is more important than knowledge.", "Albert Einstein"),
    ("What we think, we become.", "Buddha"),
    ("That which does not kill us makes us stronger.", "Friedrich Nietzsche"),
]


def get_random_quote():
    """Return a random (quote, author) tuple."""
    return random.choice(QUOTES)


def format_quote(quote, author):
    """Format a quote for display."""
    return f'"{quote}" — {author}'


def main():
    quote, author = get_random_quote()
    print(format_quote(quote, author))


if __name__ == "__main__":
    main()

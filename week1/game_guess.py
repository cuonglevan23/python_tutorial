# game guess
# tạo một trò chơi đoán từ đơn giản

secret_word = "python"
hint = "A programming language"
guess = ""

# guess.lower() là để chuyển đổi chuỗi guess thành chữ thường, giúp so sánh không phân biệt chữ hoa chữ thường.
while guess.lower() != secret_word:
    guess = input(f"Guess the secret word (Hint: {hint}): ")
    if guess.lower() == secret_word:
        print("Congratulations! You've guessed the word!")
    else:
        print("Try again!")
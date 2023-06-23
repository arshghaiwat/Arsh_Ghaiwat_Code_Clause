import time

def calculate_typing_speed(text, elapsed_time):
    words = text.split()
    num_words = len(words)
    words_per_minute = num_words / elapsed_time * 60
    return words_per_minute

def run_typing_test():
    print("Welcome to the Speed Typing Test!")
    print("Type the following text as fast as you can:\n")

    text = "The quick brown fox jumps over the lazy dog."

    print(text + "\n")

    input("Press Enter when you are ready to start the timer.")

    start_time = time.time()

    user_input = input()

    end_time = time.time()

    elapsed_time = end_time - start_time

    words_per_minute = calculate_typing_speed(user_input, elapsed_time)

    print("\nTest Results:")
    print("Time elapsed: {:.2f} seconds".format(elapsed_time))
    print("Words per minute: {:.2f}".format(words_per_minute))

run_typing_test()
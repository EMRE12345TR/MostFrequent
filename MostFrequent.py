numbers = []
frequency = {}
while True:
    x = input("Enter an integer (q for quit): ")
    if (x == 'q'):
        break
    try:
        number = int(x)
        numbers.append(number)
    except ValueError:
        print(f"Error! {x} is not an integer!")

for n in numbers:
    if n in frequency:
        frequency[n] += 1
    else:
        frequency[n] = 1
if frequency:
    max_freq = max(frequency.values())
    most_frequent = [key for key, value in frequency.items() if value == max_freq]
    print(f"The most frequent element(s): {most_frequent} ({max_freq} times)")
else:
    print("No valid numbers entered")

string = input("Enter a word or sentence: ")
freq = {}
for ch in string:
    if (ch != ' '):
        new_ch = ch.lower()
        if new_ch in freq:
            freq[new_ch] += 1
        else:
            freq[new_ch] = 1
if freq:
    for a, count in freq.items():
        print(f"{a}: {'*' * count} ({count} times)")
else:
    print("No input text to analyze.")
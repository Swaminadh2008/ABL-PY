text = input().lower()
words = text.split()

repeated = []

for word in words:
    if words.count(word) > 1 and word not in repeated:
        repeated.append(word)

print(repeated)
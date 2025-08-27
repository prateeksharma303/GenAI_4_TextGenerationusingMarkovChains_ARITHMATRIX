import random
import os
text = "I love learning AI and machine learning. AI is the future. AI will change the world. Machine learning is fun and powerful."
words = text.split()
markov_chain = {}
for i in range(len(words) - 1):
    word = words[i]
    next_word = words[i + 1]
    markov_chain.setdefault(word, []).append(next_word)
    
def generate_text(start_word, length=10):
    word = start_word
    output = [word]
    for _ in range(length - 1):
        if word not in markov_chain:
            break
        word = random.choice(markov_chain[word])
        output.append(word)
    return " ".join(output)

os.makedirs("generated_samples", exist_ok=True)
start_words = ["AI", "Machine", "I", "learning", "future"]
for i in range(20):
    start = random.choice(start_words)
    text_out = generate_text(start, 10)
    with open(f"generated_samples/sample{i+1}.txt", "w") as f:
        f.write(text_out)
print("✅ 20 samples saved inside 'generated_samples/' folder")

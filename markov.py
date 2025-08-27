{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "403066ba-ce6e-41b4-a89e-ec62f40bcdb5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ 20 samples saved inside 'generated_samples/' folder\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "import os\n",
    "\n",
    "# Example text corpus\n",
    "text = \"I love learning AI and machine learning. AI is the future. AI will change the world. Machine learning is fun and powerful.\"\n",
    "words = text.split()\n",
    "\n",
    "# Build Markov chain dictionary\n",
    "markov_chain = {}\n",
    "for i in range(len(words) - 1):\n",
    "    word = words[i]\n",
    "    next_word = words[i + 1]\n",
    "    markov_chain.setdefault(word, []).append(next_word)\n",
    "\n",
    "# Text generator\n",
    "def generate_text(start_word, length=10):\n",
    "    word = start_word\n",
    "    output = [word]\n",
    "    for _ in range(length - 1):\n",
    "        if word not in markov_chain:\n",
    "            break\n",
    "        word = random.choice(markov_chain[word])\n",
    "        output.append(word)\n",
    "    return \" \".join(output)\n",
    "\n",
    "# Create folder for outputs\n",
    "os.makedirs(\"generated_samples\", exist_ok=True)\n",
    "\n",
    "# Generate and save 20 samples\n",
    "start_words = [\"AI\", \"Machine\", \"I\", \"learning\", \"future\"]\n",
    "for i in range(20):\n",
    "    start = random.choice(start_words)\n",
    "    text_out = generate_text(start, 10)\n",
    "    with open(f\"generated_samples/sample{i+1}.txt\", \"w\") as f:\n",
    "        f.write(text_out)\n",
    "\n",
    "print(\"✅ 20 samples saved inside 'generated_samples/' folder\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "16536365-da70-4a18-956d-2b543f757c6f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python (torch-env)",
   "language": "python",
   "name": "torch-env"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

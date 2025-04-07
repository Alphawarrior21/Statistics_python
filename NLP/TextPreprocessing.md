# Tokenization

### 🧩 **Imagine you're breaking a sentence into LEGO blocks.**

Each **block** is a **word** (or sometimes a piece of a word).  
That’s what **tokenization** does!


### 🧸 Example:

Let's take a sentence:  
👉 “I love ice cream.”

When we tokenize it, we break it into smaller parts:  
👉 `["I", "love", "ice", "cream"]`

Each word is a **token** — like a puzzle piece!

### 🧠 But sometimes...

Big or unusual words (like “unbelievable”) are **too big for one block**.

So we break it into **smaller pieces**:  
👉 “unbelievable” → `["un", "believ", "able"]`

This helps the computer **understand even tricky or new words**.

### 📦 Types of Tokenization (in grown-up terms):

| Type | Like... | Example |
|------|---------|---------|
| Word Tokenization | Splitting by words | “I love dogs” → `["I", "love", "dogs"]` |
| Subword Tokenization | Splitting big words into pieces | “unhappiness” → `["un", "happi", "ness"]` |
| Character Tokenization | Every letter is a token | “cat” → `["c", "a", "t"]` |


### 🏁 In short:

> **Tokenization = cutting sentences into small parts**  
> so the computer can **read and learn** like you do with picture books 📖✨

### 🎯 Why Tokenization is Important:

- Computers don’t understand big messy sentences.
- Tokenization **chops things up** into small, easy-to-understand parts.
- Then the model can **learn** or **answer** better.


### 🔧 **Tokenization (Technical Definition):**

> **Tokenization** is the process of converting a raw text sequence into a sequence of meaningful units called **tokens** — typically words, subwords, or characters — to serve as input for downstream natural language processing tasks.

---

### 🔍 **Key Characteristics:**

1. **Preprocessing Step:**
   - It is the **first and fundamental step** in NLP pipelines (before embedding, parsing, etc.).

2. **Tokens Can Be:**
   - **Words** (e.g., `["I", "like", "pizza"]`)
   - **Subwords** (e.g., `["un", "believ", "able"]`) → used in BPE/WordPiece
   - **Characters** (e.g., `["h", "e", "l", "l", "o"]`)

3. **Tokenization Strategies:**
   - **Whitespace or Rule-Based Tokenization:** Simple split based on spaces and punctuation (e.g., NLTK).
   - **Regex-based Tokenization:** Custom rules for splitting tokens (e.g., split on contractions, punctuation).
   - **Subword Tokenization:**
     - **Byte Pair Encoding (BPE)** – used in GPT, RoBERTa
     - **WordPiece** – used in BERT
     - Helps handle **out-of-vocabulary (OOV)** issues.
   - **Unigram Language Model Tokenization** – used in models like SentencePiece.

4. **Tools/Libraries:**
   - `nltk.word_tokenize()`
   - `spaCy` tokenization
   - `HuggingFace` tokenizers (`AutoTokenizer`)
   - `SentencePiece` for subword-level tokenization

---

### 🧠 **Why It Matters:**
- Tokenization determines the **granularity of input** to the model.
- It affects the **vocabulary size**, **training efficiency**, **handling of unknown words**, and even **model performance**.
- A poor tokenization strategy can lead to loss of semantic meaning or bloated sequences.

---

### 📦 Example (BERT Tokenizer):

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
tokens = tokenizer.tokenize("Unbelievably smooth NLP experience.")
print(tokens)
# Output: ['un', '##bel', '##ievably', 'smooth', 'nlp', 'experience', '.']
```


# Normalization

### ✨ Think of Normalization like cleaning up your toys and putting them in the same box.

- Sometimes, you have toys that **look different but are really the same** — like a red car, a big red car, and a small red car.
- To make things easier, you call **all of them just "car"**.
  
**That’s what normalization does with words.**  
It makes sure words that **mean the same** or are just **different versions** of the same thing all look the same.

---

### 🧸 Example:

- **"Running", "runs", "ran"** → all become **"run"**
- **"HELLO", "hello", "Hello!"** → all become **"hello"**

It helps the computer not get confused and **treat all these as one word.**


### 🧠 **Normalization in NLP** refers to the systematic transformation of text into a standard, canonical form to reduce noise, variability, and redundancy in language data before modeling or analysis.

---

### ✅ **Goals:**

- Reduce **inflectional** and **derivational** variations
- Improve **token matching**, search, classification, and model generalization
- Shrink vocabulary space to optimize model training and inference

---

### ⚙️ **Common Normalization Techniques:**

| Technique         | Description | Example |
|------------------|-------------|---------|
| **Lowercasing** | Converts text to lowercase to avoid case-sensitive mismatches | `"Apple"` → `"apple"` |
| **Sentiment Analysis** | Case is helpful(US versus us is important) -> Context is important here along with case folding.
| **Removing Punctuation** | Eliminates non-word characters | `"hello!"` → `"hello"` |
| **Stopword Removal** | Removes common low-information words | `"is", "the", "and"` |
| **Stemming** | Cuts words to their **root** form (sometimes not a real word) | `"running"` → `"run"` |
| **Lemmatization** | Converts words to their **base dictionary form** | `"better"` → `"good"` |
| **Accents Removal** | Removes diacritics from characters | `"café"` → `"cafe"` |
| **Unicode Normalization** | Standardizes different encodings of characters | `“é”` vs. `"é"` both → `"é"` |
|**Regular Experession**| Its a algebric notation to search a pattern.

### 📌 **Stemming vs Lemmatization (Key Difference):**

| Feature | Stemming | Lemmatization |
|---------|----------|----------------|
| Output | May not be a real word | Always a valid word |
| Aggressiveness | More aggressive | More accurate |
| Example | `"caring"` → `"car"` | `"caring"` → `"care"` |
| Library | `PorterStemmer` | `WordNetLemmatizer` |

---

### 🧪 Sample in Python:

```python
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

text = "Running faster than the wind isn't always better."

# Lowercase + tokenization
tokens = nltk.word_tokenize(text.lower())

# Remove stopwords
tokens = [t for t in tokens if t not in stopwords.words("english")]

# Lemmatization
lemmatizer = WordNetLemmatizer()
normalized = [lemmatizer.lemmatize(t) for t in tokens]

print(normalized)
# Output: ['running', 'faster', 'wind', "n't", 'always', 'better']
```

---

## 🧠 TL;DR:

> **Normalization** is like **cleaning and standardizing** your text so that models can learn better by focusing on the **meaning**, not messy surface-level differences.

# Levenshtein Edit Distance

Imagine you’re playing with words like building blocks.  
You want to turn the word **"cat"** into **"cut"**.

- You see that you just need to **change the "a" to "u"**.
- That’s **1 change**.

So, the **edit distance** between “cat” and “cut” is **1**!

---

## 💻 **As a Developer:**

### 📌 **Levenshtein Distance** (also called **Edit Distance**) is a measure of how many **single-character edits** are required to transform one string into another.

These edits can be:

1. **Insertion** (add a character)  
2. **Deletion** (remove a character)  
3. **Substitution** (replace one character with another)

---

### 🧠 **Formal Definition:**

> The Levenshtein distance between two strings is the **minimum number of edits** (insertions, deletions, or substitutions) required to transform one string into the other.

---

### 📊 Example:

| Word 1 | Word 2 | Distance | Why? |
|--------|--------|----------|------|
| "kitten" | "sitting" | 3 | k → s, e → i, add g |
| "flaw" | "lawn" | 2 | f deleted, n added |
| "intention" | "execution" | 5 | multiple substitutions and insertions |

---

### 🧮 Python Implementation:

Using `python-Levenshtein` library:

```python
import Levenshtein

distance = Levenshtein.distance("kitten", "sitting")
print(distance)  # Output: 3
```

Or with a basic custom implementation:

```python
def levenshtein_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0: dp[i][j] = j
            elif j == 0: dp[i][j] = i
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    
    return dp[m][n]

print(levenshtein_distance("kitten", "sitting"))  # Output: 3
```

---

### 🚀 **Applications in NLP:**

- **Spell-checkers**
- **Fuzzy string matching**
- **Plagiarism detection**
- **OCR correction**
- **Record linkage (e.g., matching names in databases)**

---

### 🧠 TL;DR:

> **Levenshtein Distance** = How many **edits (insert, delete, substitute)** it takes to turn one string into another.  
Lower distance = More similar.


# Zipf's Law
This is used to describe the relationships between word frequencies in document collections. 
y=cx(to the power of -1/2)
y -> is used to describe the number of times that the xth word appears.
Thus the most frequent word will occur approximately twice as often as the second mist freqent word,3 times as often as the third most frequent word, etc.

# Word Associations

e.g husband - wife -spouse 
In a given word network what is the central word that n/w revolves around
e.g apologies,sorry -

Imagine you hear the word **"dog"**. What’s the first word that comes to your mind?

Maybe:

- 🐾 **"bark"**
- 🐶 **"puppy"**
- 🦴 **"bone"**

That’s **word association** — your brain is connecting words based on what you know about them!

### 🔍 **What are Word Associations in NLP?**

> **Word associations** are the relationships between words based on their **co-occurrence**, **semantic similarity**, or **contextual relevance** in a corpus or real-world knowledge.

These associations help models **understand meaning**, **generate language**, or **infer connections** between ideas.

---

### 💡 Types of Word Associations:

| Type                     | Description                                       | Example                             |
|--------------------------|---------------------------------------------------|-------------------------------------|
| **Syntagmatic**          | Words that appear **together in sentences**       | “eat” → “food”, “lunch”, “apple”   |
| **Paradigmatic**         | Words that can **substitute** each other          | “happy” ↔ “joyful”, “glad”, “cheerful” |
| **Semantic**             | Based on **meaning or concepts**                  | “fire” → “heat”, “flame”, “smoke”  |
| **Pragmatic** (context)  | Based on **usage or domain**                      | “bank” → “money” (finance), “river” (geography) |

---

### 📊 How NLP Models Learn Associations:

1. **Co-occurrence Matrices**  
   - Count how often words appear **near each other**.
   - E.g., in a 5-word window, "apple" might often be next to "fruit" or "pie".

2. **Word Embeddings (e.g., Word2Vec, GloVe)**  
   - Capture **semantic similarity** in vector space.
   - Words with similar meaning are **close together**.
   - Example: `cosine_similarity("king", "queen")` > `cosine_similarity("king", "banana")`

3. **Transformers & Attention (e.g., BERT)**  
   - Use **contextual embeddings**: the same word (e.g., “bank”) has different representations in different contexts.



### 🧠 Use Cases:

- **Search Engines**: Suggest related queries
- **Chatbots**: Maintain coherent conversations
- **Autocorrect & Prediction**: “you’re” vs “your”
- **Text Classification**: Knowing "apple" is more likely a fruit in "nutrition" context, but a company in "tech"

---

### 🧪 Try It Out in Python (with spaCy):

```python
import spacy

nlp = spacy.load("en_core_web_md")
word1 = nlp("dog")
word2 = nlp("bark")
word3 = nlp("car")

print("dog ↔ bark:", word1.similarity(word2))  # closer
print("dog ↔ car:", word1.similarity(word3))   # less related
```

## ✅ TL;DR:

> **Word associations** show how words relate to each other — in meaning, usage, or position.  
They help NLP models think more like humans when it comes to language.

# Word Dendrograms

**hierarchical relationships between words**

Imagine you’re grouping animals:

- You start with **all animals**
- Then split into **mammals, birds, reptiles**
- Then mammals into **dogs, cats, elephants**, etc.

You make a **tree-like drawing** that shows how things are **related and grouped**.

That’s a **dendrogram** — a branching picture that shows which things are similar and how closely they’re related!


### 📌 **What is a Word Dendrogram?**

> A **word dendrogram** is a **tree diagram** used to visualize **hierarchical clustering** of words based on their **similarity or distance** in a vector space.

It shows **how similar words are** and how they **group together**, forming **clusters** at different levels.

### 📊 **How it works:**

1. **Get Word Embeddings**  
   - Convert words into numeric vectors using Word2Vec, GloVe, BERT, etc.

2. **Calculate Distances**  
   - Use cosine similarity or Euclidean distance to measure how similar word vectors are.

3. **Perform Hierarchical Clustering**  
   - Use `scipy.cluster.hierarchy` to cluster similar words.

4. **Plot Dendrogram**  
   - A tree where:
     - Leaves = words
     - Branches = similarity (closer words merge earlier)

### 🧪 Example in Python:

```python
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.manifold import TSNE
import numpy as np
import gensim.downloader as api

# Load pre-trained word embeddings
model = api.load("glove-wiki-gigaword-50")  # small for speed

# Define your words
words = ["king", "queen", "man", "woman", "apple", "banana", "fruit", "dog", "cat", "puppy"]

# Get vectors
vectors = [model[word] for word in words]

# Create linkage matrix
linked = linkage(vectors, method='ward')

# Plot dendrogram
plt.figure(figsize=(10, 5))
dendrogram(linked, labels=words, orientation='top', distance_sort='descending')
plt.title("Word Dendrogram")
plt.show()
```

### 🧠 Use Cases:

- Visualizing **semantic similarity**
- Understanding **clusters of meaning**
- Creating **thesauri or topic hierarchies**
- Building **concept trees** for education or NLP exploration

### 📌 TL;DR:

> A **word dendrogram** shows how words are **clustered by similarity**, like a family tree of meanings.  
It uses **word vectors + hierarchical clustering** to create a **visual map of language**.


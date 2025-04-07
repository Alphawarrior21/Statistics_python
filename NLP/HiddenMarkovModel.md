# Hidden Markov Model

Imagine you're playing a guessing game with your friend who’s hiding behind a curtain. Every minute, they make a **sound** — sometimes a **bark**, sometimes a **meow**, or a **tweet**. You can’t see them, but based on the sound, you **guess** whether they’re pretending to be a **dog**, **cat**, or **bird**.

- What you **hear**: sounds like "bark", "meow", etc. → These are **observations**.
- What they’re **actually pretending to be** behind the curtain → These are **hidden states**.
- They might switch from cat → dog → bird in some order.

You're trying to **predict** what they’re pretending to be (the hidden state) based on the **sequence of sounds (observations)** you hear.

That’s the idea of a **Hidden Markov Model**!

---

## 💻 **HMM: Technical Definition**

A **Hidden Markov Model (HMM)** is a **probabilistic model** used to model **sequences** where:

- You observe a sequence of events (observations),
- But the actual system that generated those observations (the hidden states) is **not directly visible**.

---

### 📌 HMM Consists of:

1. **States**:  
   Hidden variables (e.g., `Rainy`, `Sunny`) → these aren’t observed directly.

2. **Observations**:  
   What you see (e.g., `Walk`, `Shop`, `Clean`).

3. **Transition Probabilities**:  
   Probability of moving from one state to another (e.g., `P(Rainy → Sunny)`).

4. **Emission Probabilities**:  
   Probability of an observation given a state (e.g., `P(Walk | Sunny)`).

5. **Initial State Probabilities**:  
   Probability of starting in a particular state (e.g., `P(Sunny)`).

---

### 🤖 What HMM Solves:

1. **Prediction (Evaluation)**:  
   What’s the probability that a given sequence of observations occurred?  
   🛠️ Algorithm: **Forward Algorithm**

2. **Decoding**:  
   What’s the most likely sequence of hidden states that led to these observations?  
   🛠️ Algorithm: **Viterbi Algorithm**

3. **Learning**:  
   Learn model parameters (transition/emission probs) from data.  
   🛠️ Algorithm: **Baum-Welch Algorithm (an Expectation-Maximization variant)**

---

### 📊 Simple Example:

#### States:  
☀️ Sunny  
🌧️ Rainy  

#### Observations:  
🧍 Walk, 🛒 Shop, 🧹 Clean  

#### Emissions:
| State  | Walk | Shop | Clean |
|--------|------|------|-------|
| Sunny  | 0.6  | 0.3  | 0.1   |
| Rainy  | 0.1  | 0.4  | 0.5   |

#### Transitions:
| From \ To | Sunny | Rainy |
|-----------|--------|--------|
| Sunny     | 0.7    | 0.3    |
| Rainy     | 0.4    | 0.6    |

---

### ✨ Where is HMM Used?

- **Speech Recognition**
- **Part-of-Speech Tagging** in NLP
- **Bioinformatics** (e.g., gene prediction)
- **Activity Recognition**
- **Weather Forecasting**

---

## ✅ TL;DR:

> **HMM** is a statistical model where the system is assumed to be a **Markov process** with **hidden states**. You see the **effects** (observations), but try to figure out the **hidden causes** (states) behind them.


# Detail explanation of HMM




# erdos-straus-algorithm
An algorithm to explore the Erdős–Straus conjecture using integer partitioning in Python.
# Erdős–Straus Conjecture Algorithm This project explores the **Erdős–Straus Conjecture**, which states that for any integer `n ≥ 2`, the fraction `4/n` can be expressed as the sum of three positive unit fractions:
4/n = 1/x + 1/y + 1/z


## 🧠 Algorithm Overview This algorithm searches for valid `(x, y, z)` triples by: - Scaling both sides of the equation to avoid fractions. - Splitting the numerator into three additive parts. - Converting each part into the denominator of a unit fraction. - Verifying the sum using Python's `fractions.Fraction` module for precision. ## 💡 Example Output
n=3, x=1/3, y=1/2, z=1/2
n=4, x=1/3, y=1/2, z=1/6
...


## 📂 Files - `erdos-straus-algorithm.py` – main algorithm code - `README.md` – this description ## 🛠 Requirements - Python 3.x No external libraries are needed. ## 👤 Author This code was developed by [your name here], based on an original exploration of integer-based solutions to the Erdős–Straus conjecture.

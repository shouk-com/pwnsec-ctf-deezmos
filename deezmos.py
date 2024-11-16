import numpy as np
from secret import FLAG, letters_to_func

samples = {}

for i, letter in enumerate(FLAG):
    curr = f"l{i}"
    for f in letters_to_func[letter]:
        shifted_func = lambda x: f(x - 10 * i)
        x = np.linspace(-100, 100, 5)
        y = shifted_func(x)
        points = list(zip(x, y))
        if curr in samples:
            samples[curr].append(points)
        else:
            samples[curr] = [points]

print(f"Samples = {samples}")
        
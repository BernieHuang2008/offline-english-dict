data_type = "csv"
data_path = "../assets/1e5_EnWords.csv"

def alloc_one_word():
    with open(data_path, "r", encoding='utf-8') as f:
        f.readline()  # skip header

        i = 0
        while True:
            start_pos = f.tell()

            line = f.readline()
            if not line:
                break

            # parse line
            word, trans = line.strip().strip('"').split(",", 1)

            # yield
            yield i, start_pos, word.upper(), trans

            i += 1


counter = {c: 0 for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}

for _, _, word, _ in alloc_one_word():
    first_letter = word[0].upper()
    counter[first_letter] += 1

print(counter)

# [../assets/1e5_EnWords.csv]
# {'A': 7454, 'B': 5205, 'C': 9789, 'D': 5675, 'E': 4520, 'F': 4008, 'G': 3435, 'H': 4481, 'I': 4215, 'J': 1005, 'K': 1460, 'L': 3620, 'M': 5807, 'N': 2712, 'O': 2509, 'P': 8386, 'Q': 588, 'R': 4946, 'S': 10669, 'T': 5486, 'U': 3057, 'V': 1804, 'W': 1989, 'X': 219, 'Y': 420, 'Z': 517}

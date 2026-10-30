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
            word, trans = line.strip().split(",", 1)

            # yield
            yield i, start_pos, word.upper().strip(' "'), trans.strip(' "')

            i += 1


counter = {a+b+c: 0 for a in "ABCDEFGHIJKLMNOPQRSTUVWXYZ@" for b in "ABCDEFGHIJKLMNOPQRSTUVWXYZ@" for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ@"}
for _, _, word, _ in alloc_one_word():
    if len(word) < 5:
        word += "@" * 4
    curr_indexer = word[0] + word[2] + word[4]
    if curr_indexer in counter:
        counter[curr_indexer] += 1

# print(counter["AAA"])

counter2 = {
    "0-word": 0,
    "1-word": 0,
    "10-words": 0,
    "max-words": -1,
}
for k in counter:
    if counter[k] == 0:
        counter2["0-word"] += 1
    elif counter[k] == 1:
        counter2["1-word"] += 1
    elif counter[k] <= 10:
        counter2["10-words"] += 1
    elif counter[k] > counter2["max-words"]:
        counter2["max-words"] = counter[k]

print(f"Total indexers: {len(counter)}")
print(f"Total indexers with no words: {counter2['0-word']} ({counter2['0-word']/len(counter)*100:.2f}%)")
print(f"Total indexers with less than 1 word: {counter2['1-word']} ({counter2['1-word']/len(counter)*100:.2f}%)")
print(f"Total indexers with less than 10 words: {counter2['10-words']} ({counter2['10-words']/len(counter)*100:.2f}%)")
print(f"Max words in one indexer: {counter2['max-words']}")

# [../assets/1e5_EnWords.csv]
# {'A': 7454, 'B': 5205, 'C': 9789, 'D': 5675, 'E': 4520, 'F': 4008, 'G': 3435, 'H': 4481, 'I': 4215, 'J': 1005, 'K': 1460, 'L': 3620, 'M': 5807, 'N': 2712, 'O': 2509, 'P': 8386, 'Q': 588, 'R': 4946, 'S': 10669, 'T': 5486, 'U': 3057, 'V': 1804, 'W': 1989, 'X': 219, 'Y': 420, 'Z': 517}

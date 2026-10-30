data_type = "csv"
data_path = "assets/1e5_EnWords.csv"

def alloc_one_word():
    with open(data_path, "r") as f:
        f.readline()  # skip header

        i = 0
        while True:
            start_pos = f.tell()

            line = f.readline()
            if not line:
                break

            # parse line
            word, trans = line.strip().strip('"').split(",")

            # yield
            yield i, start_pos, word.upper(), trans

            i += 1


def gen_index():
    index = []
    last_indexer = "@@@"
    for i, pos, word, _ in alloc_one_word():
        if len(word) < 5:
            word += "@" * 4
        curr_indexer = word[0] + word[2] + word[4]

        if curr_indexer != last_indexer:
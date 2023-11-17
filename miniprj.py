def create_substring_combinations(substrings, overlap=2):
    combined_strings = []

   
    def add_combinations(current, index):
        if index == len(substrings):
            combined_strings.append(current)
            return

        for i in range(overlap, len(substrings[index]) + 1):
            add_combinations(current + substrings[index][:i], index + 1)

    
    add_combinations("", 0)
    return combined_strings

example_fragments = ["SNU ", "U CH", "CHEN", "ENNA", "NAI."]
all_combinations = create_substring_combinations(example_fragments)
for combo in all_combinations:
    print(combo)

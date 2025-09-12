class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # words = s.split()

        # # Step 1: Check if lengths match
        # if len(pattern) != len(words):
        #     return False

        # char_to_word = {}
        # word_to_char = {}

        # # Step 2: Use a simple loop with index
        # for i in range(len(pattern)):
        #     ch = pattern[i]
        #     word = words[i]

        #     # Check existing mapping for character → word
        #     if ch in char_to_word:
        #         if char_to_word[ch] != word:
        #             return False
        #     else:
        #         # Check if word is already assigned to another character
        #         if word in word_to_char:
        #             return False
        #         # Add the new mapping
        #         char_to_word[ch] = word
        #         word_to_char[word] = ch

        # return True


        words = s.split()

        # Step 1: Check if lengths match
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        # Step 2: Use a simple loop with index
        for i in range(len(pattern)):
            ch = pattern[i]
            word = words[i]

            # Check existing mapping for character → word
            if (ch in char_to_word and char_to_word[ch] != word) or word in word_to_char and word_to_char[word] != ch:
                    return False
        
                # Add the new mapping
            char_to_word[ch] = word
            word_to_char[word] = ch

        return True


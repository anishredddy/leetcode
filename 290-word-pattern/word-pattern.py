class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        char_to_word= {}
        word_to_char = {}
        words = s.split()
        
        if len(words) != len(pattern):
            return False
        for i in range(len(pattern)):
            current_char = pattern[i]
            word= words[i]

            if current_char not in char_to_word and word not in word_to_char:
                char_to_word[current_char] = word
                word_to_char[word] = current_char
            else:
                if char_to_word.get(current_char) != word or word_to_char.get(word) != current_char:
                    return False  
        
        return True
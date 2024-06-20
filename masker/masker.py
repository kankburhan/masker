class Masker:

    def __init__(self, mask_char='*'):
        self.mask_char = mask_char

    def start(self, word, keep_char=0):
        """
        Returns the word with the specified number of characters masked from the start
        
        :param word: The input word to be masked
        :param keep_char: Number of characters to keep unmasked from the start
        :return: The masked word
        """
        if keep_char >= len(word):
            return word

        masked_part = self.mask_char * (len(word) - keep_char)
        return masked_part + word[-keep_char:]
    
    def end(self, word, keep_char=0):
        """
        Returns the word with the specified number of characters masked from the end
        
        :param word: The input word to be masked
        :param keep_char: Number of characters to keep unmasked from the end
        :return: The masked word
        """
        if keep_char >= len(word):
            return word
        masked_part = self.mask_char * (len(word) - keep_char)
        return word[:keep_char] + masked_part
    
    def mid(self, word, start_keep_char=0, end_keep_char=0):
        """
        Returns the word with the specified number of characters masked from the start and end
        
        :param word: The input word to be masked
        :param start_keep_char: Number of characters to keep unmasked from the start
        :param end_keep_char: Number of characters to keep unmasked from the end
        :return: The masked word
        """
        if start_keep_char + end_keep_char >= len(word):
            return word
        masked_part = self.mask_char * (len(word) - start_keep_char - end_keep_char)
        return word[:start_keep_char] + masked_part + word[-end_keep_char:]
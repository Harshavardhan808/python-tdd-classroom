class StringExercise:

    def __init__(self):
        pass   # Do some initial setup in this constructor method, if needed

    def reverse_string(self, input_str):
        """
        Reverses order of characters in string input_str.
        """
        return input_str[::-1]

    def is_english_vowel(self, character):
        """
        Returns True if character is an english vowel
        and False otherwise.
        """
        if(character.lower()=="a" or character.lower()=="e" or character.lower()=="i" or
                character.lower()=="o" or character.lower()=="u"):
            return True
        return False

    def find_longest_word(self, sentence):
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """
        sentence = sentence.split(" ")
        m = 0
        for word in sentence:
            m = max(m,len(word))
        for word in sentence:
            if(m == len(word)):
                return(word)


    def get_word_lengths(self, text):
        """
        Returns a list of integers representing
        the word lengths in string text.
        """
        text = text.split(" ")
        m = 0
        list = []
        for word in text:
            list.append(len(word))
        return(list)
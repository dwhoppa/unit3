# quiz 45

## UML diagram
![image](https://github.com/user-attachments/assets/8de85d90-596e-43af-9f64-502842529ec0)

## code
            class WordCounter:
                def __init__(self, text):
                    self.text = text
                    self.word_counts = {}
            
                def count_words(self):
                    words = self.text.lower().split()
                    for word in words:
                        word = word.strip(".")
                        self.word_counts[word] = self.word_counts.get(word, 0) + 1
            
                def display_counts(self):
                    for word, count in sorted(self.word_counts.items()):
                        print(f"{word} : {count}")
            
            
            text = "This is a sample text. It contains some words that will be counted."
            
            counter = WordCounter(text)
            counter.count_words()
            counter.display_counts()

## proof of work
![image](https://github.com/user-attachments/assets/ff0eaf7a-526c-409f-9034-fe733694d964)

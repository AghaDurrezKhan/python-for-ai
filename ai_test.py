import google.generativeai as genai
import pandas as pd

class Flashcard:
    def __init__(self, topic, content):
        self.topic = topic
        self.content = content

    def __str__(self):
        return f"Topic: {self.topic} | Content: {self.content}"

class Deck:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def get_topics(self):
        for card in self.cards:
            print(card.topic)

    def __str__(self):
        return f"Deck: {self.name} | Cards: {len(self.cards)}"

card1 = Flashcard("Python", "A high level programming language")
card2 = Flashcard("C++", "A middle level programming language")
card3 = Flashcard("Assembly", "A low level programming language")

deck1 = Deck("Programming Languages")

deck1.add_card(card1)
deck1.add_card(card2)
deck1.add_card(card3)

deck1.remove_card(card3)
deck1.get_topics()
deck1.add_card(card3)

print(deck1.__str__())

df = pd.DataFrame(vars(d) for d in deck1.cards)

genai.configure(api_key="API Key")
model = genai.GenerativeModel("gemini-3-flash-preview")

def generate_question(flashcard):
    prompt = f"Generate a quiz question for this flashcard: Topic: {flashcard.__str__()}. Return only the question, nothing else."
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e: 
        print(f"API Error: {e}")

for c in deck1.cards:
    print(generate_question(c))
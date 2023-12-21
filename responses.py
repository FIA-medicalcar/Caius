import random
import re
from typing import List
import requests
from apis import get_random_cat_image, get_random_chuck_norris_joke, get_random_advice


def handle_response(message: str) -> str:
    p_message = message.lower()

    greetings = [
        "Hail and well met, honorable human. May I offer my respectful salutations and extend a gracious welcome unto you.",
        "Greetings! I hope your day is as delightful as a summer breeze.",
        "Hello there! How can I assist you today?",
        "Ah, hello! It's a pleasure to make your acquaintance.",
        "Hey, hey, hey! What's up?",
        "Hello, friend! I'm here to help. What can I do for you?"
    ]

    bored_responses = [
        "I understand the feeling of boredom. How about trying a new hobby, like painting or playing a musical instrument?",
        "Boredom can be a great opportunity for creativity! You could try writing a short story or composing a song.",
        "Why not explore the world of books? Reading can transport you to fascinating places and ignite your imagination.",
        "Have you ever considered learning a new language? It can be a fun and rewarding way to spend your time.",
        "How about going for a walk in nature? Fresh air and a change of scenery can do wonders for your mood.",
        "You could try solving puzzles or brain teasers to challenge your mind and keep boredom at bay."
    ]

    cute_responses = [
        "Akitti? That's such a cute name! Sending virtual hugs to Akitti!",
        "Hello, Akitti! I hope you're having a paw-some day!",
        "Aww, Akitti! You bring joy to every conversation!",
        "Sending you lots of love and cuddles, Akitti!",
        "Hello, Akitti! Your adorable presence makes every moment brighter.",
        "Akitti, you bring a paw-sitive vibe wherever you go. Keep being pawsome!",
        "Akitti, you're the definition of adorable. Keep spreading joy!",
        "Akitti, you're as adorable as a fluffy cloud on a sunny day!"
    ]
    fact = [
        "A single rainforest can produce 20% of the Earth's oxygen.",
        "Cleopatra lived closer in time to the first Moon landing than to the construction of the Great Pyramid.",
        "The world's largest desert, Antarctica, is technically a cold desert.",
        "Wombat poop is cube-shaped to prevent it from rolling away on slopes.",
        "A 'jiffy' is an actual unit of time, equivalent to 1/100th of a second.",
        "The Great Wall of China is not visible from the moon without aid, contrary to popular belief.",
        "Octopuses have three hearts - two pump blood to the gills, and one pumps it to the rest of the body.",
        "A group of flamingos is called a 'flamboyance.'",
        "Identical twins don’t have the same fingerprints.",
        "The Universe's average colour is called 'Cosmic latte'.",
        "The world’s oldest cat 'Cream Puff lived to 38 years and three days old.",
        "Insects can fly up to 3.25km above sea level, at least.",
        "Dogs tilt their heads when you speak to them to better pinpoint familiar words. ",
        "Comets smell like rotten eggs. ",
        "The shortest war in history was between Britain and Zanzibar in 1896, lasting only 38 minutes."
    ]

    joke = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "I told my wife she should embrace her mistakes. She gave me a hug.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I only know 25 letters of the alphabet. I don't know y.",
        "Why did the computer go to therapy? It had too many bytes of emotional baggage.",
        "What do you call fake spaghetti? An impasta.",
        "Why did the scarecrow become a successful politician? Because he was outstanding in his field!",
        "I told my wife she should embrace her mistakes. She gave me a hug.",
        "Why did the math book look sad? Because it had too many problems.",
        "What's orange and sounds like a parrot? A carrot.",
        "Why don't skeletons fight each other? They don't have the guts.",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "Parallel lines have so much in common. It's a shame they'll never meet.",
        "What do you call a fish wearing a bowtie? SoFISHticated."

    ]

    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "The only way to achieve the impossible is to believe it is possible. - Charles Kingsleigh",
        "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
        "It always seems impossible until it's done.  - Nelson Mandela",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "In three words I can sum up everything I've learned about life: It goes on. - Robert Frost",
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "Strive not to be a success, but rather to be of value. - Albert Einstein",
        "The best way to predict the future is to create it. - Peter Drucker",
        "Do not wait to strike till the iron is hot, but make it hot by striking. - William Butler Yeats",
        "Success is stumbling from failure to failure with no loss of enthusiasm. - Winston S. Churchill",
        "In the middle of difficulty lies opportunity. - Albert Einstein",
        "Your attitude, not your aptitude, will determine your altitude. - Zig Ziglar",
        "The only person you are destined to become is the person you decide to be. -  Ralph Waldo Emerson",
        "Don't count the days, make the days count. -  Muhammad Ali",
        "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. - Christian D. Larson",
        "What lies behind us and what lies before us are tiny matters compared to what lies within us. - Ralph Waldo Emerson",
        "Opportunities don't happen. You create them. - Chris Grosser",
        "It's not whether you get knocked down, it's whether you get up. -  Vince Lombardi",
        "The only way to do great work is to love what you do.- Steve Jobs",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. -  Winston Churchill",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
        "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"
    ]

    if any(keyword.lower() in p_message for keyword in ['hello', 'hi', 'hey', 'heya']) and ('caius' in p_message):
        return random.choice(greetings)

    if any(phrase in p_message for phrase in ["caius i'm bored", "caius im bored", "caius i'm bored", "caius i am bored"]):
        return random.choice(bored_responses)

    if re.search(r'\bakitti\b', p_message, re.IGNORECASE):
        return random.choice(cute_responses)

    if p_message == '!norris':
        return get_random_chuck_norris_joke()

    if p_message == '!advice':
        return get_random_advice()

    if re.search(r'\bcaius cat\b', p_message, re.IGNORECASE):  # Check if the user mentioned 'caius cat'
        # Call the function to get a random cat image URL
        cat_image_url = get_random_cat_image('live_mgiNICPZqrZFcDNDNIFqMgKtlPChA5i5HyIdvJrac3k04QAASsJyxvDkzJDm5Q1G')
        return cat_image_url or "Failed to fetch a cat image."

    if p_message == 'saul':
        return "It's Saulin time."

    if 'roll' in p_message:
        return str(random.randint(1, 6))

    if p_message == '!help':
        return (
            "Welcome! Here are some commands you can use:\n"
            "- Type `!fact` to discover amazing facts.\n"
            "- Type `!quote` for a dose of interesting quotes.\n"
            "- Type `!joke` if you're in the mood for funny jokes.\n"
            "- To brighten your day with cuteness, type `caius cat` for pictures and gifs of adorable cats.\n"
            "- Need some advice? Type `!advice` to get a piece of valuable advice.\n"
            "- Want a Chuck Norris joke? Type `!norris` for a dose of Chuck Norris humor!"
        )

    if p_message == '!quote':
        return random.choice(quotes)

    if p_message == '!joke':
        return random.choice(joke)

    if p_message == '!fact':
        return random.choice(fact)

    return 'Regrettably, I am unable to grasp the meaning of your statement. Try typing "!help".'


# Example usage
user_message = input("Enter a message: ")
response = handle_response(user_message)
print(response)
# Example usage
user_message = input






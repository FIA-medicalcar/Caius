import random
import re
from typing import List
import requests
from apis import get_random_cat_image, get_random_chuck_norris_joke, get_random_advice, get_random_fox_image, get_nasa_apod, get_cat_fact, get_dad_joke
from dotenv import load_dotenv
import os
load_dotenv()

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
        "Discover the magic of music creation. Pick up an instrument, experiment with melodies, and compose a song that reflects your mood.",
        "Capture moments through photography and play with perspectives.",
        "Experiment with cooking or baking for culinary delight.",
        "Write a short story or explore poetry to unleash your creativity.",
        "Engage in mindful meditation for relaxation and mental clarity.",
        "Practice a new language with language-learning apps.",
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

    if p_message == 'c!bored':
        return random.choice(bored_responses)

    if re.search(r'caius.*akitti', p_message, re.IGNORECASE):
        return random.choice(cute_responses)

    if p_message == 'c!norris':
        return get_random_chuck_norris_joke()

    if p_message == 'c!dadjoke':
        return get_dad_joke()

    if p_message == 'c!fox':
        fox_image_url = get_random_fox_image()
        return fox_image_url or "Failed to fetch a fox image."

    if p_message == 'c!advice':
        return get_random_advice()

    if re.search(r'\bcaius cat\b', p_message, re.IGNORECASE) or re.search(r'\bc!caius cat\b', p_message, re.IGNORECASE):
        cat_image_url = get_random_cat_image(os.getenv('CAT_API_KEY'))
        return cat_image_url or "Failed to fetch a cat image."

    if p_message == "c!saul":
        return "It's Saulin time."

    if 'c!roll' in p_message:
        return str(random.randint(1, 6))

    if p_message == 'c!help':
        return (
            "Welcome to Discord Wonderland! Embark on a journey of discovery with these commands:\n"
            "- Type `c!fact` and unlock mind-blowing facts that will transport you to new realms.\n"
            "- Summon inspiration by typing `c!quote` for a collection of profound and thought-provoking quotes.\n"
            "- Elevate your mood! Type `c!joke` for a burst of laughter and `c!dadjoke` for some wholesome dad humor.\n"
            "- Seek wisdom with `c!advice` and receive valuable insights to navigate life's challenges.\n"
            "- Brace yourself for Chuck Norris' legendary humor! Type `c!norris` for a Chuck Norris joke.\n"
            "- Curious about foxes? Type `c!fox` to conjure a virtual fox and witness its playful antics.\n"
            "- Yearning for feline charm? Type `c!caius cat` for adorable cat pictures. Don't forget to spice it up "
            "with a cat fact by typing `c!catfact`.\n"
            "- Feeling bored? Type `c!bored` for quick ideas to banish boredom.\n"
            "- Reach for the stars! Type `c!nasa` and behold the Astronomy Picture of the Day from NASA."
        )

    if p_message == 'c!nasa':
        nasa_apod_info = get_nasa_apod(os.getenv('NASA_API_KEY'))
        if nasa_apod_info:
            return f"{nasa_apod_info['title']} \n\n{nasa_apod_info['explanation']}\n\n {nasa_apod_info['image_url']}"
        else:
            return "Failed to fetch NASA APOD."

    if p_message == 'c!catfact':
        cat_fact = get_cat_fact()
        return f"Cat Fact: {cat_fact}"

    if p_message == 'c!quote':
        return random.choice(quotes)

    if p_message == 'c!joke':
        return random.choice(joke)

    if p_message == 'c!fact':
        return random.choice(fact)

    return 'Regrettably, I am unable to grasp the meaning of your statement. Try typing "c!help".'


user_message = input("Enter a message: ")
response = handle_response(user_message)
print(response)
user_message = input

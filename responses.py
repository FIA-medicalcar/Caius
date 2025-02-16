import os
import random
import re
from typing import List

import puzzles
import requests

#TODO: Add reply system to Caius puzzles so it tells you if you get the puzzle right.

from apis import (get_cat_fact, get_dad_joke, get_formula1_driver_standings,
                  get_formula1_race_results, get_nasa_apod, get_random_advice,
                  get_random_cat_image, get_random_chuck_norris_joke,
                  get_random_fox_image)
from dotenv import load_dotenv

load_dotenv()

global safety_car_counter
safety_car_counter = 0

def handle_safety_car():
    global safety_car_counter

    if safety_car_counter % 2 == 0:
        safety_car_counter += 1
        return "Safety Car deployed."
    else:
        safety_car_counter += 1
        return "Safety Car in this lap."

def ask_for_track(year):
    return f"Sure! For which track would you like to see the results for Formula 1 {year}? Please input the name of the track."

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
        "I understand the feeling of boredom. How about trying a new hobby, like painting or playing a musical instrument?"
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

    if re.search(r'caius.*akitti', p_message, re.IGNORECASE) or p_message == 'c!akitti':
        return random.choice(cute_responses)

    if p_message == 'c!norris':
        return get_random_chuck_norris_joke()

    if p_message == 'c!dadjoke' or p_message == 'c!dj':
        return get_dad_joke()

    if p_message == 'c!fox':
        fox_image_url = get_random_fox_image()
        return fox_image_url or "Failed to fetch a fox image."

    if p_message == 'c!advice':
        return get_random_advice()

    if p_message == 'c!cat':
        cat_image_url = get_random_cat_image(os.getenv('CAT_API_KEY'))
        return cat_image_url or "Failed to fetch a cat image."

    if p_message == "c!saul":
        return "It's Saulin time."

    if p_message == "c!gacha":
        return "Give Tony the ol' Jedi mind trick and see if he can work his mastery on this one!"

    if p_message == 'c!taxes':
        image_url = "https://i.imgflip.com/8bi2qw.jpg"
        return f"Viz is no stranger to the art of tax shenanigans.\n{image_url}"
        #await message.channel.send(content=None, file=discord.File(image_url))

    if p_message == 'c!sleep':
        image_url = "https://pbs.twimg.com/media/GFaMnffW4AAReR8?format=jpg&name=medium"
        return image_url
        #await message.channel.send(file=discord.File(image_url))

    if p_message == "c!monad":
        return "A monad in X is just a monoid in the category of endofunctors of X, with product × replaced by composition of endofunctors and unit set by the identity endofunctor."

    if p_message.startswith("c!puzzle"):
        if "hard" in p_message:
            return puzzles.create_puzzle("hard")
        elif "easy" in p_message:
            return puzzles.create_puzzle("easy")
        elif "normal" in p_message or p_message == "c!puzzle":
            return puzzles.create_puzzle("normal")
        elif p_message.startswith("c!puzzle "):
            return "Usage: c!puzzle [easy|normal|hard]"

    if 'c!roll' in p_message:
        return str(random.randint(1, 6))

    if p_message == 'c!help':
        return (
            "Welcome to Caius! Check out these cool commands:\n"
            "- In need of some cuteness? Type `c!cat` for adorable cat pics, and add `c!catfact` for a fun cat fact.\n"
            "- Feeling curious? Type `c!fox` to bring a cute virtual fox to life.\n"
            "- Type `c!advice` for some helpful tips to tackle life’s challenges.\n"
            "- Love space? Type `c!nasa` to see the Astronomy Picture of the Day from NASA.\n"
            "- Want a laugh? Type `c!norris` for some classic Chuck Norris humor."
           
        )

    if p_message == 'c!nasa':
        nasa_apod_info = get_nasa_apod(os.getenv('NASA_API_KEY'))
        if nasa_apod_info:
            return f"{nasa_apod_info['title']} \n\n{nasa_apod_info['explanation']}\n\n {nasa_apod_info['image_url']}"
        else:
            return "Failed to fetch NASA APOD."

    if p_message == 'c!catfact'or p_message == 'c!cf':
        cat_fact = get_cat_fact()
        return f"Cat Fact: {cat_fact}"

    if p_message == 'c!quote' or p_message == 'c!q':
        return random.choice(quotes)

    if p_message == 'c!fact':
        return random.choice(fact)

    if p_message == 'c!sc':
        return handle_safety_car()

    if re.search(r'c!formula[ ]?1 (\d{4})', p_message):
        year_match = re.search(r'c!formula[ ]?1 (\d{4})', p_message)
        if year_match:
            year = int(year_match.group(1))
            return ask_for_track(year)

    if re.search(r'c!formula[ ]?1 (\d{4}) (.+)', p_message):
        year_match = re.search(r'c!formula[ ]?1 (\d{4}) (.+)', p_message)
        if year_match:
            year = int(year_match.group(1))
            track_name = year_match.group(2).strip()
            race_results = get_formula1_race_results(year, track_name)
            driver_standings = get_formula1_driver_standings(year, track_name)

            if race_results:
                response_str = f"Formula 1 {year} Season - {track_name}:\n" + "\n".join(race_results)
            else:
                response_str = f"Failed to fetch Formula 1 race results for {track_name}."

            if driver_standings:
                response_str += f"\n\nDriver Standings ({year}, {track_name}):\n" + "\n".join(driver_standings)
            else:
                response_str += f"\n\nFailed to fetch Formula 1 standings for {track_name}."

            return response_str

        else:
            return "Invalid command format. Use `c!formula1 [year] [track]` to get Formula 1 race results for a specific year and track."

    return 'Oops! I didn’t get that. Try `c!help` for a list of commands.'

if os.getenv('DEBUG_MODE'):
    user_message = input("Enter a message: ")
    response = handle_response(user_message)
    print(response)
    user_message = input




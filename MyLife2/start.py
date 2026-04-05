import random
import os
import json

def _all_jobs():
    path = os.path.join(os.path.dirname(__file__), "jobs.json")
    with open(path) as f:
        data = json.load(f)
    return [job for jobs in data["careers"].values() for job in jobs]

def random_job():
    return random.choice(_all_jobs())["name"]

def random_salary(name):
    for job in _all_jobs():
        if job["name"] == name:
            return job["salary"]

def worst_of_three_jobs():
    jobs = [random_job() for _ in range(3)]
    return min(jobs, key=lambda j: random_salary(j))

def random_lifestyle(salary):
    x = salary / 1000
    lifestyles = [
        ('Squalid',      -1/8,       15),
        ('Poor',         -1/9,       31),
        ('Lower Class',  -1/10,      50),
        ('Middle Class', -1/85,     100),
        ('Upper Class',  -1/110,    190),
        ('Comfortable',  -1/750,    400),
        ('Rich',         -1/7000,  1000),
        ('Millionaire',  -1/200000, 4000),
    ]
    names   = [l[0] for l in lifestyles]
    weights = [max(0, coef * (x - peak)**2 + 50) for _, coef, peak in lifestyles]
    return random.choices(names, weights=weights, k=1)[0]

def _load_names():
    path = os.path.join(os.path.dirname(__file__), "names.txt")
    with open(path) as f:
        return f.readlines()

def boy_name():
    lines = _load_names()
    even_lines = [lines[i] for i in range(1, len(lines), 2)] 
    return random.choice(even_lines).split()[0]

def girl_name():
    lines = _load_names()
    odd_lines = [lines[i] for i in range(0, len(lines), 2)] 
    return random.choice(odd_lines).split()[0]

def last_name():
    lines = _load_names()
    return random.choice(lines).split()[1]

Genders = ['Male', 'Female']

_white_sub = [
    'German', 'English', 'Irish', 'Italian', 'Scottish', 'French', 'Polish',
    'Dutch', 'Norwegian', 'Swedish', 'Russian', 'Greek', 'Portuguese',
    'Welsh', 'Danish', 'Hungarian', 'Czech',
    'American',       # old-stock Americans who just identify as "American"
    'Scotch-Irish', 'French Canadian', 'Jewish (Ashkenazi)', 'Arab American',
    'Ukrainian', 'Finnish', 'Austrian', 'Swiss', 'Slovak', 'Armenian',
    'Romanian', 'Croatian', 'Serbian', 'Lithuanian', 'Belgian',
    'Iranian/Persian', 'Albanian', 'Latvian', 'Bulgarian', 'Slovenian',
    'Other White',
]
_white_weights = [
    14, 13, 11, 6, 3, 3, 2.5,
    1.4, 1.5, 1.5, 1.0, 0.6, 0.5,
    0.5, 0.6, 0.55, 0.6,
    15,
    3.0, 1.5, 1.5, 1.5,
    0.6, 0.5, 0.6, 0.5, 0.5, 0.5,
    0.4, 0.4, 0.3, 0.3, 0.3,
    0.7, 0.2, 0.15, 0.15, 0.15,
    10,
]

_black_sub = [
    'African American', 'Jamaican', 'Haitian', 'Nigerian', 'Ethiopian',
    'Somali', 'Ghanaian', 'Trinidadian', 'Kenyan',
    'Guyanese', 'Liberian', 'Sudanese', 'Eritrean', 'Cameroonian',
    'Ugandan', 'Congolese', 'Sierra Leonean', 'Barbadian', 'Senegalese',
    'West Indian', 'West African', 'East African', 'Central African',
    'Belizean', 'Zimbabwean', 'Tanzanian', 'South African',
    'Ivorian', 'Rwandan', 'Malian', 'Angolan',
    'Other Black',
]
_black_weights = [
    54, 2.2, 2.2, 1.3, 0.7,
    0.5, 0.4, 0.4, 0.2,
    0.5, 0.4, 0.3, 0.2, 0.2,
    0.2, 0.2, 0.2, 0.2, 0.15,
    5.5, 8.5, 3.5, 2.5,
    0.4, 0.3, 0.3, 0.3,
    0.3, 0.2, 0.25, 0.2,
    10,
]

_hispanic_sub = [
    'Mexican', 'Puerto Rican', 'Dominican', 'Cuban', 'Salvadoran',
    'Guatemalan', 'Colombian', 'Honduran',
    'Venezuelan', 'Ecuadorian', 'Peruvian', 'Nicaraguan', 'Argentinian',
    'Chilean', 'Bolivian', 'Panamanian', 'Costa Rican', 'Uruguayan',
    'Other Hispanic',
]
_hispanic_weights = [
    60, 10, 3, 4, 3,
    2, 2, 1.5,
    1.7, 1.5, 1.0, 0.7, 0.7,
    0.4, 0.3, 0.3, 0.3, 0.1,
    7.5,
]

_asian_sub = [
    'Chinese', 'Indian', 'Filipino', 'Vietnamese', 'Korean', 'Japanese',
    'Pakistani', 'Hmong', 'Cambodian', 'Thai', 'Taiwanese',
    'Laotian', 'Bangladeshi', 'Burmese', 'Nepalese', 'Indonesian',
    'Other Asian',
]
_asian_weights = [
    22, 21, 19, 9, 8, 6,
    2.5, 1.4, 1.1, 0.9, 0.85,
    0.8, 0.8, 0.9, 0.9, 0.4,
    4.45,
]

def _sub_race(broad):
    if broad == 'White':
        return random.choices(_white_sub, weights=_white_weights, k=1)[0]
    if broad == 'Black or African American':
        return random.choices(_black_sub, weights=_black_weights, k=1)[0]
    if broad == 'Hispanic':
        return random.choices(_hispanic_sub, weights=_hispanic_weights, k=1)[0]
    if broad == 'Asian':
        return random.choices(_asian_sub, weights=_asian_weights, k=1)[0]
    return broad

_base_ethnicities = [
    'White',
    'Black or African American',
    'Hispanic',
    'Asian',
    'American Indian and Alaska Native',
    'Native Hawaiian and Other Pacific Islander',
]

_base_weights = [63.44, 12.36, 6.60, 5.82, 0.88, 0.19]

_ethnicity_pool = (
    ['White'] * 6344 +
    ['Black or African American'] * 1236 +
    ['Multiracial'] * 1071 +
    ['Hispanic'] * 660 +
    ['Asian'] * 582 +
    ['American Indian and Alaska Native'] * 88 +
    ['Native Hawaiian and Other Pacific Islander'] * 19
)

def random_ethnicity():
    result = random.choice(_ethnicity_pool)
    if result == 'Multiracial':
        first = random.choices(_base_ethnicities, weights=_base_weights, k=1)[0]
        remaining = [e for e in _base_ethnicities if e != first]
        remaining_weights = [w for e, w in zip(_base_ethnicities, _base_weights) if e != first]
        second = random.choices(remaining, weights=remaining_weights, k=1)[0]
        return f'Multiracial ({_sub_race(first)} & {_sub_race(second)})'
    return _sub_race(result)

_base_lifestyle = [
    'Squalid',
    'Poor',
    'Lower Class',
    'Middle Class',
    'Upper Class',
    'Comfortable',
    'Rich',
    'Millionaire'
]

siblings_prob = [0]*5 + [1]*27 + [2]*13 + [3]*9 + [4]*8 + [5]*9 + [6]*1 + [7]*4 + [8]*1

EASY = 20
MEDIUM = 15
HARD = 10
NIGHTMARE = 7
IMPOSSIBLE = 4
CUSTOM = 999

difficulty = input(f"What difficulty would you like to select? Depending on your difficulty, you will have differing amounts of happy tokens to start with, which you can spend on getting bonuses, increases stats, or choosing a new family in the character creation menu, or you can spin the wheel of fortune in the main world. 1. Easy ({EASY} tokens) 2. Medium ({MEDIUM} tokens) 3. Hard ({HARD} tokens) 4. Nightmare ({NIGHTMARE} tokens) 5. Impossible ({IMPOSSIBLE}) tokens 6. Custom ({CUSTOM} tokens)")

if difficulty  == '1': tokens = EASY
elif difficulty == '2': tokens = MEDIUM
elif difficulty == '3': tokens = HARD
elif difficulty == '4': tokens = NIGHTMARE
elif difficulty == '5': tokens = IMPOSSIBLE
elif difficulty == '6': tokens = CUSTOM

reroll_cost = 0
picked = False

while picked == False:

    new_gender = random.choice(Genders)
    new_home_salary = 0

    if new_gender == 'Male': new_name = boy_name()
    else: new_name = girl_name()
    new_lname = last_name()

    new_siblings_count = random.choice(siblings_prob)
    new_siblings = []
    for i in range(new_siblings_count):

        sibling_gender = random.choice(Genders)

        if sibling_gender == 'Male': sibling_name = boy_name()
        else: sibling_name = girl_name()
        sibling_lname = new_lname
        new_siblings.append([sibling_name, sibling_lname, sibling_gender])

    new_mom_name = girl_name()
    new_dad_name = boy_name()
    
    new_ethnicity = random_ethnicity()

    new_dad_job = worst_of_three_jobs()
    new_home_salary += random_salary(new_dad_job)
    if random.randint(1,100) >= 26: new_mom_job = worst_of_three_jobs()
    else: new_mom_job = "None"
    if new_mom_job == "None": new_home_salary += 0
    else: new_home_salary += random_salary(new_mom_job)

    new_lifestyle = random_lifestyle(new_home_salary)

    choice = input(f"{new_name + ' ' + new_lname}, with {new_siblings_count} siblings, who are {', '.join(s[0] + ' ' + s[1] for s in new_siblings)}. Your mom's name is {new_mom_name} while your dad's name is {new_dad_name}. Your ethnicity is {new_ethnicity}, your total salary is {new_home_salary}, with your mom's job being {new_mom_job} and your dad's job being {new_dad_job}. You live a {new_lifestyle} lifestyle. Would you like to reroll (y/n)? If you accept, it will cost {reroll_cost} happy tokens, otherwise this will be your character.")
    reroll_cost += 1

    if choice == 'n':
        picked = True

good_traits = ["Sportsy: Effective Strength is increased by 50% when doing Sports (1 happy token)",
               "Strategic: Effective Intellect is increased by 100% when playing board games, card games, or video games (1 happy token)",
               "Engergetic: Energy loss is slowed by 25% (2 happy tokens)",
               "Tricky: Effectice Sleight of Hand is increased by 50% (2 happy tokens)",
               "Perceptive: Effective Perception is increased by 75% (2 happy tokens)",
               "Agressive: Effective Intimidation is increased by 50%" + " and Effective Strength is increased by 25% while dealing damage to another human (2 happy tokens)",
               "Manipulative: Effective Deception is increased by 50%" + " on family or friends, or 25%" + " on anyone else (3 happy tokens)",
               "Charming: Effective Persuasion is increased by 50%" + " on family or friends, or 25%" + " on anyone else (3 happy tokens)",
               "Fighter: Effective Strength is increased by 50% when dealing damage to another human (3 happy tokens)",
               "Nerdy: Effective Intellect is increased by 50% when doing math, science, english, history, or foriegn languages (4 happy tokens)",
               "Seller: Effective Persuasion is increased by 50% when selling something (4 happy tokens)",
               "Resillient: Take 50%" + " less damage when it deals less then half your max health (4 happy tokens)",
               "Engineer: Effective Intellect is increased by 50% when building something with technology (5 happy tokens)",
               "Survivor: The first time you drop to 0 health, drop to 10 health instead of dying (5 happy tokens)",
               "Psychopath: Effective Deception is increased by 100% " + " and you regenerate all lost energy when commiting a major crime (6 happy tokens)",
               "Natural: The first time you gain a skill, it starts at Level 3 instead of Level 1 (7 happy tokens)"]

good_traits_weights = [1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 7]

def reroll_traits():
    global good_traits
    global good_traits_weights
    random_good_traits = []
    random_traits_weights = []
    for i in range(3): random_good_traits.append(random.choice(good_traits))
    for i in range(3): random_traits_weights.append(good_traits_weights[good_traits.index(random_good_traits[i])])
    return random_good_traits, random_traits_weights

picked = False
new_good_traits, new_good_weights = reroll_traits()
new_traits = []

while picked == False:

    choice = input(f"""Choose a trait by typing 1-3, reroll for 1 happy token by typing r, and exit by typing e. The traits are:
                   1. {new_good_traits[0]}
                   2. {new_good_traits[1]}
                   3. {new_good_traits[2]}""")

    if choice == '1' and tokens >= new_good_weights[0]:
        new_traits.append(new_good_traits[0])
        tokens -= new_good_weights[0]
    elif choice == '2' and tokens >= new_good_weights[1]:
        new_traits.append(new_good_traits[1])
        tokens -= new_good_weights[1]
    elif choice == '3' and tokens >= new_good_weights[2]:
        new_traits.append(new_good_traits[2])
        tokens -= new_good_weights[2]
    elif choice == 'r' and tokens > 0: new_good_traits, new_good_weights = reroll_traits()
    elif choice == 'e': picked = True

for i, trait in enumerate(new_traits):
    split_trait = trait.split()
    new_traits[i] = split_trait[0][0:-1]

new_strength = 0
new_smarts = 0
new_looks = 0

while tokens != 0:

    choice = input(f"""You have {tokens} tokens. You can spend one of your tokens on: 
          1. Strength {new_strength}/10: This represents your physical brawnyness, speed, and resilience. If you get a heart attack, a high score in this might save you. 0 is a literal ragdoll, and 10 is world-class bodybuilder.
          2. Smarts {new_smarts}/10: This represents your intellectual power, but your creativity is up to you, not your character. However, when provided with learning something new or an intellectlly challenging task, this might be useful. 0 is borderline intelltual disability, and 10 is prodigy.
          3. Looks {new_looks}/10: This isn't just your physical looks, but your voice and how you come across to an outsider. Super useful when trying to persuade other people or trick them into doing something. This is super underated. 0 is ugly as hell and sounds like an animal, and 10 is super good looking, charming, and deceptive person.""")

    if choice == '1': new_strength, tokens = new_strength + 1, tokens - 1
    if choice == '2': new_smarts, tokens = new_smarts + 1, tokens - 1
    if choice == '3': new_looks, tokens = new_looks + 1, tokens - 1

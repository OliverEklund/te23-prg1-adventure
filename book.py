format = [
    {
        "id": 1,
        "title": "String title for page",
        "text": "String text for page",
        "options": [
            {"text": "Option 1 with next page id", "next_id": 2},
            {"text": "Option 2 with next page id", "next_id": 3},
        ],
    },
]
BOOK = [
 
    {
        "id": 1,
        "title": "The Journey Begins",
        "text": "You are Sir Aldric, a noble knight from the kingdom of Eldoria. The king has entrusted you to find items of interest which is measured in score. Your journey begins in the bustling medieval town of Redhaven. Do you...",
        "options": [
            {"text": "Visit the local blacksmith for better gear.", "next_id": 2},
            {"text": "Set out immediately towards the haunted forest.", "next_id": 3}
        ],
    },
    {
        "id": 2,
        "title": "The Blacksmith’s Forge",
        "text": "The blacksmith, a burly man named Gorin, greets you with a nod. 'A knight on a quest, eh? I have fine weapons and armor. But they come at a price.' Do you...",
        "options": [
            {"text": "Purchase a Silver longsword.", "next_id": 4},
            {"text": "Try to barter for a better price.", "next_id": 5},
            {"text": "Leave without buying anything.", "next_id": 3}
        ],
    },
    {
        "id": 3,
        "title": "The Haunted Forest",
        "text": "The trees loom high, their twisted branches forming eerie silhouettes in the mist. Strange whispers echo through the woods. Suddenly, a pair of glowing red eyes emerge from the darkness. A pack of shadow wolves surround you! Do you...",
        "options": [
            {"text": "Draw your sword and fight.", "next_id": 6},
            {"text": "Attempt to scare them away.", "next_id": 7},
            {"text": "Climb a tree and wait them out.", "next_id": 8}
        ],
    },
    {
        "id": 4,
        "title": "Armed and Ready",
        "text": "You purchase the silver longsword. Gorin nods approvingly. 'A fine choice, knight. This blade will serve you well.' Feeling better prepared, you set off towards the haunted forest.",
        "options": [
            {"text": "Head to the haunted forest.", "next_id": 3}
        ],
        "loot": "Silver Longsword",
    },
    {
        "id": 5,
        "title": "The Blacksmith’s Wrath",
        "text": "Gorin's expression darkens. 'You insult my craft, knight?' Before you can react, he swings his massive hammer down upon you. Your adventure ends here.",
        "options": [],
    },
    {
        "id": 6,
        "title": "Battle with the Shadow Wolves",
        "text": "You draw your sword to fight, but you are outnumbered and your blade barely scratches the wolves. They overwhelm you, and your journey comes to a tragic end.",
        "options": [],
    },
    {
        "id": 7,
        "title": "A Failed Attempt",
        "text": "You attempt to scare the wolves away by shouting and waving your arms, but they are unfazed. They lunge at you, and your journey ends here.",
        "options": [],
    },
    {
        "id": 8,
        "title": "A Clever Escape",
        "text": "You quickly climb a nearby tree, evading the wolves. They snarl and pace below for what feels like hours before eventually slinking back into the shadows. You descend and cautiously continue your journey.",
        "options": [
            {"text": "Continue deeper into the forest.", "next_id": 9}
        ],
    },
        {
            "id": 9,
        "title": "The Ruined Wagon",
        "text": "You venture further down the road into the haunted forest. Suddenly, you come upon a clearing where a ruined wagon lies abandoned. Perched atop the wreckage, a monstrous mantis feasts on a classic halfling dish: a gigantic meat pie. The creature has yet to notice you. Do you...",
        "options": [
            {"text": "Attempt to sneak past the mantis.", "next_id": 10},
            {"text": "Confront the mantis head-on.", "next_id": 11},
            {"text": "Observe the mantis quietly.", "next_id": 12}
        ],
    },
    {
        "id": 10,
        "title": "A Silent Strike",
        "text": "You carefully sneak around the mantis. It remains engrossed in its meal, oblivious to your presence. You now have a choice: strike it down or continue on your way. Do you...",
        "options": [
            {"text": "Kill the mantis and loot the wagon.", "next_id": 13},
            {"text": "Leave the mantis alone and walk past it.", "next_id": 14}
        ],
    },
    {
        "id": 11,
        "title": "A Foolish Confrontation",
        "text": "You charge at the mantis with your weapon drawn, but it reacts with lightning speed. With a swift and brutal strike, it cuts you down. Your adventure ends here.",
        "options": [],
    },
    {
        "id": 12,
        "title": "Patience Pays Off... Mostly",
        "text": "You observe the mantis from a safe distance. After finishing its meal, it skitters away into the forest. You cautiously approach the wagon and search for loot, but the mantis's appetite has left only scraps behind.",
        "options": [
            {"text": "Take what little remains and continue on.", "next_id": 14}
        ],
        "loot": "Paper Scraps",
    },
    {
        "id": 13,
        "title": "Victory and Spoils",
        "text": "You strike the mantis down before it even realizes the danger. Searching the wagon, you find valuable supplies and a enchanted cookbook. Feeling victorious, you continue on your quest.",
        "options": [
            {"text": "Continue deeper into the forest.", "next_id": 14}
        ],
        "loot": "Enchanted Cookbook",
    },
    {
        "id": 14,
        "title": "Deeper into the Unknown",
        "text": "With the wagon behind you, you press on into the darkened woods, unsure of what awaits you next...",
        "options": [
            {"text": "Continue your journey.", "next_id": 15}
        ],
    },
    {
        "id": 15,
        "title": "The Rickety Bridge",
        "text": "As you continue down the road, the haunted forest begins to thin. A rickety wooden bridge stretches over a fast-moving river, marking the way out of the haunted forest. However, as you approach, a ghostly figure materializes before you. It is the spectral form of an orc jester, dressed in tattered motley, juggling ghostly skulls. 'Ho there, traveler!' the jester cackles. 'Will you spare a moment for a chat with a lonely spirit?' Do you...",
        "options": [
            {"text": "Walk past the ghost without engaging.", "next_id": 16},
            {"text": "Attempt to exorcise the ghost.", "next_id": 17},
            {"text": "Speak with the ghost.", "next_id": 18}
        ],
    },
    {
        "id": 16,
        "title": "Safe Passage",
        "text": "You ignore the ghostly jester and walk past him without incident. Soon, you reach the other side of the bridge and step into a vast field stretching towards distant mountains.",
        "options": [
            {"text": "Venture into the great field.", "next_id": 19}
        ],
    },
    {
        "id": 17,
        "title": "A Foolish Attempt",
        "text": "You attempt to exorcise the ghost, chanting sacred verses and raising your sword. However, this only exposes you to the spirit realm. With a wicked grin, the jester snaps his fingers, and your soul is ripped from your body, joining the spectral skulls in his collection. Your adventure ends here.",
        "options": [],
    },
    {
        "id": 18,
        "title": "A Laughable Encounter",
        "text": "You decide to humor the ghost and listen to his joke. 'Why did the orc bring a ladder to the bar? Because he heard the drinks were on the house!' The ghost cackles madly at his own joke and waves you along. 'You're alright, knight! Onward you go!' You cross the bridge safely.",
        "options": [
            {"text": "Step into the great field.", "next_id": 19}
        ],
    },
    {
        "id": 19,
        "title": "The Vast Field",
        "text": "Beyond the haunted forest, a great field stretches out before you, golden grass swaying in the breeze. In the far distance, the silhouette of a mountain looms, marking the next stage of your journey. What do you do?",
        "options": [
            {"text": "Head towards the mountain.", "next_id": 20}
        ],
    },
    {
        "id": 20,
        "title": "The Vast Field",
        "text": "Beyond the haunted forest, a great field stretches out before you, golden grass swaying in the breeze. In the far distance, the silhouette of a mountain looms, marking the next stage of your journey. As you walk, a strange scent fills the air. The unmistakable smell of pickles. This can only mean one thing – the Green Knight is here. A powerful centaur knight known for his green taste in vegetables and his knack for preserving food of all types. He wields a halberd and is ruthless in battle. Do you...",
        "options": [
            {"text": "Challenge the Green Knight to combat.", "next_id": 21},
            {"text": "Attempt to reason with the Green Knight.", "next_id": 22},
            {"text": "Try to sneak past him.", "next_id": 23}
        ],
    },
    
    {
        "id": 21,
        "title": "Duel with the Green Knight",
        "text": "You draw your weapon and engage in an intense duel with the Green Knight. The fight is long and grueling, your skills matched against his ruthless precision. Eventually you land a lucky strike on him. As you move in to finish him off he horse-kicks you in the chin, giving the green knight enough time to retreat into the horizon. At least you still have your life.",
        "options": [
             {"text": "Advance toward the mountain.", "next_id": 26}
        ],
    },

    {
        "id": 22,
        "title": "Negotiating with the Green Knight",
        "text": "You attempt to reason with the Green Knight. He listens carefully, then asks you a question: 'Tell me, knight, where might I find an unpreserved meal worthy of my refined palate?' How you answer may determine your fate.",
        "options": [
            {"text": "Suggest the market in Redhaven.", "next_id": 25},
            {"text": "Tell him of the halfling pie in the haunted forest.", "next_id": 24}
        ],
    },

    {
        "id": 23,
        "title": "A Silent Escape",
        "text": "Using the tall grass as cover, you carefully sneak past the Green Knight. He remains oblivious to your presence, too focused on admiring his latest jar of pickled turnips. Once safely past, you continue toward the mountain.",
        "options": [
            {"text": "Advance toward the mountain.", "next_id": 26}
        ],
    },
    {
        "id": 24,
        "title": "The Green Knight Departs",
        "text": "Hearing of the halfling pie, the Green Knight’s eyes widen with interest. Without another word, he gallops off toward the haunted forest in search of his next great meal, leaving you free to continue your journey.",
        "options": [
            {"text": "Advance toward the mountain.", "next_id": 26}
        ],
    },
    {
        "id": 25,
        "title": "Battle with the Green Knight",
        "text": "BARBARIANS! The green knight screams in rage and charges at you. You draw your sword to prepare for duel. The fight is long and grueling, your skills matched against his ruthless precision. You nearly triumph, but in the end due to you being unprepared to fight, his halberd finds its mark. You fall, your quest coming to a valiant end.",
        "options": [],
    },
    {
        "id": 26,
        "title": "The Cave Shelter",
        "text": "As you continue toward the mountain, night begins to fall. The temperature drops, and the shadows stretch long across the land. Ahead, nestled between rocky outcroppings, you spot a small cave. It looks like a safe place to rest for the night. Do you...",
        "options": [
            {"text": "Enter the cave and rest.", "next_id": 27},
            {"text": "Continue traveling through the night.", "next_id": 28}
        ],
    },
    {
        "id": 26,
        "title": "The Cave's Depths",
        "text": "You settle near the entrance, but curiosity gets the better of you. As you venture deeper into the cave, a storm begins to rage outside. The deeper you go, the more mysterious the cave becomes...",
        "options": [
            {"text": "Press forward into the darkness.", "next_id": 28},
            {"text": "Turn back and rest near the entrance.", "next_id": 29}
        ],
    },

    {
        "id": 27,
        "title": "Through the Night",
        "text": "You decide to press on through the night, though exhaustion weighs heavily on you. The moonlight guides your path as you push forward across the mountains, ever wary of what dangers might lurk in the darkness...",
        "options": [
            {"text": "Continue across the mountains.", "next_id": 30}
        ],
    }
    {
        "id": 28,
        "title": "A treasure in the depths",
        "text": "As you venture deeper into the cave. Eventually stumbling across a collection of corpses around a cannon-like contraption. You look closer and there is a piece of paper in it which says, Recoilless rifle",
        "options": [
            {"text": "Take the Recoilless Rifle", "next_id": 32}
            {"text": "Dont take the the Recoilless Rifle, just kidding take it. Dont tell me you would actually just leave this behind?", "next_id": 32}
        ],
    },

    {
        "id": 29,
        "title": "Morning Departure",
        "text": "You decide to rest near the entrance. As dawn breaks, you awaken refreshed and set out toward the mountain, traversing its rocky paths safely.",
        "options": [
            {"text": "Continue over the mountains.", "next_id": 31}
        ],
    },

    {
        "id": 30,
        "title": "The Mountain Troll",
        "text": "As you press on through the night, you come across a massive cave opening. A towering mountain troll emerges, blocking your path. 'No one passes without answering my riddles,' he bellows. Your wit will decide your fate.",
        "options": [],
    }
]




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
        "text": "You are Sir Aldric, a noble knight from the kingdom of Eldoria. The king has entrusted you with a perilous quest: to hunt an evil vampire. Your journey begins in the bustling medieval town of Redhaven. Do you...",
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
            {"text": "Purchase a Silber longsword.", "next_id": 4},
            {"text": "Try to barter for a better price.", "next_id": 5},
            {"text": "Leave without buying anything.", "next_id": 3}
        ],
    },
    {
        "id": 3,
        "title": "The Haunted Forest",
        "text": "The trees loom high, their twisted branches forming eerie silhouettes in the mist. Strange whispers echo through the woods. Suddenly, a pair of glowing red eyes emerge from the darkness. A pack of shadow wolves surround you! Do you...",
        "options": [
            {"text": "Draw your sword and fight.", "next_id": 6, "requires": "Silver Longsword"},
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
]



from book import BOOK

inventory = []
score = 0
def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_page(book_data, page_id):
    for page in book_data:
        if page["id"] == page_id:
            return page
    return None

def show_page(page):
    print(page["title"])
    print(page["text"])
    for i, option in enumerate(page["options"]):
        print(f"{i + 1}. {option['text']}")
        if "requires" in option:
            if option["requires"] and (option["requires"]) in inventory:
                #nu kan du välja detta
                print(f"This requires the {option["requires"]} item")
        else:
            print("")

def main():
    current_id = 1
    inventory = []
    while True and current_id is not None:
        current_page = get_page(BOOK, current_id)
        show_page(current_page)
        if "loot" in current_page:
            print(f"You found {current_page['loot']}!")
            inventory.append(current_page["loot"])
            score = score + 1
        choice = input_int("Enter your choice: ")
        print(inventory) 
        print(f"Score: {score}")
        if 1 <= choice <= len(current_page["options"]):
            current_id = current_page["options"][choice - 1]["next_id"]
        else:
            print("Invalid choice. Please try again.")
            current_id = None

if __name__ == "__main__":
    main()
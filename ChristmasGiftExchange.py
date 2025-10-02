from random import shuffle

def secret_santa():
    print("🎄 Welcome to the Secret Santa Generator! 🎁")
    print("Enter the names of all participants.")
    print("Type 'done' when you are finished.\n")

    people = []
    while True:
        person = input("Enter a name (or 'done' to finish): ").strip()
        if person.lower() == "done":
            break
        if person:  # skip empty entries
            people.append(person)

    if len(people) < 2:
        print("❌ You need at least 2 participants for Secret Santa.")
        return

    shuffle(people)
    # Each person gives a gift to the next in the shuffled list
    receivers = [people[-1]] + people[:-1]

    print("\n🎅 Secret Santa Results 🎅")
    print("----------------------------")
    for giver, receiver in zip(people, receivers):
        print(f"{giver} → gives a gift to → {receiver}")
    print("----------------------------")
    print("✨ Merry Christmas! ✨")

if __name__ == "__main__":
    secret_santa()

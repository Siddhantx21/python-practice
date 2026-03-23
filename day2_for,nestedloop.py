team = ["Siddhant - ML", "Friend 1 - Coder", "Friend 2 - Electronics"]

print("\n=== MY DREAM TEAM ===")
for member in team:
    print("\nMember:", member)
    for char in member:  # nested loop to go through each character
        print("-", char)

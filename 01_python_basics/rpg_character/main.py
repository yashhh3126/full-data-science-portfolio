def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return "Error: Name must be a string."
    if len(name) > 10:
        return "Error: Name is too long."
    if " " in name:
        return "Error: Name should not contain spaces."

    stats = [strength, intelligence, charisma]

    if not all(isinstance(stat, int) for stat in stats):
        return "Error: All stats must be integers."
    if any(stat < 1 for stat in stats):
        return "Error: Stats must be >= 1."
    if any(stat > 4 for stat in stats):
        return "Error: Stats must be <= 4."
    if sum(stats) != 7:
        return "Error: Total stats must equal 7."

    def stat_bar(value):
        return "●" * value + "○" * (10 - value)

    return (
        f"{name}\n"
        f"STR {stat_bar(strength)}\n"
        f"INT {stat_bar(intelligence)}\n"
        f"CHA {stat_bar(charisma)}"
    )


print(create_character("Yash", 4, 2, 1))

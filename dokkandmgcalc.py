def calculate_damage_taken(enemy_sa_damage, defense, damage_reduction, type_mod, class_mod, guard):
    """
    Calculate the damage a unit will take from a super attack in Dokkan Battle.

    Parameters:
    enemy_sa_damage: The enemy's super attack damage (raw value).
    defense: The unit's effective defense.
    damage_reduction: Damage reduction rate (0 to 1, e.g., 0.3 for 30%).
    type_mod: String for type modifier ("neutral", "advantage", "disadvantage").
    class_mod: String for class modifier ("neutral", "advantage", "disadvantage").
    guard: Whether Guard is active (True or False).

    Returns:
    The final damage taken by the unit.
    """
    # Map type and class modifiers to multipliers
    type_modifiers = {
        "neutral": 1.0,
        "advantage": 0.5,
        "disadvantage": 1.5
    }
    class_modifiers = {
        "neutral": 1.0,
        "advantage": 1.0,  # Class advantage is not a typical Dokkan mechanic, but added for completeness
        "disadvantage": 1.25
    }

    # Get the correct multipliers
    type_multiplier = type_modifiers.get(type_mod.lower(), 1.0)  # Default to neutral if invalid input
    class_multiplier = class_modifiers.get(class_mod.lower(), 1.0)  # Default to neutral if invalid input

    # Apply defense
    reduced_damage = max(0, enemy_sa_damage - defense)

    # Apply damage reduction
    reduced_damage *= (1 - damage_reduction)

    # Apply Guard (if active, treated as 30% additional reduction)
    if guard:
        reduced_damage *= 0.7  # Equivalent to 30% mitigation

    # Apply type modifier
    reduced_damage *= type_multiplier

    # Apply class modifier
    reduced_damage *= class_multiplier

    return reduced_damage

# Example Values:
enemy_sa_damage = 1000000  # Enemy's super attack damage
defense = 200000  # Your unit's defense after buffs
damage_reduction = 0.3  # 30% damage reduction
type_mod = "neutral"  # Type interaction (neutral, advantage, disadvantage)
class_mod = "disadvantage"  # Class interaction (neutral, advantage, disadvantage)
guard = True  # Guard is active

# Calculate Damage Taken
damage_taken = calculate_damage_taken(enemy_sa_damage, defense, damage_reduction, type_mod, class_mod, guard)

# Print the Result
print(f"Damage Taken: {damage_taken}")

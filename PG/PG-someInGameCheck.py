from math import floor

# calculation of Unrest level in a game tribe based on various factors
def calculate_unrest(
    B: int,  # Base issues (0-100 scale)
    R: int = 0,  # Race discontent (if applicable) (0-100 scale)
    G: int = 0,  # Goblin activity level (if applicable) (0-100 scale)
    D_days: int = 0,  # Days without religious ceremonies (if applicable) (count 0 on start)
    Z: int = 0,  # Orcks Blood Frenzy level (if applicable) (0-100 scale)
    O_losses: int = 0,  # O_losses (number of losses in recent battles) (count 0 on start)
    renown: int = 0,  # Renown (increases loyalty)
    companion_events: int = 0,  # Number of companion events (increases loyalty)
    clamp_result: bool = True  # Whether to clamp the result between 0 and 100
):
    """
    Unrest U = B + R + O + G + D + Z − L
    where: 
    - 0 = min(5 * O_losses, 20) #Capped at 20
    - D = min(5 * D_days, 20) #Capped at 20
    - L_raw = renown // 10 + companion_events / 2
    - L = min(L_raw, 25) #Capped at 25
    """

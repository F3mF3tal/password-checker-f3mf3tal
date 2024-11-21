# Import des bibliothèques nécessaires
import hashlib
import requests
import re

# 1. Fonction pour afficher la bannière
def display_banner():
    banner = """
███████╗██████╗ ███╗   ███╗███████╗██████╗ ████████╗ █████╗ ██╗     
██╔════╝╚════██╗████╗ ████║██╔════╝╚════██╗╚══██╔══╝██╔══██╗██║     
█████╗   █████╔╝██╔████╔██║█████╗   █████╔╝   ██║   ███████║██║     
██╔══╝   ╚═══██╗██║╚██╔╝██║██╔══╝   ╚═══██╗   ██║   ██╔══██║██║     
██║     ██████╔╝██║ ╚═╝ ██║██║     ██████╔╝   ██║   ██║  ██║███████╗
╚═╝     ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚══════╝                                            
for the security of everyone
"""
    print(banner)
    print("\nHey, je suis F3mF3tal.")
    print("Nous allons ensemble regarder si ton mot de passe est assez solide.\n")

# 2. Vérifier la force du mot de passe
def check_password_strength(password: str) -> dict:
    score = 0
    feedback = []

    # Vérifie la longueur du mot de passe
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Votre mot de passe doit contenir au moins 8 caractères.")

    # Vérifie la présence de majuscules, minuscules, chiffres, caractères spéciaux
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Ajoutez au moins une lettre majuscule.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Ajoutez au moins une lettre minuscule.")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Ajoutez au moins un chiffre.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Ajoutez au moins un caractère spécial (!@#$...).")

    return {
        "score": score,
        "feedback": feedback
    }

# 3. Générer des conseils
def generate_advice(score: int, feedback: list) -> str:
    if score == 5:
        return "✅ Votre mot de passe est fort !"
    else:
        return "⚠️ Conseils pour améliorer votre mot de passe :\n" + "\n".join(feedback)

# 4. Le menu principal
def main():
    while True:
        print("\n=== Menu ===")
        print("1. Vérifier un mot de passe")
        print("2. Quitter")
        choice = input("Choisissez une option : ")

        if choice == "1":
            password = input("Entrez un mot de passe pour l'évaluer : ")

            # Vérification de la force
            strength = check_password_strength(password)
            print(f"\n🔐 Score de sécurité : {strength['score']}/5")
            print(generate_advice(strength['score'], strength['feedback']))

        elif choice == "2":
            print("\nMerci d'avoir utilisé F3mF3tal Security. À bientôt !")
            break

        else:
            print("Option invalide. Veuillez réessayer.")

# 5. Point d'entrée du programme
if __name__ == "__main__":
    display_banner()
    main()
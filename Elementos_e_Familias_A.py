import random
from colorama import Fore, Style, init

elements = {"H": "Hidrogenio", "He": "Helio", "Li": "Litio", "Be": "Berilio",
			"B": "Boro", "C": "Carbono", "N": "Nitrogenio", "O": "Oxigenio",
			"F": "Fluor", "Ne": "Neonio", "Na": "Sodio", "Mg": "Magnesio",
			"Al": "Aluminio", "Si": "Silicio", "P": "Fosforo", "S": "Enxofre",
			"Cl": "Cloro", "Ar": "Argonio", "K": "Potassio", "Ca": "Calcio",
			"Sc": "Escandio", "Ti": "Titanio", "V": "Vanadio", "Cr": "Cromio",
			"Ni": "Niquel", "Cu": "Cobre", "Zn": "Zinco", "Ga": "Galio",
			"Ge": "Germanio", "As": "Arsenio", "Se": "Selenio", "Br": "Bromo",
			"Kr": "Criptonio", "Rb": "Rubideo", "Sr": "Estroncio", "Y": "Itrio",
			"Zr": "Zirconio", "Nb": "Niobio", "Mo": "Molibdenio", "Tc": "Tecnesio",
			"Ru": "Rutenio", "Rh": "Rodio", "Pd": "Paladio", "Ag": "Prata",
			"Cd": "Cadmio", "In": "Indio", "Sn": "Estanho", "Sb": "Antimonio",
			"Te": "Telurio", "I": "Iodo", "Xe": "Xenonio", "Cs": "Cesio",
			"Ba": "Bario", "La": "Lantanio", "Ce": "Cerio", "Pr": "Praseodimio",
			"Nd": "Neodimio", "Pm": "Promecio", "Sm": "Samario", "Eu": "Europio",
			"Gd": "Gadolinio", "Tb": "Terbio", "Dy": "Disprosio", "Ho": "Holmio",
			"Er": "Erbio", "Tm": "Tulio", "Yb": "Iterbio", "Lu": "Lutecio",
			"Ac": "Actinio", "Th": "Torio", "Pa": "Protactinio", "U": "Uranio",
			"Np": "Netunio", "Pu": "Plutonio", "Am": "Americio", "Cm": "Curio",
			"Bk": "Berquelio", "Cf": "Californio", "Es": "Einstenio", "Fm": "Fermio",
			"Md": "Mendelevio", "No": "Nobelio", "Lr": "Laurencio", "Rf": "Rutherfordio",
			"Fe": "Ferro", "Co": "Cobalto", "Hf": "Hafinio", "Ta": "Tantalo",
			"W": "Tungstenio", "Re": "Renio", "Os": "Osmio", "Ir": "Iridio",
			"Pt": "Platina", "Au": "Ouro", "Hg": "Mercurio", "Tl": "Talio",
			"Pb": "Chumbo", "Bi": "Bismuto", "Po": "Polonio", "At": "Astato",
			"Rn": "Radonio", "Fr": "Francio", "Ra": "Radio", "Mn": "Manganes"}

families = {"1A": [elements['H'], elements['Li'], elements['Na'], elements['K'], elements['Rb'], elements['Cs'], elements['Fr']],
			"2A": [elements['Be'], elements['Mg'], elements['Ca'], elements['Sr'], elements['Ba'], elements['Ra']],
			"3A": [elements['B'], elements['Al'], elements['Ga'], elements['In'], elements['Tl']],
			"4A": [elements['C'], elements['Si'], elements['Ge'], elements['Sn'], elements['Pb']],
			"5A": [elements['N'], elements['P'], elements['As'], elements['Sb'], elements['Bi']],
			"6A": [elements['O'], elements['S'], elements['Se'], elements['Te'], elements['Po']],
			"7A": [elements['F'], elements['Cl'], elements['Br'], elements['I'], elements['At']],
			"8A": [elements['He'], elements['Ne'], elements['Ar'], elements['Kr'], elements['Xe'], elements['Rn']]}

init()
print(f"{Fore.MAGENTA}Elementos Químicos. Feito por Everton Colombo em 12/03/2019{Style.RESET_ALL}\n\n")

def element():
	corrects = 0
	while True:
		try:
			simbol = random.choice(list(elements.keys()))
		except:
			break
		name = elements[simbol]
		elements.pop(simbol)
		print(f"{Fore.CYAN}Qual o elemento cujo simbolo é", Fore.YELLOW + "{}".format(simbol) + Style.RESET_ALL + "?", sep=' ')
		answer = input("R: ")
		print()
		if answer.upper() == name.upper():
			corrects += 1
			print(f"{Fore.GREEN}Correto!{Style.RESET_ALL}")
		else:
			print(f"{Fore.RED}Errado!{Style.RESET_ALL}" + "\nO correto seria" + Fore.YELLOW + " {}".format(name) + Style.RESET_ALL)
		print("\n-------\n")

	print("\n\n" + "=" * 40 + "\n\n")
	result = Style.BRIGHT + Fore.MAGENTA + str(corrects) + Style.RESET_ALL
	if corrects <= 52:
		print(Fore.RED + "Voce acertou apenas {}/104".format(result + Fore.YELLOW))
	else:
		print(Fore.GREEN + "Voce acertou {}/104".format(result + Fore.YELLOW))
	print(Style.RESET_ALL)
	input("Pressione ENTER para fechar...")


def family():
	cf = 0
	for f in families.keys():
		ac = True
		print()
		print('=' * 20)
		print(f"{Fore.CYAN} Familia: " + Fore.YELLOW + "{}".format(f) + Style.RESET_ALL)
		print('=' * 20)
		print()

		for e in families[f]:
			answer = input("{}/{}: ".format(families[f].index(e) + 1, len(families[f])))

			if answer.upper() == e.upper():
				print(f"{Fore.GREEN}Correto!{Style.RESET_ALL}")
			else:
				ac = False
				print(f"{Fore.RED}Errado!{Style.RESET_ALL}" + "\nO correto seria" + Fore.YELLOW + " {}".format(e) + Style.RESET_ALL)
			print("\n-------\n")
		cf += 1 if ac else 0
	print("\n\n" + "+" * 40 + "\n\n")
	result = Style.BRIGHT + Fore.MAGENTA + str(cf) + Style.RESET_ALL
	if cf <= 4:
		print(Fore.RED + "Voce acertou apenas {}/8".format(result + Fore.YELLOW))
	else:
		print(Fore.GREEN + "Voce acertou {}/8".format(result + Fore.YELLOW))
	print(Style.RESET_ALL)
	input("Pressione ENTER para fechar...")

if __name__ == "__main__":
	mode = input("'elementos' ou 'familias'? ")
	print()
	element() if mode == "elementos" else family() if mode == 'familias' else print(f"{Fore.RED}Erro")

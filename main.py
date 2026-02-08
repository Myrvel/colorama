from colorama import Fore, Back, Style, init

init(autoreset=True)

print(Fore.RED + "Червоний текст")
print(Back.GREEN + "Текст на зеленому фоні")
print(Style.BRIGHT + "Яскравий текст")
print(Style.RESET_ALL + "Звичайний текст")
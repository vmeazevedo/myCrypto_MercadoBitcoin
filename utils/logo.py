from pyfiglet import figlet_format

def logo(titulo):
    print("=" * 80)
    print(figlet_format(text=titulo, font="standard", justify="center"))
    print("=" * 80)
import os

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print("Fichye a pa jwenn.")
        return None

def write_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print("Kontni a anrejistre avèk siksè.")
    except Exception as e:
        print("Erè lè anrejistre kontni:", e)

def clean_text(text):
    cleaned_text = text.strip()  # Retire espas devan ak dèyè
    cleaned_text = ''.join(char for char in cleaned_text if char.isprintable())  # Retire karaktè espesyal
    return cleaned_text

def main():
    filename = input("Antre chemen fichye a: ")
    
    while True:
        print("\n1. Li kontni fichye")
        print("2. Modifye kontni")
        print("3. Netwaye tèks")
        print("4. Anrejistre kontni modifye nan menm fichye a")
        print("5. Anrejistre kontni modifye nan yon lòt fichye")
        print("6. Chèche ak ranplase mo")
        print("7. Sòti")
        
        choice = input("Chwazi yon aksyon: ")
        
        if choice == '1':
            content = read_file(filename)
            if content is not None:
                print("\nKontni Fichye:\n")
                print(content)
        elif choice == '2':
            content = read_file(filename)
            if content is not None:
                print("\nKontni kounye a:\n")
                print(content)
                edit_choice = input("Kisa ou vle fè? (Ajoute/Ajoute nan endèks): ")
                if edit_choice.lower() == "ajoute":
                    new_text = input("Antre tèks ou vle ajoute: ")
                    content += new_text
                elif edit_choice.lower() == "ajoute nan endèks":
                    index = int(input("Antre endèks kote ou vle ajoute tèks la: "))
                    new_text = input("Antre tèks ou vle ajoute: ")
                    content = content[:index] + new_text + content[index:]
                else:
                    print("Opsyon pa valab.")
        elif choice == '3':
            if 'content' in locals():
                content = clean_text(content)
                print("Tèks netwaye:\n")
                print(content)
            else:
                print("Pa gen kontni a modifye.")
        elif choice == '4':
            if 'content' in locals():
                write_file(filename, content)
            else:
                print("Pa gen kontni a modifye.")
        elif choice == '5':
            if 'content' in locals():
                new_filename = input("Antre chemen nouvo fichye a: ")
                if new_filename == filename:
                    print("Nou pa ka anrejistre nan menm non fichye a.")
                else:
                    write_file(new_filename, content)
            else:
                print("Pa gen kontni a modifye.")
        elif choice == '6':
            if 'content' in locals():
                search_text = input("Antre tèks ou vle chèche: ")
                replace_text = input("Antre tèks ou vle ranplase li ak: ")
                content = content.replace(search_text, replace_text)
            else:
                print("Pa gen kontni a modifye.")
        elif choice == '7':
            print("Pwogram lan ap fèmen.")
            break
        else:
            print("Opsyon pa valab. Chwazi yon opsyon ki nan lis la.")

if __name__ == "__main__":
    main()

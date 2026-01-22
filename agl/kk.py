class KK:
    
    word_index = list()
    tags = list()

    def __init__(self):
        self.tags.extend(["Kalba","Калба"])
        self.tags.extend(["English","Anglo","Аҥгло","Aŋglo"])

        self.title = input("Page Title: ")
        self.tags.append(self.title)

        self.dialog()

        input("Press ENTER to Close")
    
    def dialog(self):
        run_dialog = True

        while run_dialog:
            print("0)Compile HTML"+"\n"+"1)Add a word")

            match input("What would you like to do? "):
                case "0":
                    website = self.compile_website()

                    from os import chdir, path
                    chdir(path.dirname(path.realpath(__file__)))

                    f = open(f"index.html","w",encoding="utf-8")
                    f.write(website)
                    f.close()

                    run_dialog = False

                case "1":
                    self.word_index.append(self.make_word())
    
    def compile_website(self) -> str:
        html_components = list()

        html_components.append("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<link href=\"https://kalbejewde.github.io/kazmi.css\" rel=\"stylesheet\">")
        html_components.append("<link href=\"https://kalbejewde.github.io/k1.png\" type=\"image/png\" rel=\"icon\"/>")
        html_components.append(f"<meta name=\"description\" content=\"{self.title}\">\n<meta name=\"keywords\" content=\"" + ", ".join(self.tags) + "\">")
        html_components.append(f"<title>{self.title}</title>\n</head>\n<body>\n<h1>{self.title.upper()}</h1>\n<div class=\"kk\">")

        html_components.extend(self.word_index)

        html_components.append("</div>\n</body>")

        return "\n".join(html_components)

    def make_word(self) -> str:
        defeniton_header = list()

        defeniton_header.append(input("Kurila: "))
        defeniton_header.append(input("Romula: "))

        self.tags.extend([defeniton_header[0],defeniton_header[1]])

        defeniton_header.append(input("Irregular Forms: "))

        defeniton_header.append(input("Etymology Data: "))
        
        defenition_tracker = 0
        make_defenitions = True

        word_defentions = list()

        print("Definitions. Eject with " + "!BUN")

        while make_defenitions:
            defenition_tracker += 1

            new_defenition = input(f"{defenition_tracker}) ")
            word_defentions.append(f"{defenition_tracker}) {new_defenition}")

            if  new_defenition == "!BUN":
                word_defentions.pop()
                make_defenitions = False

            elif  new_defenition == "":
                word_defentions.pop()
                defenition_tracker -= 1
        
        final_defenition = list()

        final_defenition.append(f"<table>\n\t<tr><td>{defeniton_header.pop(0)}</td><td>{defeniton_header.pop(0)}</td></tr>")

        if defeniton_header[0] != "":
            final_defenition.append(f"\t<tr><td colspan=\"2\">{defeniton_header.pop(0)}</td></tr>")

        if defeniton_header[-1] != "":
            final_defenition.append(f"\t<tr><td colspan=\"2\">{defeniton_header.pop(-1)}</td></tr>")

        for defenition in word_defentions:
            final_defenition.append(f"\t<tr><td colspan=\"2\">{defenition}</td></tr>")

        final_defenition.append("</table>")

        return "\n".join(final_defenition)

qlb = KK()
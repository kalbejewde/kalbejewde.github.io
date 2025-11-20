class KK:

    wddx = list()
    tags = list()

    def __init__(self):
        self.tags.extend(["Kalba","Калба"])
        self.tags.extend(["English","Anglo","Аҥгло","Aŋglo"])
        self.title = input("Page Title: ")
        self.tags.append(self.title)
        self.dialog()
        input("Press ENTER to Close")

    def dialog(self):
        dlog = True
        while dlog:
            print("0)Compile HTML")
            print("1)Add a word")
            match input("What would you like to do? "):
                case "0":
                    website = self.compile()
                    from os import chdir, path
                    chdir(path.dirname(path.realpath(__file__)))

                    f = open(f"{self.title.lower()}.html", "w", encoding = "utf-8")
                    f.write(website)
                    f.close()
                    dlog = False
                case "1":
                    self.wddx.append(self.dialog_word())

    def compile(self) -> str:
        o = list()
        o.append("<!DOCTYPE html>") #Disable Quirks mode
        o.append(f"<html lang=\"en\">") #Set Language
        o.append("<head>")
        o.append("<link href=\"https://kalbejewde.github.io/kk/kk.css\" rel=\"stylesheet\">")
        o.append(f"<meta name=\"description\" content=\"{self.title}\">")
        o.append("<meta name=\"keywords\" content=\"" + ", ".join(self.tags) + "\">")
        o.append(f"<title>{self.title}</title>")
        o.append("</head>")
        o.append("<body>")
        o.append(f"<h1>{self.title.upper()}</h1>")
        o.append("<div class=\"kk\">")
        o.extend(self.wddx)
        o.append("</div>")
        o.append("</body>")
        return "\n".join(o)


    def dialog_word(self) -> str:
        c = list()
        c.append(input("Kurila: "))
        c.append(input("Romula: "))
        c.append(input("Irregular Forms: "))
        c.append(input("Etymology Data: "))
        
        mdefs = True
        ndef = 0
        cdfs = list()
        print("Definitions. Eject with " + "!BUN")
        while mdefs:
            ndef += 1
            cdc = input(f"{ndef}) ")
            cdfs.append(f"{ndef}) {cdc}")
            if cdc == "!BUN":
                cdfs.pop()
                mdefs = False
            elif cdc == "":
                cdfs.pop()
                ndef -= 1

        #Code to flatten word into single string
        e = list()
        e.append("<table>")
        e.append(f"\t<tr><td>{c[0]}</td><td>{c[1]}</td></tr>")
        if c[2] != "": e.append(f"\t<tr><td colspan=\"2\">{c[2]}</td></tr>")
        if c[3] != "": e.append(f"\t<tr><td colspan=\"2\">{c[3]}</td></tr>")
        for d in cdfs:
            e.append(f"\t<tr><td colspan=\"2\">{d}</td></tr>")
        e.append("</table>")

        self.tags.append(c[0])
        self.tags.append(c[1])

        return "\n".join(e)

qlb = KK()
from fpdf import FPDF


class Shirtificate:
    def __init__(self, name) -> None:
        self.name = name
        self.generate()

    @classmethod
    def get(cls):
        name = input("Name: ").strip()
        return cls(name)

    def generate(self):
        pdf = FPDF()
        pdf.set_auto_page_break(auto=False, margin=0)
        pdf.add_page()
        pdf.set_font("Helvetica", style="B", size=50)
        pdf.cell(
            0,
            50,
            "CS50 Shirtificate",
            border=0,
            align="C",
            new_x="LMARGIN",
            new_y="NEXT",
        )
        pdf.image("shirtificate.png", x=5, y=80, w=200)
        pdf.set_font("Helvetica", style="", size=30)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(
            0, 
            180, 
            f"{self.name} took CS50", align="C"
        )
        pdf.output("shirtificate.pdf")


def main():
    Shirtificate.get()


if __name__ == "__main__":
    main()

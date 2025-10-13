# single responsibility principle


class Report:
    def __init__(self, content: str) -> None:
        self._content: str = content

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    def generate(self) -> None:
        print(f"content: {self.content}")


class ReportSaver:
    def __init__(self, report: Report) -> None:
        self.report: Report = report

    def save_to_file(self, filename: str) -> None:
        with open(filename, mode="w") as file:
            file.write(self.report.content)


if __name__ == "__main__":
    r = Report("dummy content")
    r.generate()

    rs = ReportSaver(r)
    rs.save_to_file("srp_report.txt")

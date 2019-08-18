import re
from pathlib import Path
from typing import List

README_PATH = "../README.md"
PYTHON_HEADER = "### Python\n"
TABLE_HEADER = "| # | Title | Solution | Difficulty | Topic |\n"
TABLE_SEPARATOR = "|---| ----- | -------- | ---------- | ----- |\n"
TABLE_LINE_PATTERN = \
    r"^\| ([0-9]+) \| \[([0-9a-zA-Z\ \-\.]+)\]\((.*)\) \| \[([a-zA-Z]+)\]\(([a-zA-Z0-9\.\/\-]+)\) \| (.*) \| (.*) \|$"


# TABLE_LINE_PATTERN = r"^\| ([0-9]+) (.*)\|$"


# ========== HELPERS START ==========
def _check_prerequisites() -> bool:
    """
    Checks the prerequisites
    :return: True if the prerequisites are met. False otherwise
    """
    if not Path(README_PATH).exists():
        print("README.md does not exist in the root folder")
        return False

    return True


# ========== HELPERS END ==========


class Question:
    """
    Represents a LeetCode question

    ===== Attributes =====
    _path: Path
    _name: str
    _number: int
    _link: Optional[str]
    _difficulty: Optional[str]
    _topic: Optional[List[str]]
    """
    _number: int
    _name: str
    _path: Path
    _language: str
    _link: str
    _difficulty: str
    _topic: List[str]

    def __init__(self, number: int, path: Path, language: str = "Python", link: str = "", difficulty: str = "",
                 topic: List[str] = ""):
        self._number = number
        question_name = "-".join(path.name.split(".")[0].split("-")[1:])
        name = " ".join([w.capitalize() for w in question_name.split("-")])
        self._name = name
        self._path = Path("Python", path.name)
        self._language = language if language else "Python"
        # TODO: link generation
        self._link = link if link else ""
        self._difficulty = difficulty if difficulty else ""
        self._topic = topic if topic else []

    def generate_entry(self) -> str:
        """
        Generates the table entry according to the question

        :return: the generated table entry for the current question
        """
        # TODO: This file path needs to be relative to LeetCode instead of utils.
        table_entry = "| {0} | [{1}]({2}) | [{3}]({4}) | {5} | {6} |\n".format(self._number, self._name, self._link,
                                                                               "Python", self._path, self._difficulty,
                                                                               ", ".join(self._topic))
        return table_entry

    def get_num(self) -> int:
        """
        Returns the number of the question

        :return: the number of the question
        """
        return self._number


class ReadMeFile:
    """
    Represents a readme file

    ===== Attributes =====
    _lines: The lines in the readme file
    _questions = A list of all the questions
    """
    _lines: List[str]
    _questions = List[Question]
    _entry_idx = int

    def __init__(self, lines):
        self._lines = lines
        self._questions = []
        self._entry_idx = 0
        self._initialize()

    def _initialize(self) -> None:
        """ Initializes the instance """
        compiled_pat = re.compile(TABLE_LINE_PATTERN)
        cursor = self._lines.index(PYTHON_HEADER)
        self._entry_idx = cursor = self._lines.index(TABLE_SEPARATOR, cursor) + 1
        while cursor < len(self._lines) and self._lines[cursor].strip():
            line = self._lines[cursor].strip()

            match = re.match(compiled_pat, line)
            if match:
                num, name, link, language, path, difficulty, topic = match.groups()
                num = int(num)
                # Utils is at the same level as python, so we need to add a ..
                path = Path("..", path)
                topic = topic.split(", ")
                question = Question(num, path, language, link, difficulty, topic)
                self._questions.append(question)
            else:
                print("WARNING: this line did not match regex: " + line)
            cursor += 1

        # just in case, we sort the questions list
        self._questions.sort(key=lambda x: x.get_num())

    def insert_question(self, question: Question) -> None:
        """
        Inserts a question into the table of content

        :param question: the question object
        """
        prev_questions = [q for q in self._questions if q.get_num() <= question.get_num()]
        if prev_questions[-1].get_num() == question.get_num():
            question_idx = len(prev_questions) - 1
            self._questions[question_idx] = question
            self._lines[self._entry_idx + question_idx] = question.generate_entry()
        else:
            question_idx = len(prev_questions)
            self._questions.insert(question_idx, question)
            self._lines.insert(self._entry_idx + question_idx, question.generate_entry())

    def get_lines(self) -> List[str]:
        """
        Gets the lines of the README file

        :return: the lines of the readme file
        """
        return self._lines


def _get_current_question_number(file: Path) -> int:
    """
    Gets the current question number given the path of the file

    :param file: the file path
    :return: the question number
    """
    # The file name format: (question_num)-(question name).py
    split_file_name = file.name.split(".")[0].split("-")
    question_no = int(split_file_name[0])
    return question_no


def generate_directory(dir_path: str, readme_file: ReadMeFile) -> bool:
    """
    Inserts a directory of questions into the readme file

    :param dir_path: the target directory path
    :param readme_file: the readme file object
    :return: True if the directory is generated successfully, Galse otherwise
    """
    directory = Path(dir_path)
    for file in directory.iterdir():
        # Note: iterdir does not go in order
        if file.is_file():
            print("===== Processing file [{}]".format(file.name))
            question_num = _get_current_question_number(file)
            question = Question(question_num, file.absolute(), "Python", "", "", [])
            readme_file.insert_question(question)
        elif file.is_dir():
            if not generate_directory(str(file), readme_file):
                print("ERROR: Unable to generate directory: [{}]".format(file.name))
        else:
            print("WARNING: Unknown file path:" + str(file))
    return True


def main() -> None:
    """ The main function """
    print("========= Application Start =========")
    if not _check_prerequisites():
        print("ERROR: Prerequisites are not met.")
        return

    with open(README_PATH, "r") as readme_open:
        readme_file = ReadMeFile(readme_open.readlines())

    if not generate_directory("../Python", readme_file):
        print("ERROR: Was not able to successfully generate directory")

    # insert_directory_to_table("../Python")
    # insert_directory_to_table("../TODOs")
    # insert_question_to_table("../001-two-sum.py")

    with open(README_PATH, "w") as readme_open:
        readme_open.writelines(readme_file.get_lines())

    print("========= Application End =========")


if __name__ == '__main__':
    # ========== PARSER ==========
    # parser = argparse.ArgumentParser(
    #     description='Create a new question entry in the README table contents')
    # parser.add_argument('integers', metavar='N', type=str, nargs='+',
    #                     help='an integer for the accumulator')
    # parser.add_argument('--sum', dest='accumulate', action='store_const',
    #                     const=sum, default=max,
    #                     help='sum the integers (default: find the max)')
    #
    # args = parser.parse_args()
    # print(args.accumulate(args.integers))

    main()

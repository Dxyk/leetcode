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
        # TODO: investigate how to fix the path problem
        self._number = number
        question_name = "-".join(path.name.split(".")[0].split("-")[1:])
        name = " ".join([w.capitalize() for w in question_name.split("-")])
        self._name = name
        self._path = Path("Python", path.name)
        self._language = language if language else "Python"
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
        print("Generated entry: ", table_entry)
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
    # The file name format: (question_num)-(question name).py
    split_file_name = file.name.split(".")[0].split("-")
    question_no = int(split_file_name[0])
    print("Current file number: ", question_no)
    return question_no


def _get_inserting_idx(data: List[str], start: int, end: int, target_question_no: int) -> int:
    # Get all the question numbers
    target_idx = None
    compiled_pat = re.compile(TABLE_LINE_PATTERN)
    table_content = data[start: end]

    if table_content and re.search(compiled_pat, table_content[0].strip()):
        question_nums = [int(re.search(compiled_pat, line.strip()).group(1)) for line in
                         table_content]
        # find the index to insert into
        for idx in range(len(question_nums)):
            if question_nums[idx] >= target_question_no:
                target_idx = idx
                if question_nums[idx] == target_question_no:
                    data.pop(idx)
                break
    target_idx = target_idx if target_idx is not None else len(table_content)
    print("target index: ", target_idx)
    return target_idx


def _generate_line(file_path: str, link: str = None, difficulty: str = None,
                   topic: str = None) -> str:
    # TODO: This file path needs to be relative to LeetCode instead of utils.
    path = Path(file_path)
    split_file_name = path.name.split(".")[0].split("-")
    question_no = str(int(split_file_name[0]))  # str(int()) to remove padded zeros
    question_name = " ".join([word.capitalize() for word in split_file_name[1:]])
    question_name = "[{}]".format(question_name) if link else question_name
    link = "({})".format(link) if link else ""
    difficulty = difficulty if difficulty else ""
    language = "[Python]"
    topic = topic if topic else ""
    readme_line = "| {0} | {1}{2} | {3}({4}) | {5} | {6} |\n".format(question_no, question_name,
                                                                     link, language, file_path,
                                                                     difficulty, topic)
    print("Generated line: ", readme_line)
    return readme_line


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
            question_num = _get_current_question_number(file)
            question = Question(question_num, file.absolute(), "Python", "", "", [])
            readme_file.insert_question(question)
        elif file.is_dir():
            if not generate_directory(str(file), readme_file):
                print("ERROR: Unable to generate directory: [{}]".format(file.name))
        else:
            print("WARNING: Unknown file path:" + str(file))
    return True


def insert_question_to_table(file_path: str, link: str = None, difficulty: str = None,
                             topic: str = None) -> None:
    """
    Insert a question to the readme table of content.
    The table of content should be sorted according to question number in ascending order.

    :param file_path: The file path
    :param link: The LeetCode link to the question
    :param difficulty: The difficulty of the question
    :param topic: The topics for the question
    """
    if not Path(file_path).exists() and not Path(file_path).is_file():
        print("ERROR: The file {0} does not exist!".format(file_path))
        return

    # Read the readme file and extract the table of contents
    readme_file = open(README_PATH, "r+")
    data = readme_file.readlines()
    table_start = data.index("##### Python\n") + 4  # empty line, header, lines
    table_end = data.index("\n", table_start) if "\n" in data[table_start:] else len(data)

    question_no = _get_current_question_number(Path(file_path))

    # Get all the question numbers
    target_idx = _get_inserting_idx(data, table_start, table_end, question_no)
    data.insert(table_start + target_idx, _generate_line(file_path, link, difficulty, topic))
    print(data)

    # TODO: clear file
    readme_file.write("\n\n")
    readme_file.writelines(data)

    readme_file.close()


def main() -> None:
    """ The main function """
    if not _check_prerequisites():
        print("ERROR: Prerequisites are not met.")
        return

    with open(README_PATH, "r") as readme_open:
        readme_file = ReadMeFile(readme_open.readlines())

    if not generate_directory("../Python", readme_file):
        print("ERROR: Was not able to successfully generate directory")

    with open(README_PATH, "w") as readme_open:
        readme_open.writelines(readme_file.get_lines())

    # insert_directory_to_table("../Python")
    # insert_directory_to_table("../TODOs")
    # insert_question_to_table("../001-two-sum.py")


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

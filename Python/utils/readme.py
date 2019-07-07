import re
from pathlib import Path
from typing import List

README_FILE = "../../README.md"
TABLE_LINE_PATTERN = r"^\| ([0-9]+) (.*)\|$"


# def insert_directory_to_table(dir_path: str, data: List[str], start: int, end: int,
#                               target_question_no: int) -> None:
def insert_directory_to_table(dir_path: str) -> None:
    """
    Insert a directory of questions to the content table

    :param dir_path: the path for the directory
    :param data: the array of all the lines in the readme file
    :param start: the starting index of the content table
    :param end: the ending index of the content table
    :param target_question_no: the target question number
    :return:
    """
    # Read the readme file and extract the table of contents
    readme_file = open(README_FILE, "r+")
    data = readme_file.readlines()
    start = data.index("##### Python\n") + 4  # empty line, header, lines

    dir_path = Path(dir_path)

    for file in dir_path.iterdir():
        if file.is_file():
            end = data.index("\n", start) if "\n" in data[start:] else len(data)
            question_no = _get_current_question_number(file)
            target_idx = _get_inserting_idx(data, start, end, question_no)
            # TODO: shouldn't use file here cuz the types don't match
            data.insert(start + target_idx, _generate_line(file))
    # TODO: clear file
    readme_file.write("\n\n")
    readme_file.writelines(data)

    readme_file.close()


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
    readme_file = open(README_FILE, "r+")
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

    # insert_directory_to_table("../.")
    insert_directory_to_table("../TODOs")

    # insert_question_to_table("../001-two-sum.py")

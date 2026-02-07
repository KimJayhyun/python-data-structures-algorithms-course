class FileNode:
    def __init__(self, name, size):
        self.name = name
        self.size = size  # 파일 크기 (KB)
        self.is_file = True


class DirectoryNode:
    def __init__(self, name):
        self.name = name
        self.is_file = False
        self.children = []  # 파일들과 하위 폴더들

    def add_child(self, child):
        self.children.append(child)


# 예시 트리 만들기
def create_example():
    root = DirectoryNode("project")
    root.add_child(FileNode("main.py", 100))
    root.add_child(FileNode("utils.py", 50))

    data_folder = DirectoryNode("data")
    data_folder.add_child(FileNode("input.txt", 200))

    archive = DirectoryNode("archive")
    archive.add_child(FileNode("old.txt", 150))
    data_folder.add_child(archive)

    root.add_child(data_folder)
    return root


# 여기에 함수 작성!
def calculate_total_size(node: DirectoryNode | FileNode):
    if isinstance(node, FileNode):
        return node.size

    result = 0
    for child in node.children:
        result += calculate_total_size(child)

    return result


def _find_file(node: DirectoryNode | FileNode, file_name, full_path: list):
    if node.is_file:
        if node.name == file_name:
            full_path.append(node.name)
            return True
        else:
            return False

    full_path.append(node.name)

    for child in node.children:
        sub_path = _find_file(child, file_name, full_path)
        if sub_path:
            return True

    full_path.pop()

    return False


def find_file(node, file_name):
    full_path = []

    _find_file(node, file_name, full_path)

    if full_path:
        return "/" + "/".join(full_path)
    else:
        return "없어용"


root = create_example()

print(calculate_total_size(root))  # 500 (100+50+200+150)
print(find_file(root, "old.txt"))

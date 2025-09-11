from typing import List, Dict


class TrieNode:

    def __init__(self, value):
        self.value: str = value
        self.next: Dict[str, TrieNode] = dict()
        self.is_folder = False
        self.full_path = ''


    def __repr__(self) -> str:
        return f'\'{self.value}\' ({self.is_folder}; \'{self.full_path}\') -> {self.next.keys()}'



class RemoveSubFoldersFromTheFilesystem:
    """
    Leetcode #1233
    Link: https://leetcode.com/problems/remove-sub-folders-from-the-filesystem
    """

    def remove_subfolders(self, folders: List[str]) -> List[str]:
        """
        >>> sut = RemoveSubFoldersFromTheFilesystem()
        >>> actual = sut.remove_subfolders(['/a', '/a/b', '/c/d', '/c/d/e', '/c/f'])
        >>> expected = ['/a', '/c/d', '/c/f']
        >>> assert sorted(actual) == sorted(expected), f'expected {sorted(expected)}; got {sorted(actual)}'
        >>> actual = sut.remove_subfolders(['/a', '/a/b/c', '/a/b/d'])
        >>> expected = ['/a']
        >>> assert sorted(actual) == sorted(expected), f'expected {sorted(expected)}; got {sorted(actual)}'
        >>> actual = sut.remove_subfolders(['/a/b/c', '/a/b/ca', '/a/b/d'])
        >>> expected = ['/a/b/c', '/a/b/ca', '/a/b/d']
        >>> assert sorted(actual) == sorted(expected), f'expected {sorted(expected)}; got {sorted(actual)}'
        """
        root = TrieNode('')
        for folder in folders:
            path: List[str] = folder[1:].split('/')
            r = root
            for i, p in enumerate(path):
                if p not in r.next:
                    r.next[p] = TrieNode(p)
                r = r.next[p]
                if i == len(path) - 1:
                    r.is_folder = True
                    r.full_path = folder

        result: List[str] = list()

        bfs: List[TrieNode] = list()
        bfs.append(root)

        while bfs:
            c = bfs.pop()
            if c.is_folder:
                result.append(c.full_path)
            else:
                bfs += c.next.values()

        return result


    def remove_subfolders_opt(self, folder: List[str]) -> List[str]:
        """
        >>> sut = RemoveSubFoldersFromTheFilesystem()
        >>> actual = sut.remove_subfolders_opt(['/a', '/a/b', '/c/d', '/c/d/e', '/c/f'])
        >>> expected = ['/a', '/c/d', '/c/f']
        >>> assert sorted(actual) == sorted(expected), f'expected {sorted(expected)}; got {sorted(actual)}'
        >>> actual = sut.remove_subfolders_opt(['/a', '/a/b/c', '/a/b/d'])
        >>> expected = ['/a']
        >>> assert sorted(actual) == sorted(expected), f'expected {sorted(expected)}; got {sorted(actual)}'
        >>> actual = sut.remove_subfolders_opt(['/a/b/c', '/a/b/ca', '/a/b/d'])
        >>> expected = ['/a/b/c', '/a/b/ca', '/a/b/d']
        >>> assert sorted(actual) == sorted(expected), f'expected {sorted(expected)}; got {sorted(actual)}'
        """
        folder.sort()
        res = []
        for path in folder:
            if not res or not path.startswith(res[-1] + '/'):
                res.append(path)
        return res


if __name__ == '__main__':
    import doctest

    doctest.testmod()

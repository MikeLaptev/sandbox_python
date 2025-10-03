class CompareVersionNumbers:

    def compare_version(self, version1: str, version2: str) -> int:
        """
        >>> sut = CompareVersionNumbers()
        >>> v1 = "1.2"
        >>> v2 = "1.10"
        >>> expected = -1
        >>> actual = sut.compare_version(version1=v1, version2=v2)
        >>> assert expected == actual, f"expected {expected}; got {actual}; compared v1 - [{v1}] with v2 - [{v2}]"
        >>> v1 = "1.01"
        >>> v2 = "1.001"
        >>> expected = 0
        >>> actual = sut.compare_version(version1=v1, version2=v2)
        >>> assert expected == actual, f"expected {expected}; got {actual}; compared v1 - [{v1}] with v2 - [{v2}]"
        >>> v1 = "1.0.1"
        >>> v2 = "1.0.0.0"
        >>> expected = 1
        >>> actual = sut.compare_version(version1=v1, version2=v2)
        >>> assert expected == actual, f"expected {expected}; got {actual}; compared v1 - [{v1}] with v2 - [{v2}]"
        >>> v1 = "1.0.0"
        >>> v2 = "1.0.0.0"
        >>> expected = 0
        >>> actual = sut.compare_version(version1=v1, version2=v2)
        >>> assert expected == actual, f"expected {expected}; got {actual}; compared v1 - [{v1}] with v2 - [{v2}]"
        """
        v1_parts = version1.split(".")
        v2_parts = version2.split(".")
        for i in range(max(len(v1_parts), len(v2_parts))):
            r = self.compare(
                v1_parts[i] if i < len(v1_parts) else "0",
                v2_parts[i] if i < len(v2_parts) else "0",
            )
            if r != 0:
                return r

        return 0

    def compare(self, v1_part: str, v2_part: str) -> int:
        v1_part = v1_part.lstrip("0")
        v2_part = v2_part.lstrip("0")
        if v1_part == v2_part:
            return 0
        return (
            1 if int(v1_part if v1_part else 0) > int(v2_part if v2_part else 0) else -1
        )


if __name__ == "__main__":
    import doctest

    doctest.testmod()

from functools import total_ordering

@total_ordering
class Version:
    def __init__(self, version):
        self._version = version.split('.')
        while len(self._version) < 3:
            self._version.append('0')
        self._ver = int(self._version[0]) * 100000 + int(self._version[1]) * 1000 + int(self._version[2])

    def __str__(self):
        return f"{'.'.join(self._version)}"

    def __repr__(self):
        return f"Version('{'.'.join(self._version)}')"

    def __eq__(self, other):
        if isinstance(other, Version):
            return self._ver == other._ver
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Version):
            return self._ver < other._ver
        return NotImplemented


print(Version('3.0.3') == Version('1.11.28'))
print(Version('3.0.0') < Version('3.11.28'))
print(Version('3.1.3') > Version('3.0.999'))
print(Version('3.0.3') <= Version('1.11.28'))
print(Version('3.0.3') >= Version('1.11.28'))

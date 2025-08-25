import typing
T = typing.TypeVar('T')


class Accumulator(typing.Generic[T]):
    def __init__(self):
        self._contents: list[T] = []

    def update(self, *args: T) -> None:
        self._contents.extend(args)

    def undo(self) -> None:
        if self._contents:
            self._contents.pop()

    def __len__(self) -> int:
        return len(self._contents)

    def __iter__(self) -> typing.Iterator[T]:
        return iter(self._contents)


@typing.runtime_checkable
class SupportsUpdateUndo(typing.Protocol):
    def update(self, *args: T) -> None:
        ...

    def unsdo(self) -> None:
        ...


acc: Accumulator[int] = Accumulator()
acc.update(1,2,3)
print(sum(acc))
acc.undo()
print(sum(acc))

acc: Accumulator[str] = Accumulator()
acc.update('hello', 'world')
print(' '.join(acc))
acc.undo()
print(' '.join(acc))

isinstance(acc, SupportsUpdateUndo)
issubclass(Accumulator, SupportsUpdateUndo)

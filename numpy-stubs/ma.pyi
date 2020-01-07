from numpy import ndarray, _DType, bool_
from typing import Generic

class MaskedArray(ndarray[_DType]): ...

def array(data: ndarray[_DType], mask: ndarray[bool_] = ...) -> MaskedArray[_DType]: ...
def dot(a: MaskedArray[_DType], b: MaskedArray[_DType]) -> MaskedArray[_DType]: ...
def masked_array(data: ndarray[_DType], mask: ndarray[_DType]) -> MaskedArray[_DType]: ...
def median(data: MaskedArray[_DType]) -> _DType: ...
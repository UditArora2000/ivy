# global
import mxnet as mx

# local
from ivy.functional.backends.mxnet import _handle_flat_arrays_in_out


@_handle_flat_arrays_in_out
def isfinite(x: mx.ndarray.ndarray.NDArray)\
        -> mx.ndarray.ndarray.NDArray:
    # ToDo: remove float32 conversion once int8 and uint8 work correctly. Currently 0 returns 0 for these types.
    return mx.nd.contrib.isfinite(x.astype('float32')).astype('bool')


@_handle_flat_arrays_in_out
def logical_not(x: mx.ndarray.ndarray.NDArray)\
        -> mx.ndarray.ndarray.NDArray:
    return mx.nd.logical_not(x)

# @_handle_flat_arrays_in_out
# def negative(x: mx.ndarray.ndarray.NDArray)\
#         -> : mx.ndarray.ndarray.NDArray:
#     return mx.np.negative(x)

from pyroaring import BitMap
from modules.MD5Util import MD5Util
import base64


class RoaringBitmapUtil:
    @staticmethod
    def from_byte_array(byte_array):
        # Create a new RoaringBitmap instance and deserialize from the byte array
        roaring_bitmap = BitMap.deserialize(byte_array)
        return roaring_bitmap

    @staticmethod
    def from_base64(base64_string):
        return RoaringBitmapUtil.from_byte_array(base64.b64decode(base64_string))

    @staticmethod
    def to_string_array(bitmap):
        # Convert RoaringBitmap to an array of strings
        return [MD5Util.to_string(i) for i in bitmap]

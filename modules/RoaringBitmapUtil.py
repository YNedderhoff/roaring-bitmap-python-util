from pyroaring import BitMap

from modules.MD5Util import MD5Util


class RoaringBitmapUtil:

    @staticmethod
    def to_byte_array(bitmap):
        # Serialize the RoaringBitmap and return the byte array
        return bitmap.serialize()

    @staticmethod
    def from_byte_array(byte_array):
        # Create a new RoaringBitmap instance and deserialize from the byte array
        roaring_bitmap = BitMap.deserialize(byte_array)
        return roaring_bitmap

    @staticmethod
    def to_string_array(bitmap):
        # Convert RoaringBitmap to an array of strings
        return [MD5Util.to_string(i) for i in bitmap]
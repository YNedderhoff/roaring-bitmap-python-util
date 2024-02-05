from modules.RoaringBitmapUtil import RoaringBitmapUtil

# below are two byte array representations of RoaringBitmaps

# the byte array representation of a RoaringBitmap containing id '938c'
SERIALISED_BITMAP_1 = bytes([58, 48, 0, 0, 1, 0, 0, 0, 51, 57, 0, 0, 16, 0, 0, 0, 99, 56])
# the byte array representation of a RoaringBitmap containing ids '938c' and '3f7e'
SERIALISED_BITMAP_2 = bytes([58, 48, 0, 0, 2, 0, 0, 0, 102, 51, 0, 0, 51, 57, 0, 0, 24, 0, 0, 0, 26, 0, 0, 0, 101, 55, 99, 56])


def run():
    # deserialise both byte arrays to BitMap objects
    roaring_bitmap_1 = RoaringBitmapUtil.from_byte_array(SERIALISED_BITMAP_1)
    roaring_bitmap_2 = RoaringBitmapUtil.from_byte_array(SERIALISED_BITMAP_2)

    # bitwise AND
    intersected_bitmap = roaring_bitmap_1 & roaring_bitmap_2

    # Convert to string arrays
    string_array_1 = RoaringBitmapUtil.to_string_array(roaring_bitmap_1)
    string_array_2 = RoaringBitmapUtil.to_string_array(roaring_bitmap_2)
    intersected_string_array = RoaringBitmapUtil.to_string_array(intersected_bitmap)

    print("Deserialised ids from bitmap 1:\t" + str(string_array_1))  # ['938c']
    print("Deserialised ids from bitmap 2:\t" + str(string_array_2))  # ['3f7e', '938c']
    print("")
    print("bitwise AND on the above:\t\t" + str(intersected_string_array))  # ['938c']


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

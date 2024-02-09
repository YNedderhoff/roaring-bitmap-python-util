import struct


class MD5Util:
    @staticmethod
    def to_byte_array(first_four_bytes_of_md5):
        return struct.pack('>I', first_four_bytes_of_md5)

    @staticmethod
    def to_string(first_four_bytes_of_md5):
        return MD5Util.to_byte_array(first_four_bytes_of_md5).decode('utf-8')

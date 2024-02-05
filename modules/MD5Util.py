import struct


class MD5Util:
    MD5_BYTES = 16

    @staticmethod
    def truncate_to_four_bytes(md5_bytes):
        if len(md5_bytes) != MD5Util.MD5_BYTES:
            raise ValueError("The byte array must represent an MD5 hash, so it must be 16 bytes long")
        return md5_bytes[:4]

    @staticmethod
    def to_int(md5_bytes_truncated):
        if len(md5_bytes_truncated) != 4:
            raise ValueError(
                "The byte array must represent the first four bytes of an MD5 hash, so it must be 4 bytes long")
        return struct.unpack('>I', md5_bytes_truncated)[0]

    @staticmethod
    def to_byte_array(first_four_bytes_of_md5):
        return struct.pack('>I', first_four_bytes_of_md5)

    @staticmethod
    def to_string(first_four_bytes_of_md5):
        return MD5Util.to_byte_array(first_four_bytes_of_md5).decode('utf-8')

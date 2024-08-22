#!/usr/bin/python3
def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list of int): A list of integers representing bytes of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    n_bytes = 0

    # Masks to check the two most significant bits in a byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # Mask to check the significant 8 bits in the integer
        byte = num & 0xFF

        if n_bytes == 0:
            # Count the number of leading 1s in the first byte
            mask = 1 << 7
            while mask & byte:
                n_bytes += 1
                mask >>= 1

            if n_bytes == 0:
                continue

            # If n_bytes is more than 4 or less than 2, it's invalid
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # If the byte doesn't start with '10', it's invalid
            if not (byte & mask1 and not (byte & mask2)):
                return False

        n_bytes -= 1

    # Return True if all bytes are validated, otherwise False
    return n_bytes == 0

#!/usr/bin/python3
def validUTF8(data):
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

            # If n_bytes is more than 4 or less than 2 (invalid UTF-8)
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # If the byte doesn't start with '10', it's invalid
            if not (byte & mask1 and not (byte & mask2)):
                return False

        n_bytes -= 1

    # If n_bytes is not zero, it means there were bytes missing at the end
    return n_bytes == 0

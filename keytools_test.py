from typing import List
import unittest
import keytools
import unittest.mock


class NotRandom():
    iteration: int = 0

    def linear(self, size: int) -> bytes:
        output: List[bytes] = []
        for i in range(size):
            output.append(self.iteration.to_bytes(1, 'big'))
            self.iteration += 1
        return b''.join(output)

    def big_then_small(self, size: int) -> bytes:
        output: List[bytes] = []
        for i in range(size):
            if self.iteration < keytools.key_chunk_size:
                output.append(bytes.fromhex("ff"))
            else:
                output.append(bytes.fromhex("00"))

            self.iteration += 1
        return b''.join(output)


class TestKeygen(unittest.TestCase):
    def test_generate_key(self) -> None:
        generator = NotRandom()
        with unittest.mock.patch("os.urandom", generator.linear):
            key = keytools.generate_key(5)

            self.assertEqual(
                key.hex(),
                "000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2021222324"
                + "25262728292a2b2c2d2e2f303132333435363738393a3b3c3d3e3f40414243444546474849"
                + "4a4b4c4d4e4f505152535455565758595a5b5c5d5e5f606162636465666768696a6b6c6d6e"
                + "6f707172737475767778797a7b7c7d7e7f808182838485868788898a8b8c8d8e8f90919293"
                + "9495969798999a9b9c9d9e9fa0a1a2a3a4a5a6a7a8a9aaabacadaeafb0b1b2b3b4b5b6b7b8"
            )

    def test_invalid_first_generated_keychunk(self) -> None:
        generator = NotRandom()
        with unittest.mock.patch("os.urandom", generator.big_then_small):
            key = keytools.generate_key(2)

            self.assertEqual(
                key.hex(),
                "00000000000000000000000000000000000000000000000000000000000000000000000000"
                + "00000000000000000000000000000000000000000000000000000000000000000000000000"
            )

    def test_out_of_bounds_index(self) -> None:
        with self.assertRaises(ValueError):
            keytools._permutation_from_index(3, 6)

    def test_invalid_key_size(self) -> None:
        with self.assertRaises(ValueError):
            keytools.convert_key_to_character_lists(b'not37byteslong')

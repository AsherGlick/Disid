from typing import Final, List
import unittest
import disid
import keytools

shift_cipher_5_key: Final[List[str]] = keytools.convert_key_to_character_lists(
    bytes.fromhex(
        "fcd4af68bde6b2f73910443fb6d1a75bbaea6a2dd4f08c360d37bd1ec5c497cf78b35dede4"
        + "319cb4119917d8e5f51c3c01478a3989071059f96229c0a41ebdb9430b40819c9090c5fbf3"
        + "6b1fe5e4271a5835d7437c6d028f5ac3ad7b0a7d9d2d6ccb8bbcc3da4a94fe8f24b0da46c6"
        + "3a66266834fa3f482ea50d6e6089e5b2b1781131e251ac0e0bc6da39ab3cbd62b269f596c0"
        + "02eaadf2257d4007952dc0d02efef91ae62f32e4d1912a7e71b0157948613ee24222e538dc"
    )
)

shift_cipher_7_key: Final[List[str]] = keytools.convert_key_to_character_lists(
    bytes.fromhex(
        "40fcc61e5bc570210a33499623e03ff799ecaf5a4ece761ef8da9a5f48d5ca7b2080039079"
        + "6c64e8e9d9e700d2cbea4be8497ec470e015fe68c1e0187e1fd177f9ac977866715305a724"
        + "1675695bc26bab021fff8db76377be716e2b1684d272ace95ff5e9200a665f4d5b32a02c34"
        + "70fc747d9cf3fb50675371e05fc9cbb370b3984832f3f2c1560ddd804f20a69f753428066b"
        + "163690bcabda08a24b269feb26e83fbde033cdfaa825ac508231e330d4ee20dde574f755a6"
        + "fed437c5354290bd9a95d225779b260b9deddb87f6d0a0962ea427a10f25f9e6058f693046"
        + "93b17e9e06fbd75b7f168ac43f25018deba16610173994d65ae194ea1ba4293a5b1962f4e3"
    )
)

range_100: Final[List[int]] = [i for i in range(100)]
range_12: Final[List[int]] = [i for i in range(12)]


class TestV3Generator(unittest.TestCase):
    def test_default_length(self) -> None:
        ids = [disid.uint_to_id_v3(i, shift_cipher_5_key) for i in range_100]

        self.assertListEqual(
            ids,
            [
                '-d2t_', 'aBbf2', 'gmIbQ', 'sbh-w', 'kj0cg', '4fYqJ', 'T_oTL',
                'GIUvB', 'wLW8e', 'AOz2E', 'zod_l', 'UDg9r', 'Een3F', 'Xnt1R',
                'FsFmG', 'PxxSi', 'HKqK_', 'tG7Z2', 'Qh8oQ', '3vLlw', 'y4A4g',
                'CqiVJ', 'WXfeL', 'r6DHB', '5Vu5e', 'D5MLE', 'iT6Pl', 'c2ZYr',
                'vSJMF', 'BwmJR', 'OYkkG', '_Q3Ui', '0W2w_', 'I3bB2', 'h-IxQ',
                'YrhQw', 'eR0zg', 'ZlYaJ', 'q0o0L', 'fzUEB', 'puWIe', 'VpzpE',
                '8CdFl', 'bFgrr', 'RAniF', '6NtWR', '2aFDG', 'mPxAi', 'N9qg_',
                'xi7C2', '978jQ', 'uJLRw', 'JUA6g', 'lHihJ', 'M8fGL', '7yDXB',
                'ncuye', 'S1MdE', 'Lk6ul', 'otZnr', '1EJNF', 'dgmsR', 'KZkOG',
                'jM37i', '-BGek', 'ameH-', 'gby5h', 'sjOLT', 'kfwPq', '4_TY1',
                'TI_MN', 'GLEJn', 'wOlk9', 'Ao9U3', 'zDSwX', 'UeKB0', 'EnjxO',
                'XsBQv', 'FxszU', 'PKNaj', 'HG-0k', 'thcE-', 'Qv4Ih', '34HpT',
                'yqpFq', 'CX1r1', 'W6ViN', 'rVPWn', '55CD9', 'DTXA3', 'i2vgX',
                'cSRC0', 'vwrjO', 'BYQRv', 'OQa6U', '_W5hj', '03GGk', 'I-eX-',
                'hryyh', 'YROdT'
            ]
        )

        numbers = [disid.id_v3_to_uint(i, shift_cipher_5_key) for i in ids]

        self.assertListEqual(
            numbers,
            range_100
        )

    def test_length_seven(self) -> None:
        ids = [disid.uint_to_id_v3(i, shift_cipher_7_key) for i in range_12]

        self.assertListEqual(
            ids,
            [
                'QLzmJB1', 'U9mwdTC', 'Ay2OYiV', 'KWE04wk', 't4kvheQ', 'FUGKrq4',
                'jxDxXSp', 'gBhCkYt', '7PWnuje', 'YQ3AN_y', '6csqQ62', 'ZIOz8mZ'
            ]
        )

        numbers = [disid.id_v3_to_uint(i, shift_cipher_7_key) for i in ids]

        self.assertListEqual(
            numbers,
            range_12
        )


class TestV2Generator(unittest.TestCase):
    def test_default_length(self) -> None:
        ids = [disid.uint_to_id_v2(i, shift_cipher_5_key) for i in range(100)]

        self.assertListEqual(
            ids,
            [
                '-d5Fm', 'aBGeu', 'gmebt', 'sbyDx', 'kjOP6', '4fwT8', 'T_TjP',
                'GI_kA', 'wLE_m', 'AOlGu', 'zo9xt', 'UDSmx', 'EeKu6', 'Xnj08',
                'FsBoP', 'PxsOA', 'HKNFm', 'tG-eu', 'Qhcbt', '3v4Dx', 'y4HP6',
                'CqpT8', 'WX1jP', 'r6VkA', '5VP_m', 'D5CGu', 'iTXxt', 'c2vmx',
                'vSRu6', 'Bwr08', 'OYQoP', '_QaOA', '0W5Fm', 'I3Geu', 'h-ebt',
                'YryDx', 'eROP6', 'ZlwT8', 'q0TjP', 'fz_kA', 'puE_m', 'VplGu',
                '8C9xt', 'bFSmx', 'RAKu6', '6Nj08', '2aBoP', 'mPsOA', 'N9NFm',
                'xi-eu', '97cbt', 'uJ4Dx', 'JUHP6', 'lHpT8', 'M81jP', '7yVkA',
                'ncP_m', 'S1CGu', 'LkXxt', 'otvmx', '1ERu6', 'dgr08', 'KZQoP',
                'jMaOA', '-B2tI', 'ambiC', 'gbI5c', 'sjhcK', 'kf0g4', '4_YMa',
                'TIo8V', 'GLU6Z', 'wOWwI', 'Aoz3C', 'zDdyc', 'UegzK', 'EnnK4',
                'XstNa', 'FxFIV', 'PKx4Z', 'HGqtI', 'th7iC', 'Qv85c', '34LcK',
                'yqAg4', 'CXiMa', 'W6f8V', 'rVD6Z', '55uwI', 'DTM3C', 'i26yc',
                'cSZzK', 'vwJK4', 'BYmNa', 'OQkIV', '_W34Z', '032tI', 'I-biC',
                'hrI5c', 'YRhcK'
            ]
        )

        numbers = [disid.id_v2_to_uint(i, shift_cipher_5_key) for i in ids]

        self.assertListEqual(
            numbers,
            range_100
        )

    def test_length_seven(self) -> None:
        ids = [disid.uint_to_id_v2(i, shift_cipher_7_key) for i in range_12]

        self.assertListEqual(
            ids,
            [
                'QL6YxDM', 'U9BMebl', 'AyjOjvM', 'KW1-v-l', 't49TADM', 'FUHx_bl',
                'jxxWfvM', 'gB-uF-l', '7PLqxDM', 'YQeSebl', '6cb1jvM', 'ZIPBv-l'
            ]
        )

        numbers = [disid.id_v2_to_uint(i, shift_cipher_7_key) for i in ids]

        self.assertListEqual(
            numbers,
            range_12
        )


class TestV1Generator(unittest.TestCase):
    def test_default_length(self) -> None:
        ids = [disid.uint_to_id_v1(i, shift_cipher_5_key) for i in range(100)]

        self.assertListEqual(
            ids,
            [
                '-MaOA', 'ad3pv', 'gB54G', 'sm27y', 'kbGFZ', '4jbVU', 'Tfeti',
                'G_Irp', 'wIyem', 'ALhfj', 'zOOi_', 'Uo0HS', 'EDwbI', 'XeYWk',
                'FnT52', 'Pso-z', 'Hx_Du', 'tKUL-', 'QGEcQ', '3hWAo', 'yvlPC',
                'C4zqh', 'Wq9gw', 'rXdYY', '56STt', 'DVgCT', 'i5KMg', 'cTnvM',
                'v2jjc', 'BStJq', 'OwB8J', '_YFRW', '0Qskx', 'IWx21', 'h3N6L',
                'Y-qUb', 'er-_K', 'ZR7hN', 'qlcwB', 'f089H', 'pz4G6', 'VuLBn',
                '8pH3e', 'bCAX7', 'RFpx4', '6Ai19', '2N1yE', 'mafQD', 'NPVm8',
                'x9Dd3', '9iPzl', 'u7uSd', 'JJCua', 'lUMaX', 'MHXKr', '786ns',
                'nyv0P', 'ScZZ0', 'L1RNF', 'okJE5', '1troV', 'dEmsO', 'KgQIR',
                'jZklf', '-d3pv', 'aB54G', 'gm27y', 'sbGFZ', 'kjbVU', '4feti',
                'T_Irp', 'GIyem', 'wLhfj', 'AOOi_', 'zo0HS', 'UDwbI', 'EeYWk',
                'XnT52', 'Fso-z', 'Px_Du', 'HKUL-', 'tGEcQ', 'QhWAo', '3vlPC',
                'y4zqh', 'Cq9gw', 'WXdYY', 'r6STt', '5VgCT', 'D5KMg', 'iTnvM',
                'c2jjc', 'vStJq', 'BwB8J', 'OYFRW', '_Qskx', '0Wx21', 'I3N6L',
                'h-qUb', 'Yr-_K'
            ]
        )

        numbers = [disid.id_v1_to_uint(i, shift_cipher_5_key) for i in ids]

        self.assertListEqual(
            numbers,
            range_100
        )

    def test_length_seven(self) -> None:
        ids = [disid.uint_to_id_v1(i, shift_cipher_7_key) for i in range_12]

        self.assertListEqual(
            ids,
            [
                'QbFcF-l', 'ULoVl6D', 'A96iCFA', 'Kyz_Sf0', 'tWBYmJc', 'F4mgTxe',
                'jUjmwmP', 'gx2L1pN', '7B1Mx9T', 'YPEwV7J', '6Q94Jzz', 'ZckU9ay'
            ]
        )

        numbers = [disid.id_v1_to_uint(i, shift_cipher_7_key) for i in ids]

        self.assertListEqual(
            numbers,
            range_12
        )


class TestPadZeros(unittest.TestCase):
    def test_default_length_one_elem(self) -> None:
        self.assertEqual(
            disid.pad_zeros([7]),
            [7, 0, 0, 0, 0]
        )

    def test_default_length_two_elem(self) -> None:
        self.assertEqual(
            disid.pad_zeros([2, 9]),
            [2, 9, 0, 0, 0]
        )

    def test_default_length_five_elem(self) -> None:
        self.assertEqual(
            disid.pad_zeros([2, 9, 8, 1, 4]),
            [2, 9, 8, 1, 4]
        )

    def test_default_length_six_elem(self) -> None:
        self.assertEqual(
            disid.pad_zeros([2, 9, 8, 1, 4, 7]),
            [2, 9, 8, 1, 4, 7]
        )

    def test_custom_length(self) -> None:
        self.assertEqual(
            disid.pad_zeros([5], 7),
            [5, 0, 0, 0, 0, 0, 0]
        )


class TestUintToBase64(unittest.TestCase):
    def test_positive_integer(self) -> None:
        self.assertEqual(
            disid.uint_to_base64(123456789),
            [21, 52, 60, 22, 7]
        )

    def test_negative_integer(self) -> None:
        with self.assertRaises(ValueError):
            disid.uint_to_base64(-1)

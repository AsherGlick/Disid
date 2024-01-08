from typing import List
from .disid import uint_to_id_v3, id_v3_to_uint


################################################################################
# Disid3
#
# A helper class to allow for easier handling of encoding/decoding disid values.
################################################################################
class Disid3():
	digit_order: List[str]

	def __init__(self, digit_order: List[str]):
		self.digit_order = digit_order

	def encode(integer: int) -> str:
		return uint_to_id_v3(integer, self.digit_order)

	def decode(token: str) -> int:
		return id_v3_to_uint(token, self.digit_order)

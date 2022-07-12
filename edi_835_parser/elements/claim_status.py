from edi_835_parser.elements import Element


class ClaimStatus(Element):

	# todo: https://x12.org/codes/claim-status-codes

	def parser(self, value: str) -> int:
		if value == '':
		    return 0

		return int(value)

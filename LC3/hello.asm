.ORIG x3000

LD R0, HELLO_LOC

TRAP x22
TRAP x23
TRAP x25

HELLO_LOC .FILL HELLO_STR
HELLO_STR	.STRINGZ "HELLO WORLD"

.END

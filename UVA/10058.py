import re

VERB = '(hate|love|know|like)s?'
NOUN = '(tom|jerry|goofy|mickey|jimmy|dog|cat|mouse)'
ARTICLE = '(a|the)'
ACTOR = '({0}|{1} *{0})'.format(NOUN, ARTICLE)
ACTIVE_LIST = '({0} *and *)*{0}'.format(ACTOR)
ACTION = '({0} {1} {0})'.format(ACTIVE_LIST, VERB)
STATEMENT = '^ *{0}( *, *{0})* *$'.format(ACTION)

test = re.compile(STATEMENT)

while True:
	try:
		print(['NO I WON\'T', 'YES I WILL'][bool(test.match(input()))])
	except EOFError:
		break
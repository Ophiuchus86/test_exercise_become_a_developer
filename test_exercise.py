from collections import Counter

def foo(text):
	def get_first_unique_char(word):
		for char, count in Counter(word).items():
			if count == 1:
				return char

	words = text.split(" ")
	result1 = []

	for word in words:
		result1.append(get_first_unique_char(word))

	return get_first_unique_char(result1)


if __name__ == '__main__':
	text = input("Enter text: ")
	print(f"Result: {foo(text)}")

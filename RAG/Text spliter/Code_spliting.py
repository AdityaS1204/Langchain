from langchain.text_splitter import RecursiveCharacterTextSplitter,Language

code = '''
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b


calc = Calculator()
print("Add: ", calc.add(5, 3))

'''

spliter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=200,
    chunk_overlap=0
)

result = spliter.split_text(code)

print(len(result))
print(result)
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='Resources',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.load()
# docs = loader.lazy_load() lazy_load() it returns a generator of document object, loads on demand best when huge number of pdfs,txt,docx is to be loaded.  

print(len(docs))
for document in docs:
    print(document.metadata)

    # print(docs[1].page_content)
    # print(docs[0].metadata)

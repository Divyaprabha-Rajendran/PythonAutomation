import PyPDF2

pdf_file = open('D:\MyFolder\My books\magoosh-gre-1000-words.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
print (number_of_pages)
word=[]
meaning=[]
for x in range(number_of_pages):
    page = read_pdf.getPage(x)
    page_content = page.extractText()
    data = page_content

    data = data.replace('\n', '')
    stripped_data = data.replace('gre.magoosh.com/flashcards', '')
    stripped_data = stripped_data.replace('Common (High-frequency) Words', '')
    stripped_data = stripped_data.replace('This word has other definitions but this is the most important one for the GRE','')

    # print (stripped_data)

    split_data = stripped_data.split(".")
    print(len(split_data))
    # print (split_data)
    for x in split_data:
        curr_str = x
        if (len(x.split(":")) > 1):
            word_str = x.split(":")
            print(word_str[0] + "\t" + word_str[1])
            word.append(word_str[0])
            meaning.append(word_str[1])
#print (len(word))
#print (len(meaning))
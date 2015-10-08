import re


def articles_description():
    text = []
    f1 = open('article_description.scv', 'w', encoding='utf-8')
    f1.write('Название статьи;Кол-во ссылок из статьи;Кол-во словоформ в статье\r\n')
    f = open('udmwiki-20150901-pages-articles-multistream.xml', 'r', encoding='utf-8')
    for line in f:
        text.append(line)
    for l in range(0,len(text)):
            if "'''" in text[l][0:4]:
                stri = 0
                ref = 0
                r = re.findall("^'''(.*?)'''", text[l])
                for i in r:
                    f1.write(i)
                while '</text>' not in text[l]:
                    r = re.findall("\[\[", text[l])
                    ref += len(r)
                    stri += len(text[l])
                    l += 1
                else:
                    f1.write(';'+str(ref)+';'+str(stri)+'\r\n')

    f1.close()

articles_description()
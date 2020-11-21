import web
urls = (
'/', 'Index'
)

app = web.application(urls, globals())
render = web.template.render('templates/')

class Index(object):
    def GET(self):
        return render.form()

    def POST(self):
        form = web.input(name="test.txt")
        txt = open(form.name)
        readOne = txt.readline()
        readAll = txt.readlines()

        data = []
        sortedData = []
        allData = []
        finalData = []
        split_list = []
        for i in readAll:
            splitLine = i.split()
            data.append(splitLine[1] + " " + i)

        for line in sorted(data):
            line.split(' ', 1)
            sortedSplitLine = line.split(' ', 1)[1]
            sortedData.append(sortedSplitLine)

        for i in sortedData:
            finalSplit = i.split()
            allData.append(finalSplit)

        for i in allData:
            if i[0]:
                finalData.append(i[0])
                del i[0]
            if i[-1]:
                finalData.append(i[-2])
                del i[-2]
            if i[-2]:
                finalData.append(i[-1])
                del i[-1]

        pos = 1
        for i in allData:
            listToStr = ' '.join([str(elem) for elem in i])
            finalData.insert(pos, listToStr)
            pos = pos + 4


        length = int(((len(finalData)) - 4) / 4)
        index = 4
        for i in range(0, length):
            if i < length:
                split_list.append(index)
                index = index + 4


        allInfo = [finalData[i: j] for i, j in zip([0] + split_list, split_list + [None])]

        txt.close()

        return render.index(allInfo = allInfo)

if __name__ == "__main__":
    app.run()

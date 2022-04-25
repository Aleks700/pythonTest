# from gettext import find
from importlib.resources import path
import os
import pathlib
currentdirpath = pathlib.Path().resolve()
rez = os.listdir(currentdirpath)
# print('current rez', rez)

folderAndCount = []






def returnFolders(currentFolderPath):
    # currentFolderPath = pathlib.Path(currentFolderPath)

    countOfFolders  = 0
    arrayOfFoldersPath  = []
    namesOfFolder = []

    listOfAllFiles = os.listdir(currentFolderPath)
    for i in listOfAllFiles:
        currentFilesPath = currentFolderPath.joinpath(i)
        if(os.path.isdir(currentFilesPath)):
            namesOfFolder.append(i)
            arrayOfFoldersPath.append(currentFilesPath.__str__())
            countOfFolders=countOfFolders+1
    return (namesOfFolder,arrayOfFoldersPath,countOfFolders)




# print(returnFolders(currentdirpath)[0])
def returnFolderFirstLevel():
    folderPath = pathlib.Path().resolve()
    data = returnFolders(folderPath)
    findArray = [data[0],data[1]]
    countArray=[]
    print('Только имена',data[0])
    print('Только только пути', data[1])
    print('Только количество', data[2])
    for i in data[1]:
        print('itemssssssssssss',returnFolders(pathlib.Path(i))[2])
        countArray.append(returnFolders(pathlib.Path(i))[2])

    with open('./foo.txt', 'w') as fp:
        allscene = 0
        allarea = 0
        for i in range(countArray.__len__()):
            allscene = allscene+float(countArray[i])/2
            allarea = allarea+float(countArray[i])*400/2
            print(i)
            fp.write(str(data[0][i])+'\t' + str(float(countArray[i])/2)+'\n')
        # fp.write(str('summ'+'\t'+str(allscene)+'\t'+str(allarea)))
    print(countArray.__len__())
    print('Finish Arrat', data[0], countArray)

# text = 'sdfgsdfgsdfgsdfg'

    



returnFolderFirstLevel()

# type(float(5))


    # rez = os.path.isdir(filePath)
    # print('123123123')



# returnFolders()
# # folderAndCount.append('asd')
# for a in rez:
#     filePath = currentdirpath.joinpath(a)
#     print(filePath,'is dir?',os.path.isdir(filePath))
#     if(os.path.isdir(filePath)):
#         folderAndCount.append(filePath.__str__())

# print(folderAndCount)
#     # filePathSring=(filePath.__str__())
#     # print(type(filePathSring))
#     # print (filePath.__str__()+" "+'YYYYeeeeeesssss')





# newfilePath = currentdirpath.joinpath('A1')
# print('new joined concurrent',newfilePath)
# print(os.path.isdir(newfilePath))
# rez = os.listdir(currentdirpath)

# # stringCurrentdirPath = "C:\Users\A.Agadilov\Desktop\python_auto"
# # print()
# print(type(currentdirpath))

# print("current path",currentdirpath)
# # print("current path"+stringCurrentdirPath)

# rez = os.listdir(currentdirpath)
# for a in rez:
#     print(currentdirpath.joinpath(a))




# print(rez)

# os.path.isdir('C:\Users\A.Agadilov\Desktop\автоматизация рутинных задач в python')
# print(rez)
# print(os.path.isdir(rez[0]))

# for root, dirs, files in os.walk('C:\Users\A.Agadilov\Desktop\python_auto'):
    
#     print(root, "consumes", end=" ")
#     print(sum(getsize(join(root, name)) for name in files), end=" ")
#     print("bytes in", len(files), "non-directory files")
#     if 'CVS' in dirs:
#         dirs.remove('CVS')  # don't visit CVS directories

# perem = os.path.isdir('C:\Users\A.Agadilov\Desktop\python_auto\A1')
# print(perem)
# print(os.path.dirname())
# for current_dir, dirs, files in os.walk(".",topdown=True):
#     print('current directory' + current_dir,'seondary' + dirs)
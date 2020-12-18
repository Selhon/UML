from Book import Book

#книги

HeavenAndHell = Book("Рай и Ад","Умар Сулейман аль-Ашкар","Philosophy","012313735","ОЛСАА У Э38/А-984","Russian","","Универсальный читальный зал",open('ContentBooks/HeavenAndHell.txt', 'r'),True)
LawsOfPower = Book("48 законов власти","Грин, Роберт","Social literature","012338931","2020-3/13261 У С550.51/Г-850","Russian","","Универсальный читальный зал",open('ContentBooks/48 laws of power.txt', 'r'),True)
ArtificialIntelligenceSuperpowers = Book("Сверхдержавы искусственного интеллекта : Китай, Кремниевая долина и новый мировой порядок","Кай-Фу Ли","Social literature","012319639","2020-7/2919 У З813/Л-550","Russian","","Русский книжный фонд",open('ContentBooks/Artificial intelligence superpowers.txt', 'r'),True)

#коллекции
collectionUniversalReadingRoom=["Универсальный читальный зал",HeavenAndHell,LawsOfPower]
collectionRussianBookFund=["Русский книжный фонд",ArtificialIntelligenceSuperpowers]
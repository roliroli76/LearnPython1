listColors = ["red", "orange", "green", "violet", "blue", "yellow"]

def need_color(listColors, n):
    return(listColors[:n])

for n in range(len(listColors)):
    print(need_color(listColors, n))


writing = "Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli."
print(writing[3:56])



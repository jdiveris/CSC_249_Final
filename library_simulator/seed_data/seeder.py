from library_simulator.models.book import Book
from library_simulator.models.library_card import LibraryCard


def seed_books():
    """
    Creates a dictionary of 40 predefined Book objects.

    Returns:
        dict: A dictionary mapping ISBN strings to Book objects.
    """
    return {
        "9780143127741": Book("9780143127741", "Yuval Noah Harari", "Sapiens", total_copies=3),
        "9780451524935": Book("9780451524935", "George Orwell", "1984", total_copies=4),
        "9780062316097": Book("9780062316097", "Paulo Coelho", "The Alchemist", total_copies=5),
        "9780061120084": Book("9780061120084", "Harper Lee", "To Kill a Mockingbird", total_copies=4),
        "9780140449266": Book("9780140449266", "Homer", "The Odyssey", total_copies=2),
        "9780141439518": Book("9780141439518", "Jane Austen", "Pride and Prejudice", total_copies=4),
        "9780441172719": Book("9780441172719", "Frank Herbert", "Dune", total_copies=3),
        "9780486282114": Book("9780486282114", "Mary Shelley", "Frankenstein", total_copies=3),
        "9780060850524": Book("9780060850524", "Aldous Huxley", "Brave New World", total_copies=2),
        "9780316769488": Book("9780316769488", "J.D. Salinger", "The Catcher in the Rye", total_copies=4),
        "9780142437179": Book("9780142437179", "Herman Melville", "Moby-Dick", total_copies=3),
        "9780743273565": Book("9780743273565", "F. Scott Fitzgerald", "The Great Gatsby", total_copies=5),
        "9780547928227": Book("9780547928227", "J.R.R. Tolkien", "The Hobbit", total_copies=3),
        "9780679734505": Book("9780679734505", "Fyodor Dostoevsky", "Crime and Punishment", total_copies=4),
        "9780451419439": Book("9780451419439", "Victor Hugo", "Les Misérables", total_copies=2),
        "9780141441146": Book("9780141441146", "Charlotte Brontë", "Jane Eyre", total_copies=4),
        "9780140448955": Book("9780140448955", "Dante Alighieri", "The Divine Comedy", total_copies=3),
        "9780374528379": Book("9780374528379", "Fyodor Dostoevsky", "The Brothers Karamazov", total_copies=3),
        "9781451673319": Book("9781451673319", "Ray Bradbury", "Fahrenheit 451", total_copies=3),
        "9780618640157": Book("9780618640157", "J.R.R. Tolkien", "The Lord of the Rings", total_copies=5),
        "9780553380163": Book("9780553380163", "Bill Bryson", "A Short History of Nearly Everything", total_copies=3),
        "9780141182803": Book("9780141182803", "Franz Kafka", "The Trial", total_copies=2),
        "9780143058144": Book("9780143058144", "Sylvia Plath", "The Bell Jar", total_copies=3),
        "9780812981605": Book("9780812981605", "Daniel Kahneman", "Thinking, Fast and Slow", total_copies=4),
        "9780812988406": Book("9780812988406", "Tara Westover", "Educated", total_copies=3),
        "9780140283334": Book("9780140283334", "Yann Martel", "Life of Pi", total_copies=4),
        "9780375703768": Book("9780375703768", "Toni Morrison", "Beloved", total_copies=2),
        "9780743247542": Book("9780743247542", "Khaled Hosseini", "The Kite Runner", total_copies=3),
        "9780156012195": Book("9780156012195", "Antoine de Saint-Exupéry", "The Little Prince", total_copies=5),
        "9780060883287": Book("9780060883287", "Malcolm Gladwell", "Outliers", total_copies=3),
        "9780307278449": Book("9780307278449", "Cormac McCarthy", "The Road", total_copies=2),
        "9781400033416": Book("9781400033416", "Jeffrey Eugenides", "Middlesex", total_copies=3),
        "9780316769532": Book("9780316769532", "Kurt Vonnegut", "Slaughterhouse-Five", total_copies=4),
        "9780307387899": Book("9780307387899", "Junot Díaz", "The Brief Wondrous Life of Oscar Wao", total_copies=3),
        "9780062024039": Book("9780062024039", "Susan Cain", "Quiet", total_copies=3),
        "9780142437230": Book("9780142437230", "Bram Stoker", "Dracula", total_copies=2),
        "9780451205766": Book("9780451205766", "Ayn Rand", "Atlas Shrugged", total_copies=3),
        "9780374533557": Book("9780374533557", "Haruki Murakami", "Norwegian Wood", total_copies=2),
        "9780140449334": Book("9780140449334", "Leo Tolstoy", "War and Peace", total_copies=3),
        "9780679783272": Book("9780679783272", "Oscar Wilde", "The Picture of Dorian Gray", total_copies=3),
    }



def seed_library_cards():
    """
    Creates a dictionary of 20 mock LibraryCard objects.

    Returns:
        dict: A dictionary mapping LibraryCard IDs to LibraryCard objects.
    """
    return {
        "card001": LibraryCard("card001"),
        "card002": LibraryCard("card002"),
        "card003": LibraryCard("card003"),
        "card004": LibraryCard("card004"),
        "card005": LibraryCard("card005"),
        "card006": LibraryCard("card006"),
        "card007": LibraryCard("card007"),
        "card008": LibraryCard("card008"),
        "card009": LibraryCard("card009"),
        "card010": LibraryCard("card010"),
        "card011": LibraryCard("card011"),
        "card012": LibraryCard("card012"),
        "card013": LibraryCard("card013"),
        "card014": LibraryCard("card014"),
        "card015": LibraryCard("card015"),
        "card016": LibraryCard("card016"),
        "card017": LibraryCard("card017"),
        "card018": LibraryCard("card018"),
        "card019": LibraryCard("card019"),
        "card020": LibraryCard("card020"),
    }
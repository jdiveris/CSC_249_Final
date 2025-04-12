from library_simulator.models.book import Book
from library_simulator.models.card_holder import Cardholder


def seed_books():
    """
    Creates a dictionary of 40 predefined Book objects.

    Returns:
        dict: A dictionary mapping ISBN strings to Book objects.
    """
    return {
        "9780143127741": Book("9780143127741", "Sapiens", "Yuval Noah Harari", total_copies=3),
        "9780451524935": Book("9780451524935", "1984", "George Orwell", total_copies=4),
        "9780062316097": Book("9780062316097", "The Alchemist", "Paulo Coelho", total_copies=5),
        "9780061120084": Book("9780061120084", "To Kill a Mockingbird", "Harper Lee", total_copies=4),
        "9780140449266": Book("9780140449266", "The Odyssey", "Homer", total_copies=2),
        "9780141439518": Book("9780141439518", "Pride and Prejudice", "Jane Austen", total_copies=4),
        "9780441172719": Book("9780441172719", "Dune", "Frank Herbert", total_copies=3),
        "9780486282114": Book("9780486282114", "Frankenstein", "Mary Shelley", total_copies=3),
        "9780060850524": Book("9780060850524", "Brave New World", "Aldous Huxley", total_copies=2),
        "9780316769488": Book("9780316769488", "The Catcher in the Rye", "J.D. Salinger", total_copies=4),
        "9780142437179": Book("9780142437179", "Moby-Dick", "Herman Melville", total_copies=3),
        "9780743273565": Book("9780743273565", "The Great Gatsby", "F. Scott Fitzgerald", total_copies=5),
        "9780547928227": Book("9780547928227", "The Hobbit", "J.R.R. Tolkien", total_copies=3),
        "9780679734505": Book("9780679734505", "Crime and Punishment", "Fyodor Dostoevsky", total_copies=4),
        "9780451419439": Book("9780451419439", "Les Misérables", "Victor Hugo", total_copies=2),
        "9780141441146": Book("9780141441146", "Jane Eyre", "Charlotte Brontë", total_copies=4),
        "9780140448955": Book("9780140448955", "The Divine Comedy", "Dante Alighieri", total_copies=3),
        "9780374528379": Book("9780374528379", "The Brothers Karamazov", "Fyodor Dostoevsky", total_copies=3),
        "9781451673319": Book("9781451673319", "Fahrenheit 451", "Ray Bradbury", total_copies=3),
        "9780618640157": Book("9780618640157", "The Lord of the Rings", "J.R.R. Tolkien", total_copies=5),
        "9780553380163": Book("9780553380163", "A Short History of Nearly Everything", "Bill Bryson", total_copies=3),
        "9780141182803": Book("9780141182803", "The Trial", "Franz Kafka", total_copies=2),
        "9780143058144": Book("9780143058144", "The Bell Jar", "Sylvia Plath", total_copies=3),
        "9780812981605": Book("9780812981605", "Thinking, Fast and Slow", "Daniel Kahneman", total_copies=4),
        "9780812988406": Book("9780812988406", "Educated", "Tara Westover", total_copies=3),
        "9780140283334": Book("9780140283334", "Life of Pi", "Yann Martel", total_copies=4),
        "9780375703768": Book("9780375703768", "Beloved", "Toni Morrison", total_copies=2),
        "9780743247542": Book("9780743247542", "The Kite Runner", "Khaled Hosseini", total_copies=3),
        "9780156012195": Book("9780156012195", "The Little Prince", "Antoine de Saint-Exupéry", total_copies=5),
        "9780060883287": Book("9780060883287", "Outliers", "Malcolm Gladwell", total_copies=3),
        "9780307278449": Book("9780307278449", "The Road", "Cormac McCarthy", total_copies=2),
        "9781400033416": Book("9781400033416", "Middlesex", "Jeffrey Eugenides", total_copies=3),
        "9780316769532": Book("9780316769532", "Slaughterhouse-Five", "Kurt Vonnegut", total_copies=4),
        "9780307387899": Book("9780307387899", "The Brief Wondrous Life of Oscar Wao", "Junot Díaz", total_copies=3),
        "9780062024039": Book("9780062024039", "Quiet", "Susan Cain", total_copies=3),
        "9780142437230": Book("9780142437230", "Dracula", "Bram Stoker", total_copies=2),
        "9780451205766": Book("9780451205766", "Atlas Shrugged", "Ayn Rand", total_copies=3),
        "9780374533557": Book("9780374533557", "Norwegian Wood", "Haruki Murakami", total_copies=2),
        "9780140449334": Book("9780140449334", "War and Peace", "Leo Tolstoy", total_copies=3),
        "9780679783272": Book("9780679783272", "The Picture of Dorian Gray", "Oscar Wilde", total_copies=3),
    }


def seed_cardholders():
    """
    Creates a dictionary of 20 mock Cardholder objects.

    Returns:
        dict: A dictionary mapping cardholder IDs to Cardholder objects.
    """
    return {
        "card001": Cardholder("card001"),
        "card002": Cardholder("card002"),
        "card003": Cardholder("card003"),
        "card004": Cardholder("card004"),
        "card005": Cardholder("card005"),
        "card006": Cardholder("card006"),
        "card007": Cardholder("card007"),
        "card008": Cardholder("card008"),
        "card009": Cardholder("card009"),
        "card010": Cardholder("card010"),
        "card011": Cardholder("card011"),
        "card012": Cardholder("card012"),
        "card013": Cardholder("card013"),
        "card014": Cardholder("card014"),
        "card015": Cardholder("card015"),
        "card016": Cardholder("card016"),
        "card017": Cardholder("card017"),
        "card018": Cardholder("card018"),
        "card019": Cardholder("card019"),
        "card020": Cardholder("card020"),
    }

class DataBaseService:
  @staticmethod
  def full(a):
    a.append(
    {
      "author": "Jerome Salinger",
        "book_name": "The Catcher in the Rye",
        "publishing_house" : "Testpublishing_house",
        "year": "1951",
        "annotation": "The Catcher in the Rye is told from the first person point of view of Holden Caulfield, a teenager living in New York City in the late 1940’s. Holden’s ambivalence about the adult world drives the novel’s conflicts and provokes questions about human behavior.",
        "rubricator": "novel"
    }
    )
    a.append(
    {
      "author": "Stephen Hawking",
        "book_name": "The Theory of Everything",
        "publishing_house" : "Phoenix Books and Audio",
        "year": "2006",
        "annotation": "Stephen Hawking is widely believed to be one of the world’s greatest minds: a brilliant theoretical physicist whose work helped to reconfigure models of the universe and to redefine what’s in it. Imagine sitting in a room listening to Hawking discuss these achievements and place them in historical context. It would be like hearing Christopher Columbus on the New World. Hawking presents a series of seven lec-tures—covering everything from big bang to black holes to string theory—that capture not only the brilliance of Hawking’s mind but his characteristic wit as well. Of his research on black holes, which absorbed him for more than a decade, he says, “It might seem a bit like looking for a black cat in a coal cellar.” Hawking begins with a history of ideas about the universe, from Aristotle’s determination that the Earth is round to Hubble’s discovery, over 2000 years later, that the universe is expanding. Using that as a launching pad, he explores the reaches of modern physics, including theories on the origin of the universe (e.g., the big bang), the nature of black holes, and space-time.",
        "rubricator": "scientific"
    }
    )
    a.append(
    {
      "author": "William Gerald Golding",
        "book_name": "Lord of the Flies",
        "publishing_house" : "Faber and Faber",
        "year": "1954",
        "annotation": "The book begins with the boys arriving on the island after their plane has been shot down during what seems to be part of a nuclear World War III.[3] Some of the marooned characters are ordinary students, while others arrive as a musical choir under an established leader. With the exception of Sam and Eric and the choirboys, they appear never to have encountered each other before. The book portrays their descent into savagery; left to themselves on a paradisiacal island, far from modern civilization, the well-educated boys regress to a primitive state.",
        "rubricator": "novel"
    }
    )
    a.append(
    {
      "author": "Charlotte Brontë",
        "book_name": "Jane Eyre",
        "publishing_house" : "Smith, Elder & Company",
        "year": "1847",
        "annotation": "The novel revolutionised prose fiction by being the first to focus on its protagonist's moral and spiritual development through an intimate first-person narrative, where actions and events are coloured by a psychological intensity. Charlotte Brontë has been called the first historian of the private consciousness, and the literary ancestor of writers like Proust and Joyce.",
        "rubricator": "drama"
    }
    )
    a.append(
    {
      "author": "Arkady and Boris Strugatsky",
        "book_name": "Hard to Be a God",
        "publishing_house" : "AST",
        "year": "1963",
        "annotation": "This 1963 masterpiece is widely considered one of the best novels of the greatest Russian writers of science fiction. Yet until now the only English version (unavailable for over thirty years) was based on a German translation, and was full of errors, infelicities, and misunderstandings. Now, in a new translation by Olena Bormashenko, whose translation of the authors’ Roadside Picnic has received widespread acclaim, here is the definitive edition of this brilliant work. It tells the story of Don Rumata, who is sent from Earth to the medieval kingdom of Arkanar with instructions to observe and to save what he can. Masquerading as an arrogant nobleman, a dueler and a brawler, Don Rumata is never defeated, but can never kill. With his doubt and compassion, and his deep love for a local girl named Kira, Rumata wants to save the kingdom from the machinations of Don Reba, the first minister to the king. But given his orders, what role can he play? Hard to Be a God has inspired a role-playing video game and two movies, including Aleksei German’s long-awaited swan song. This long overdue translation will reintroduce one of the most profound Soviet-era novels to an eager audience.",
        "rubricator": "science fiction"
    }
    )
    return (a)
